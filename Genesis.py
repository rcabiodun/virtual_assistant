from speech_recognition import *
import pyttsx3
import pywhatkit
import datetime
import random
import wikipedia
#import os
from pygame import mixer
from pathlib import Path
#from pathlib import *



mixer.init()





listener = Recognizer()
engine = pyttsx3.init()
#voice = engine.getProperty('voices')
#engine.setProperty('voice', voice[2].id)
engine.setProperty('rate', 142)
grt = "sir"


def talk(text):
    engine.say(text)
    engine.runAndWait()

#if this is not done,it would be referenced before assignment
command = ""


def take_in():

    try:
        with Microphone() as mic:
            global command
            print("listening...")
            my_voice = listener.listen(mic)
            command = listener.recognize_google(my_voice)
            command = command.lower()

            if "genesis" in command:
                command = command.replace("genesis", " ")
                print(command)
    except:
        pass
    return command

def play_all():
    p = Path("C:/Users/personal/Music/")
    l = []
    l.extend(list(p.glob('*.mp3')))
    random.shuffle(l)
    print(l)

    for song in l:
        mixer.music.load(song)
        mixer.music.play()
        query = input(">>>")
        if query == "exit":
            mixer.music.stop()
            break
        while mixer.music.get_busy() == True:
            continue


def wake():
    hr = datetime.datetime.now().strftime('%H')
    int_hr = int(hr)
    after_noon = 12
    evening = 18
    morning = 0

    if (int_hr > morning) and (int_hr < after_noon):
        print("Good morning " + grt)
        talk("good morning" + grt)
        talk("the quote of the day is")
        talk(quotes())

    elif (int_hr > after_noon) and (int_hr < evening):
        talk("Good afternoon" + grt)

    else:
        print("Good evening sir")
        talk("Good evening" + grt)


def quotes():
    quo = ["'never complain about life, just adapt'  BY Big Sean",
           " 'there are no mistakes in life,only lessons'  BY Big Sean", "'Reality is often disappointing' BY Thanos",
           "'life is what happens when you are too busy making other plans' BY John Lennon",
           "'You live only once, but if you do it right,once is enough' BY Mae West "]
    quote = random.choice(quo)
    print(quote)
    return quote


def run_genesis():
    cmd = take_in()
    if "open youtube and search for" in cmd:
        songgg = cmd.replace("play", "")
        talk("playing" + songgg)
        print("playing" + songgg)
        pywhatkit.playonyt(songgg)


    if "the time" in cmd:
        tim = datetime.datetime.now()
        timm = tim.strftime("%H;%M")
        print(grt + " the current time is " + timm)
        talk(grt + "the current time is" + timm)



    if "who is" in cmd:
        print(cmd)
        person = cmd.replace("who is", "")
        info = wikipedia.summary(person, 2)
        talk(grt + info)

    if "search for" in cmd:
        src = cmd.replace("search for", "")
        talk("here are the top results" + grt)
        pywhatkit.search(src)

    if "today's date" in cmd:
        date = datetime.datetime.now()
        datee = date.strftime("%Y;%M;D")
        talk("today's date is " + datee)

    if "shut down" in cmd:
        print("shutting down")
        talk("shutting down in 50 seconds")
        pywhatkit.shutdown(50)

    #if the play command is used after each song played,genesis won't loop unless you stop the player by typing "s"
    #it goes directly to music folder and nowhere else
    if "play" in cmd:

        sun=cmd.lstrip("play ")
        mp = ".mp3"
        song = sun + mp
        print("playing "+sun)
        talk("playing"+sun)
        p = Path("C:/Users/personal/Music/")
        song = Path("C:/Users/personal/Music/" + song)
        if song in list(p.glob("*")):
            mixer.music.load(song)
            mixer.music.play()

            while True:
                query = input(">>>")

                if query == "p":
                    mixer.music.pause()
                elif query == "pl":
                    mixer.music.unpause()
                elif query == "s":
                    mixer.music.stop()
                    break

    if "play everything" in cmd:
        play_all()

wake()
while True:
    run_genesis()
