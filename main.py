"""
Code to convert text translation from any language to any other language
"""
from tempfile import NamedTemporaryFile
import time
from googletrans import Translator
from gtts import gTTS
import pygame
pygame.init() # Using pygame for playing the audio - converted speech
INPUT_STRING="Hello, My name is Ram"
translator = Translator()
translated = translator.translate(INPUT_STRING, dest='ta')
def convert_tamil_to_speech(tamil_text):
    '''
    Convert tamil text to speech and saves the instance of mp3 file
    '''
    tts = gTTS(text=tamil_text, lang='ta')
    tts_file = NamedTemporaryFile(suffix='.mp3')
    tts.save(tts_file.name)
    return tts_file
tamil_translation = translated.text
tts_file = convert_tamil_to_speech(tamil_translation)
pygame.mixer.music.load(tts_file.name)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
# Lets user to stop by pressing enter
# input("Press enter to stop playback...")
# pygame.mixer.music.stop()

'''
Take input from user by speech
recognize the language 
if its non-english, translate it to english;
prompt it to llm
get the answer from llm 
translate it to recognized langauge
and respond to the user 
'''
