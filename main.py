import datetime
import operator
import os
import smtplib
import subprocess
import sys
import random
import re
import webbrowser
from googlesearch import search
import webbrowser as web
from os import startfile
from time import sleep
import time
import psutil
#import pygame
import pyjokes
import pyttsx3
import pywhatkit
import requests
import screen_brightness_control as sbc
import speech_recognition as sr
import wikipedia
#from PIL import Image
from bs4 import BeautifulSoup
from halo import Halo
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from playsound3 import playsound
from pyautogui import click
from pygame import mixer
from pynotifier import Notification
#from pyttsx3 import Engine



# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 171)
engine.setProperty('volume', 150)

# Initialize speech recognizer
listener = sr.Recognizer()

# Initialize Pygame mixer for music playback
mixer.init()

# Load and play music
mixer.music.load("K:\\myjarvis\\jarvis\\jarvis-147563.mp3")
mixer.music.play()
mixer.music.set_volume(0.5)

# Speak and wait for speech recognition
engine.say("Hello, I am ready.")
engine.runAndWait()
sleep(4)  # Adjust timing as needed

# Example usage of speech recognition
try:
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)
        command = listener.recognize_google(audio)
        print(f"User said: {command}")

except Exception as e:
    print(f"Error: {e}")

# Example variable for reminders
reminders = "Nothing"

def sounds():
    mixer.music.load("K:\\myjarvis\\jarvis\\jarvis-intro-1.mp3")
    mixer.music.play()
    mixer.music.set_volume(0.2)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said : {query}")

    except:
        return ""

    query = str(query)
    return query.lower()

def mind_game():
    talk("yes sir, choose a number between 1-9")
    talk("got it?")
    talk("multiply your number by 9 sir")
    talk("have your time")
    talk(".")
    talk(".")
    talk("you got a two digit number sir?")
    talk("if you got ,  add the both number sir")
    talk("for example if you got 13, add 1 and 3 and made it 4")
    talk("done?")
    talk("minus 6 from your number sir")
    talk("now fix a alphabet to your number, like a for 1, b for 2, c for 3, d for 4, like that")
    talk("choose a country and a pet animal with your alphabet")
    talk("got it?")
    talk("now look at me")
    talk("the country u chosen is canada and cat as a pet and finally your number is 3")
    talk("how is it sir?")

def calc(my_string):
    print(my_string)

    def get_operator_fn(op):
        return {
            '+': operator.add,
            '-': operator.sub,
            'x': operator.mul,
            'divided': operator.__truediv__,
        }[op]

    def eval_binary_expr(op1, oper, op2):
        op1, op2 = int(op1), int(op2)
        return get_operator_fn(oper)(op1, op2)

    talk("Your result is")
    talk(eval_binary_expr(*(my_string.split())))

def notification(title, desc):
    Notification(
        title=title,
        description=desc,
        duration=5,
        urgency='normal'
    ).send()

def remind(remind0):
    global reminders
    reminders = remind0


def pearson(my_string):
    query = my_string
    sounds()
    talk("Scanning and analyzing user name in social media")
    talk("Check this out sir, I think this is enough to know about a person.")

    # Adjusted regex pattern to match social media and related URLs
    pattern = r"(instagram|facebook|youtube|twitter|github|linkedin|scholar|hackerrank|tiktok|maps)\.(com|edu|net|fandom)"

    # Perform web search and open relevant URLs
    for url in webbrowser.search(query, tld="co.in", num=15, stop=15, pause=2):
        if re.search(pattern, url):
            webbrowser.open(url)
            time.sleep(1)  # Optional: add a small delay before opening the next URL
        else:
            print(f"No match found for {url}")


def phnumber(my_string):
    # Print the input phone number
    print("Input Phone Number:", my_string)

    # Prepare the phone number with country code
    phonenum = "91" + my_string.replace(" ", "")

    # Construct the API URL with the access key and phone number
    url = f"http://apilayer.net/api/validate?access_key=cd3af5f7d1897dc1707c47d05c3759fd&number={phonenum}"

    try:
        # Make the API request
        resp = requests.get(url)

        # Check if request was successful
        if resp.status_code == 200:
            details = resp.json()

            # Use sounds() and talk() for auditory feedback
            sounds()
            talk("Collecting data")

            # Print and speak retrieved information
            print('')
            print("Country:", details.get('country_name', 'Not available'))
            talk("Country:" + details.get('country_name', 'Not available'))

            print("Location:", details.get('location', 'Not available'))
            talk("Location:" + details.get('location', 'Not available'))

            print("Carrier:", details.get('carrier', 'Not available'))
            talk("Carrier:" + details.get('carrier', 'Not available'))

        else:
            print(f"Error: Unable to retrieve data. Status code: {resp.status_code}")
            talk("Unable to retrieve data. Please try again later.")

    except Exception as e:
        print(f"Error: {e}")
        talk("An error occurred while fetching data. Please try again later.")


