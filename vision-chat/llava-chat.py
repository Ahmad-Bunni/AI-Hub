import base64
from io import BytesIO

from langchain_ollama import ChatOllama
from PIL import Image

llava = ChatOllama(model="llava")


def convert_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


pil_image = Image.open("sample.jpg")
image_b64 = convert_to_base64(pil_image)

llm_with_image_context = llava.bind(images=[image_b64])
result = llm_with_image_context.invoke("extract the information in json format")

print(result)
