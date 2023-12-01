import speech_recognition as sr
import asyncio

# Upcoming : 
# Send the text to llm - 
# infer the text file that is sent 


r = sr.Recognizer()
async def google_translator(audio):
    try:
        text = r.recognize_google(audio)
        print(text)
        return text
    except r.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except r.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))    

async def sphinx_translator(audio):
    try:
        text = r.recognize_sphinx(audio)
        print(text)        
        return text
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

async def main():
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            # read the audio data from the default microphone
            # audio = r.record(source, duration=5)
            audio = r.listen(source)
            # recognize speech using google
            await google_translator(audio)
            # await sphinx_translator(audio) # sphinx requires downloading the file to 


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

