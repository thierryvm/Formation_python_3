# import speech_recognition as sr
# import pyttsx3
# import datetime
# import wikipedia
# import webbrowser

# r = sr.Recognizer()
# engine = pyttsx3.init()
# engine.setProperty('volume', 'com.apple.speech.synthesis.voice.french.premiere')
#
#
# #  The Main Part (Listens to the voice)
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
#
#
# # def ecouter():
# #     try:
# #         with sr.Microphone() as source:
# #             print("parlez maintenant")
# #             voix = listener.listen(source)
# #             command = listener.recognize_google(voix, language='fr-FR')
# #             command.lower()
# #     except sr.UnknownValueError:
# #         pass
# #     return command
#
#
# while True:
#     with sr.Microphone() as source:
#         print("Say Something:  ")
#         audio = r.listen(source)  # Starts listening
#
#         try:
#             text = r.recognize_google(audio).lower()
#             print(f'You said : {text}')
#             command = r.listen().recognize_google(audio, language='fr-FR')
#
#         except:
#             print('Sorry I could not recognize your voice')
#
#         if 'what is the time' in text:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f'Sir, the time is {strTime}')
#
#         elif 'wikipedia' in text:
#             speak('Searching Wikipedia...')
#             text = text.replace('wikipedia', '')
#             webbrowser.open(f'https://en.wikipedia.org/wiki/{text}')
#             results = wikipedia.summary(text, sentences=2)
#             speak('According to Wikipedia')
#             print(results)
#             speak(results)
#
#         elif 'search in google' in text:
#             speak('What do you want to search?')
#             text = text.replace('search in google', '')
#             webbrowser.open(f'https://google.com/search?q={text}')
#
#         elif 'search in youtube' in text:
#             speak('What do you want to search?')
#             text = text.replace('search in youtube', '')
#             webbrowser.open(f'https://youtube.com/results?search_query={text}')
#
#         elif 'open youtube' in text:
#             speak('Opening Youtube')
#             webbrowser.open('https://www.youtube.com/watch?v')
#
#         elif 'open stackoverflow' in text:
#             speak('Opening Stackoverflow')
#             webbrowser.open('https://stackoverflow.com')
#
#         elif 'open github' in text:
#             speak('Opening Github')
#             webbrowser.open('https://github.com')
#
#         elif 'open coda' in text:
#             speak('Opening Coda')
#             webbrowser.open('https://www.coda.io')
#
#         else:
#             speak('I do not understand')
#
# #  The End


import sys
import webbrowser

import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("voice", "french")
engine.setProperty("rate", 175)
voices = engine.getProperty('voices')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def greetMe():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        talk('Bonjour Thierry')

    if 12 <= current_hour < 18:
        talk('Bon après midi Thierry!')

    if current_hour >= 18 and current_hour != 0:
        talk('Bonsoir Thierry!')


# set french voice
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.french.premiere')
greetMe()
engine.say('comment vas tu?')
# engine.say('Que puis-je faire pour t'aider ?')
engine.runAndWait()


def alexa_command():
    with sr.Microphone() as source:
        print("listening...")
        listener.pause_threshold = 0.5
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="fr-FR")
        command = command.lower()
        print(command)
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
    return command


def run_alexa():  # sourcery no-metrics
    command = alexa_command()
    if 'musique' in command:
        song = command.replace('musique', '')
        talk('musique en cours....')
        print(song)
        pywhatkit.playonyt(song)
    elif 'heure' in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk(f'il est actuelement: {time}')
    elif 'qui est' in command:
        person = command.replace("qui est", "")
        wikipedia.set_lang("fr")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'google' in command:
        search = command.replace("google", "")
        webbrowser.open(f'https://google.com/search?q={search}')
    elif 'youtube' in command:
        search = command.replace("youtube", "")
        webbrowser.open(f'https://youtube.com/results?search_query={search}')
    elif 'ouvre coda' in command:
        webbrowser.open('https://www.coda.io')
    elif 'ouvre Notion' in command:
        webbrowser.open('https://www.notion.so/Dashboard-51614fc1cfae4f03ae360015a3e775d2')
    elif 'ouvre github' in command:
        webbrowser.open('https://github.com')
    elif 'ouvre stackoverflow' in command:
        webbrowser.open('https://stackoverflow.com')
    elif 'ouvre youtube' in command:
        webbrowser.open('https://www.youtube.com')
    elif 'ouvre google' in command:
        webbrowser.open('https://www.google.com')
    elif 'ouvre wikipedia' in command:
        webbrowser.open('https://www.wikipedia.org')
    elif 'jouer' in command:
        talk('quel est le nom de la musique?')
        song = command.replace('jouer', '')
        print(song)
        pywhatkit.playonyt(song)
    elif "sortir" in command:
        talk("Désolé, je suis un peu souffrante en ce moment.")
    elif "es-tu en couple" in command:
        talk("non pas encore, mon coeur est encore à conquérir.")
    elif "blague" in command:
        jokes = [
            "C’est la maîtresse qui demande à Toto « Cite-moi un mammifère qui n’a pas de dents »… « Ma grand-mère ? »",
            "C’est l’histoire de la maîtresse qui demande à Toto : « Récite-moi le verbe marcher au présent. » Toto "
            "répond ",
            "« Je…marche…tu…tu…marches… », mais la maîtresse le presse, allez, plus vite Toto ! "
            "Ce à quoi il répond « je cours ..…tu cours il court… »",]
        talk(random.choice(jokes))
    elif "et toi" in command:
        msgs = ["Je fais juste mon truc !", "Je vais bien !", "Bien !", "Je suis bien et plein d'énergie."]
        talk(random.choice(msgs))
    elif "tu es" in command:
        msgs = ["Je suis bien.", "Je suis bien et plein d'énergie.", "Je suis bien et je suis plein d'énergie."]
        talk(random.choice(msgs))
    elif "désactive toi" in command:
        talk("merci de m'avoir utilisé, Thierry !")
        sys.exit()

    else:
        talk("pourrais tu repété? je n'ai pas bien compris.")


if __name__ == '__main__':
    while True:
        run_alexa()
