import multiprocessing
import re
from threading import Thread

import pyttsx3
import speech_recognition as sr
from langchain_community.llms.ollama import Ollama


def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


@threaded
def manage_process(p):
    global term
    while p.is_alive():
        if term:
            p.terminate()
            term = False
        else:
            continue


def say(phrase):
    global t
    global term
    term = False
    p = multiprocessing.Process(target=speak, args=(phrase,))
    p.start()
    t = manage_process(p)


def speak(phrase):
    engine = pyttsx3.init()
    engine.say(phrase)
    engine.runAndWait()
    engine.stop()


def stop_speaker():
    global term
    term = True
    t.join()


def listen():
    r = sr.Recognizer()
    print("Listening...")
    while True:
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, 60, 30)
                return r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Still listening")
        except sr.RequestError:
            print("Still listening")


def process(llm: Ollama, text):
    print(f"You: {text}")
    response = llm.invoke(text)
    response = clean_response(response)
    print(f"AI: {response}")
    return response


def clean_response(text):
    return re.sub(r"[^a-zA-Z0-9\s\-=\+\-\*/]", "", text)


if __name__ == "__main__":
    llm = Ollama(
        model="gemma:2b",
        stop=[],
        system="You are a sharp assistant. Provide brief and short answers.",
    )

    while True:
        try:
            text = listen()
            response = process(llm, text)
            say(response)
        except KeyboardInterrupt:
            stop_speaker()
            break