def mail():
    talk("to whom you want to send a mail sir")
    receiver = input("type the mail: ")
    talk("what message do you want to send sir ")
    message = take_command()
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("m.deepan621212@gmail.com", "evkr@2004")
    server.sendmail("m.deepan621212@gmail.com", "receiver", message)
    print("sending message to the" + receiver)
    sounds()
    talk("sending mail")
    talk("message sent")

def answer_finder(que):
    que1=que+"filetype:pdf"
    for i in search(que1, tld="co.in", num=5, stop=10, pause=2):
        if (re.search("pdf", i)):
            webbrowser.open(i)
        else:
            print("match not found")
def ppt_finder(que):
    que1=que+"filetype:ppt"
    for i in search(que1, tld="co.in", num=3, stop=3, pause=2):
        if (re.search("ppt", i)):
            webbrowser.open(i)
        else:
            print("match not found")



def ChromeAuto(command):
    sounds()
    query = command

    if 'new tab' in query:

        press_and_release('ctrl + t')

    elif 'close the tab' in query:

        press_and_release('ctrl + w')

    elif 'new window' in query:

        press_and_release('ctrl + n')

    elif 'history' in query:

        press_and_release('ctrl + h')

    elif 'download' in query:

        press_and_release('ctrl + j')

    elif 'bookmark' in query:

        press_and_release('ctrl + d')

        press('enter')

    elif 'incognito' in query:

        press_and_release('Ctrl + Shift + n')

    elif 'switch tab' in query:

        tab = query.replace("switch tab ", "")
        tab = tab.replace("to", "")
        tab = tab.replace("in chrome", "")

        num = int(tab)

        bb = f'ctrl + {num}'

        press_and_release(bb)

    elif 'open' in query:

        name = query.replace("open ", "")

        NameA = str(name)

        if 'youtube' in NameA:

            web.open("https://www.youtube.com/")

        elif 'instagram' in NameA:

            web.open("https://www.instagram.com/")

        elif 'whatsapp web' in NameA:

            web.open("https://web.whatsapp.com/")

        else:
            talk("i can get you sir")

def YouTubeAuto(command):
    sounds()
    query = str(command)
    if 'pause' in query:
        press('space bar')
    elif 'resume' in query:
        press('space bar')
    elif 'full screen' in query:
        press('f')
    elif 'film screen' in query:
        press('t')
    elif 'skip' in query:
        press('l')
    elif 'back' in query:
        press('j')
    elif 'previous' in query:
        press_and_release('SHIFT + p')
    elif 'next' in query:
        press_and_release('SHIFT + n')
    elif 'mute' in query:
        press('m')
    elif 'unmute' in query:
        press('m')
    else:
        talk("No Command Found!")


def WhatsappMsg(name, message):
    sounds()
    startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2422.7.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
    sleep(4)
    click(x=260, y=130)
    sleep(3)
    write(name)
    sleep(3)
    click(x=230, y=290)
    sleep(3)
    click(x=800, y=1050)
    sleep(3)
    write(message)

def WhatsappCall(name):
    sounds()
    talk("connecting")
    startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2424.6.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
    sleep(2)
    click(x=260, y=130)
    sleep(1)
    write(name)
    sleep(1)
    click(230, y=290)
    sleep(1)
    click(x=1730, y=90)

def WhatsappChat(name):
    startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2424.6.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
    sleep(10)
    click(x=260, y=130)
    sleep(1)
    write(name)
    sleep(1)
    click(230, y=290)
    sleep(1)
    click(x=1660, y=90)
    sleep(1)

