from whisper_live.client import TranscriptionClient

client = TranscriptionClient(
    "localhost",
    9090,
    is_multilingual=False,
    translate=True,
    model_size="tiny",
)

client()
