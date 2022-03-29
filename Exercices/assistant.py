import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('volume', 'com.apple.speech.synthesis.voice.french.premiere')


#  The Main Part (Listens to the voice)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# def ecouter():
#     try:
#         with sr.Microphone() as source:
#             print("parlez maintenant")
#             voix = listener.listen(source)
#             command = listener.recognize_google(voix, language='fr-FR')
#             command.lower()
#     except sr.UnknownValueError:
#         pass
#     return command


while True:
    with sr.Microphone() as source:
        print("Say Something:  ")
        audio = r.listen(source)  # Starts listening

        try:
            text = r.recognize_google(audio).lower()
            print(f'You said : {text}')
            command = r.listen().recognize_google(audio, language='fr-FR')

        except:
            print('Sorry I could not recognize your voice')

        if 'what is the time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'wikipedia' in text:
            speak('Searching Wikipedia...')
            text = text.replace('wikipedia', '')
            webbrowser.open(f'https://en.wikipedia.org/wiki/{text}')
            results = wikipedia.summary(text, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'search in google' in text:
            speak('What do you want to search?')
            text = text.replace('search in google', '')
            webbrowser.open(f'https://google.com/search?q={text}')

        elif 'search in youtube' in text:
            speak('What do you want to search?')
            text = text.replace('search in youtube', '')
            webbrowser.open(f'https://youtube.com/results?search_query={text}')

        elif 'open youtube' in text:
            speak('Opening Youtube')
            webbrowser.open('https://www.youtube.com/watch?v')

        elif 'open stackoverflow' in text:
            speak('Opening Stackoverflow')
            webbrowser.open('https://stackoverflow.com')

        elif 'open github' in text:
            speak('Opening Github')
            webbrowser.open('https://github.com')

        elif 'open coda' in text:
            speak('Opening Coda')
            webbrowser.open('https://www.coda.io')

        else:
            speak('I do not understand')

#  The End
