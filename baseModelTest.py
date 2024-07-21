import os
from dotenv import load_dotenv
from deepgram import Deepgram
import asyncio
import json

# .env dosyasını yükleyin
load_dotenv()

# Ses dosyasının yolu
AUDIO_FILE = "audio/8842-304647-0013.flac"

# Deepgram API anahtarı
API_KEY = os.getenv("DG_API_KEY")

print(f"API_KEY: {API_KEY}")
if not API_KEY:
    raise ValueError("API key is missing. Please check your .env file.")


async def transcribe_audio():
    try:
        # Deepgram istemcisini oluşturma
        deepgram = Deepgram(API_KEY)

        # Ses dosyasını okutma
        with open(AUDIO_FILE, "rb") as audio_file:
            buffer_data = audio_file.read()

        print(f"Audio file path: {AUDIO_FILE}")
        if not os.path.exists(AUDIO_FILE):
            raise FileNotFoundError(f"Audio file not found: {AUDIO_FILE}")

        # Ses kaynağı
        source = {
            "buffer": buffer_data,
            "mimetype": "audio/flac"
        }

        #Transkriptin özellikleri
        options = {
            "model": "base",
            "language": "en",
            "smart_format": True,
        }

        # Deepgram API çağrısı
        response = await deepgram.transcription.prerecorded(source, options)

        response = await deepgram.transcription.prerecorded(source, options)

        print(f"API response: {response}")

        if not response:
            print("Empty response received.")
        else:
            response_json = json.dumps(response, indent=4, ensure_ascii=False)
            print(response_json)

            with open("transcription.json", "w", encoding="utf-8") as json_file:
                json_file.write(response_json)

        # Yanıtı yazdırma
        response_json = json.dumps(response, indent=4, ensure_ascii=False)
        print(response_json)

        with open("transcription.json", "w", encoding="utf-8") as json_file:
            json_file.write(response_json)

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    asyncio.run(transcribe_audio())