def scan_image():
    talk("scaning and analysing the image")
    talk("wait a second sir")
    spinner = Halo(text=' Scanning', spinner='dots')
    image = ("K:\\myjarvis\\jarvis\\OIP.jpg")
    try:
        spinner.start()
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        url = 'http://www.google.co.in/searchbyimage/upload'
        secondurl = {'encoded_image': (image, open(image, 'rb')), 'image_content': ''}
        response = requests.post(url, files=secondurl, allow_redirects=False)
        fetch = response.headers['Location']

        req = requests.get(fetch, headers=headers)
        socialmedia = ["instagram", "facebook", "twitter", "linkedin", "github"]
        linklist = []
        print("[+] Scan started......")
        talk("Checking whether the image is associated in any social media ")
        print("Scanning started in Instagram")
        print("Scanning started in Github")
        print("Scanning started in Facebook")
        print("Scanning started in Twitter")
        print("Scanning started in Linkedin")
        talk('found some matching result')
        if (req.status_code == 200):
            soup = BeautifulSoup(req.content, 'html.parser')
            for g in soup.find_all('div', class_='g'):
                anchors = g.find_all('a')
                if 'href' in str(anchors[0]):
                    linklist.append(anchors[0]['href'])
            c = 0
            for i in socialmedia:
                sm = str(i)

                for j in linklist:
                    if sm in str(j):
                        c = c + 1
                        print("[+]" + j)

                        webbrowser.open(j)

            if c == 0:
                talk("No social Media links associated with this image")
        spinner.stop()
    except Exception as e:
        webbrowser.open(e)
        print(e)

def webscrap_translate(command):
    sounds()
    search = command
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find('div', class_="PME8Xe MUxGbd gbj1yb WZ8Tjf", id="lrtl-transliteration-text")
    print(temp.text)
    talk(temp.text)

def webscrap_search(command):
    sounds()
    search = command
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    notification("information", temp)
    talk(temp)

def intro():

    sounds()
    ampm = datetime.datetime.now().strftime('%p')
    hour = datetime.datetime.now().strftime('%I')
    hour = int(hour)
    if "AM" in ampm:
        talk("hello sir, good morning")
    elif "PM" in ampm and hour < 4:
        talk("hello sir, good afternoon ")
    elif "PM" in ampm and hour > 3:
        talk("hello sir, good evening")
    else:
        talk("good night")

    time = datetime.datetime.now().strftime('%I:%M %p')
    notification("Time", 'Current time is ' + time)
    talk('Current time is ' + time)

    talk("how can i help you sir")


intro()

