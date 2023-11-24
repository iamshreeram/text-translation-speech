from googletrans import Translator
from gtts import gTTS
import pygame
from tempfile import NamedTemporaryFile

translator = Translator()
translated = translator.translate('veritas lux mea', src='la', dest='ta')

def convert_tamil_to_speech(tamil_text):
    tts = gTTS(text=tamil_text, lang='ta')
    tts_file = NamedTemporaryFile(suffix='.mp3')
    tts.save(tts_file.name)
    return tts_file

tamil_translation = translated.text
tts_file = convert_tamil_to_speech(tamil_translation)

pygame.init()

pygame.mixer.music.load(tts_file.name)
pygame.mixer.music.play()

input("Press enter to stop playback...")
pygame.mixer.music.stop()
