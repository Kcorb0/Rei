import os
import json
from playsound import playsound
from google.cloud import texttospeech as tts

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "rei/utils/configs/credentials.json"


def text_to_speech(text: str):
    configs = voice_configs()
    synthesizer_input = tts.SynthesisInput(text=text)
    voice = tts.VoiceSelectionParams(
        language_code=configs["languageCode"], name=configs["voiceId"]
    )

    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.LINEAR16,
        pitch=configs["pitch"],
        speaking_rate=configs["speakingRate"],
    )

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=synthesizer_input, voice=voice, audio_config=audio_config
    )

    with open("rei/utils/audio_output/output.wav", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.wav"')

    playsound("rei/utils/audio_output/output.wav")


def voice_configs():
    voice_configs_file = open("rei/utils/configs/main-voice.json")
    voice_id = json.load(voice_configs_file)

    configs = {
        "pitch": voice_id["audioConfig"]["pitch"],
        "speakingRate": voice_id["audioConfig"]["speakingRate"],
        "languageCode": voice_id["voice"]["languageCode"],
        "voiceId": voice_id["voice"]["name"],
    }

    return configs