def run_genesis():
    command = take_command().lower()
    print(command)

    if 'play' in command:
        talk("what song do you want to play sir")
        song = take_command()
        sounds()
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif "translate" in command:
        webscrap_translate(command)
    elif "wake up" in command:
        sbc.set_brightness(100)
        intro()
    elif 'time' in command:
        sleep(1)
        time = datetime.datetime.now().strftime('%I:%M %p')
        notification("Time", 'Current time is ' + time)
        talk('Current time is ' + time)
    elif 'your name' in command or "who are you" in command:
        sounds()
        talk('im jarvis and im a virtual artificial intelligence developed to assist with your task since best i can . ')
    elif "what is" in command:
        webscrap_search(command)
    elif "which is" in command:
        webscrap_search(command)

    elif 'who is' in command or "do you know about" in command:
        person = command.replace('who is', '').replace("do you know about", '')
        info = wikipedia.summary(person, 1)
        notification("information", info)
        talk(info)
    elif 'what can you do' in command:
        talk(
            'i can say the current time , weather , i can play songs from youtube , i can search anything on google or wikipedia , i do some maths, i can open apps for you, set a reminder, know about a person and many more')

    elif "i am back" in command:

        playsound("K:\\myjarvis\\jarvis\\jarvis-147563.mp3")

    elif 'good morning' in command:
        wishes = ["Wishing you a very Good Morning!  A new blessing, a new hope, a new light and a new day is waiting for you to conquer it.","A very Good Morning! I hope this morning brings a bright smile on your face. May you have a beautiful and rewarding day! Always keep smiling.","Life is a mystery and things always look impossible until it is made. Do not stop, move ahead and kill it. Good Morning, have a nice day!","Good Morning! It is a bright day. Wake up every morning with an assurance that you can do it. Think positive, stay happy and keep going"]
        talk(random.choice(wishes))

    elif 'good afternoon' in command:
        wishes = ["I wish you a lovely afternoon and a beautiful day.","Wishing for your afternoon to be wonderful, cozy, and happy. Have a great one, dear.","May this afternoon bring a lot of pleasant surprises for you and fills your heart with infinite joy. Wishing you a very warm and love-filled afternoon!","May your Good afternoon be light,blessed,enlightened,productive and happy."]
        talk(random.choice(wishes))

    elif 'good evening' in command:
        wishes = ["Good evening! I hope you had a good and productive day. Cheer up!","No matter how bad your day has been, the beauty of the setting sun will make everything serene. Good evening.","No matter how bad your day has been, the beauty of the setting sun will make everything serene. Good evening.","I am wishing you an amazing evening full of gossips and coffee. Just know that you are always in my mind. Enjoy this evening to the fullest!"]
        talk(random.choice(wishes))

    elif 'good night' in command:
        wishes = ["You have so many reasons to thank God, but first thank him for such a peaceful night like this. What a blissful night for a good sleep. Good night!","May you have sound sleep and wake up tomorrow with new hopes and a lot of positive energy. Good night to you!","Wishing you good night and rest well, dear friend. Stop worrying about life. I will always have your back no matter what.","May tomorrow be sunny and full of joy. Good night!"]
        talk(random.choice(wishes))

    elif 'open chrome' in command:
        sounds()
        talk('opening chrome for you sir')
        subprocess.call("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")


    elif 'office' in command:
        sounds()
        talk('opening office for you sir')
        print('opening office for you sir')
        subprocess.call("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk")

    elif 'search' in command:
        talk("what you want to search sir")
        my_string = take_command()
        sounds()
        talk('ok sir ill search that for you in google')
        print('oks ir ill search that for you in google')
        pywhatkit.search(my_string.replace('search', ''))

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif "reminder" in command:
        sounds()

        talk("what you want to remind sir")

        remind0 = take_command()

        talk("ok sir i remind that")

        remind(remind0)

    elif "remind me" in command:
        global reminders
        if reminders == "NOTHING":
            talk("You didn't say to remind")
        else:
            talk("yes sir you said to remind" + reminders)

    elif "can you calculate" in command:
        talk("what you want to calculate sir")
        my_string = take_command()
        calc(my_string)

    elif 'hello' in command:
        sounds()
        talk("hi sir, how was the day")

    elif 'sad' in command or 'bad' in command or 'nothing much' in command:
        wishes = ["i wish to have a arms to hug you and say, iam there for you","Please don’t be sad","A certain darkness is needed to see the stars.","Don’t let little stupid things break your happiness","Breathe. It’s only a bad day, not a bad life"]
        talk(random.choice(wishes))
        talk("can i play a song for you sir?")
        des = take_command()
        if "yes" in des:
            options = ["https://www.youtube.com/watch?v=403FGqa-Uv8","https://www.youtube.com/watch?v=pgN-vvVVxMA","https://www.youtube.com/watch?v=wnHW6o8WMas"]
            webbrowser.open_new(random.choice(options))
        else:
            talk("ok sir")

    elif 'happy' in command or 'good' in command:
        wishes = ["im so glad to hear from you sir, your smile make me happy too","im so glad to hear from you sir,Be happy for this moment. This moment is your life","im so glad to hear from you sir,The best way to pay for a lovely moment is to enjoy it","im so glad to hear from you sir,Sometimes your joy is the source of your smile, but sometimes your smile can be the source of your joy"]
        talk(random.choice(wishes))
        talk("can i play a song for you sir?")
        des = take_command()
        if "yes" in des:
            webbrowser.open_new("https://www.youtube.com/watch?v=tQ0yjYUFKAE")
        else:
            talk("ok sir")

    elif 'angry' in command:
        wishes = ["calm down sir, no matter how angry you get , you end up forgiving the people you love","calm down sir,The smarter you get, the more you realize anger is not worth it","Never waste a minute thinking about people you don’t like. Dwight D. Eisenhower"]
        talk(random.choice(wishes))

    elif 'sing' in command:
        talk('I see treeeees of greeeen. red roses tooooo, I watch them bloooom for me and you . And I think to '
             'myself. what a wonderful wooorld')

    elif 'classroom' in command:
        sounds()
        talk("opening google class room for you sir")
        webbrowser.open_new("https://classroom.google.com/h")

    elif 'work to do' in command or "to do" in command:
        sounds()
        talk("sir you have some assignments to do")
        talk("do i open it for you sir")
        des = take_command()
        if "yes" in des:
            webbrowser.open_new("https://classroom.google.com/a/not-turned-in/all")
        else:
            talk("ok sir")

    elif 'scan' in command or "image" in command:
        talk("okay sir")
        sounds()
        scan_image()

    elif 'discord' in command:
        sounds()
        talk("opening discord")
        web.open("https://discord.gg/cT8ZAqcg")

    elif 'google meet' in command:
        sounds()
        talk("opening google meet sir")

        webbrowser.open_new("https://meet.google.com/lookup/gzbdzqag3p?authuser=0&hs=179")

    elif 'check my whatsapp' in command or "whatsapp message" in command:
        sounds()
        talk("sir you have some messages can i open it for you")
        des = take_command()
        if "yes" in des:
            talk("opening whatsapp")
            startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2423.8.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
            sleep(5)
        else:
            talk("ok sir")

    elif 'instagram' in command:
        web.open("https://www.instagram.com/")

    elif 'in youtube' in command:
        talk("ok sir")
        YouTubeAuto(command)

    elif 'in chrome' in command:
        talk("ok sir")
        ChromeAuto(command)

    elif "close chrome" in command or "close the chrome" in command:
        sounds()
        talk("closing")
        os.system("taskkill /im chrome.exe /f")

    elif "who created you" in command:
        talk("im jarvis and virtual artificial intelligence developed by sir karthick to assist with some task which programmed by him ")

    elif ' gmail' in command:
        sounds()
        talk("opening gmail sir")
        webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")


    elif 'read my mind' in command:
        mind_game()

    elif 'awesome' in command:
        talk("thank you sir")

    elif 'thank you' in command or "thanks" in command:
        talk("its my pleasure sir")

    elif 'mail' in command:
        talk("ok sir ill do it for you")
        mail()

    elif "you doing" in command:
        response = ["I’m doing great (thanks). How about you?", "Doing good. You?", 'Doing pretty good. You?']
        talk(random.choice(response))

    elif 'how are you' in command:
        response = ["I’m good, thanks. You?","I’m pretty good. What’s new with you?","Never been better. What about you?"]
        talk(random.choice(response))

    elif 'i am fine' in command:
        talk("happy to hear that sir , how can i help you?")

    elif "wait a minute" in command or "minute" in command:
        talk("im always here to help you")

    elif 'trace' in command:
        talk("say the phone number sir ill trace for you")
        my_string = take_command()
        phnumber(my_string)

    elif 'want to know about' in command:
        talk("can i help you sir , whom you want to know about")
        my_string = take_command()
        pearson(my_string)

    elif "type" in command:
        talk("ok sir ill type for you, what you want to type sir")
        text = take_command()
        write(text)

    elif 'send a message to' in command:
        name = command.replace("send a message to ", "")
        talk("whats the message sir")
        message = take_command()
        WhatsappMsg(name, message)

    elif 'call to' in command:
        name = command.replace("make a call to ", "")
        talk("ok sir ill connect the call")
        WhatsappCall(name)

    elif 'connect a video with' in command:
        name = command.replace("connect a video with ", "")
        talk("ok sir ill connect the call")
        WhatsappChat(name)

    elif 'how much power left' in command or "how much power we have" in command or "battery" in command:
        battery = psutil.sensors_battery()
        per = battery.percent
        talk(f"sir your system have{per} percent battery")
        if per >= 75:
            talk("we have enough juice to continue our work")
        elif per>=40 and per<=75:
            talk("not yet full but its ok , we have enough power for couple of hours")
        elif per<=15 and per<=30:
            talk("we dont have enough power to manage. please connect your charger")
        elif per>15:
            talk("system in critical stage. please connect to charging or else the system will shutdown in few minutes")




    elif "hi" in command or "hay" in command:
        intro()

    elif "are you there" in command:
        talk("YEs sir, how can i help you")

    elif "wish me" in command:
        wishes = ["wish you happy life","wishing you all the best","im so proud of you","i wish you luck","You've worked hard for this, i believe in you "]
        talk(random.choice(wishes))
    elif "dice" in command:
        options = [1,2,3,4,5,6]
        talk(random.choice(options))

    elif "coin" in command:
        options = ["head","tail"]
        talk(random.choice(options))

    elif "notes" in command or "files" in command or "data" in command:
        talk("sure sir. i can do it for you. please say the title or topic sir ")
        que = take_command()
        talk("collecting data from the internet")
        answer_finder(que)
        talk("check this out sir")

    elif "ppt" in command or "presentations" in command:
        talk("sure sir. i can do it for you. please say the title or topic sir ")
        que = take_command()
        talk("collecting data from the internet")
        ppt_finder(que)
        talk("check this out sir")


    elif "worst" in command:
        talk("sorry sir, im doing my best")

    elif "your bad" in command:
        talk("Sorry sir , i will try to change")

    elif 'sleep' in command:
        talk("bye sir, have a good day")
        sys.exit()



    elif '' in command:
        print('still listening....')


    else:
        talk('sorry sir i did not get you.')
        print('sorry sir i did not get you.')

while True:
    run_genesis()


    exit_command = take_command()
    if exit_command and "exit" in exit_command:
        break

