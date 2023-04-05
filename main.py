import datetime
import json
import os  # (for module of operatng system)
import webbrowser
import webbrowser as wb  # (for webbrowser)
from urllib.request import urlopen
import psutil  # pip install pustil(for cpu utlization)
import pyautogui  # pip install pyautogui (For Screenshot)
import pyjokes  # pip install pyjokes(for jokes)
import pyttsx3  # pip install pyttsx3 (For Speak)
import pywhatkit  # open youtube
import requests
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia
from requests import get

# required python 3.8
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def search_in_chrome_():
    speak('What should i search?')
    chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    # chromepath is the location of chrome path in computer

    search = TakeCommand().lower()
    wb.get(chromepath).open_new_tab(str(search) + '.com')  # only open website with '.com' at end.


def youtube_():
    speak("what should i search")
    search_term = TakeCommand().lower()
    speak("Here we go to youtube")
    # wb.open('https://www.youtube.com/results?search_query=' + search_term)
    pywhatkit.playonyt(str(search_term))
    # pywhatkit.playonyt("tu pyar hai kisi aur ka")


def google_():
    speak("what should i search")
    search_term = TakeCommand().lower()
    speak("searching in google......")
    wb.open('https://www.google.com/search?q=' + search_term)


def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S %p")
    print("The current time is the boss")
    speak("The current time is the boss")
    print(Time)
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    print("The current date is the boss")
    speak("The current date is the boss")
    print(f"the date is {date}/{month}/{year}")

    speak(date)
    speak(month)
    speak(year)


def introduction_():
    speak("""Good morning sir First of all, thanks for giving me this opportunity to  introduce myself. 
My name is Dhiraj Kumar.
 I am basically from Mashrakh Bihar but 
currently, I am staying in Bhopal. 
I have completed my intermediate from SDS college Chapra and 
currently, I am pursuing B.tech in computer science from 
Ies college of technology Bhopal. 
I have three members in my family. 
My father's name is late Santosh Singh 
and my mother's name is Gita Devi and she is a housewife and 
my younger brother is pursuing his b.tech from Patel College Bhopal. 
Now coming to my technical skills are I have knowledge of c and c++. and 
during the last year of my college 
I made a project along with my teammates and 
the name of my project is voice assistant using python and 
there are three members in my group and I am leading that 
group. My hobby are playing video games and 
learning new things. I am seeking an opportunity 
where I can utilize my potential and skills for the 
growth of the organization. I am a keen learner who 
loved to work in a team""")


def creator_():
    print("My name is sara and i am created by Dhiraj kumar,Aman kumar and Anam ali and my current version is 1.0")
    speak("My name is sara and i am created by Dhiraj kumar,Aman kumar and Anam ali and my current version is 1.0")


def ip_address_():
    ip = get('https://api.ipify.org').text
    print(f"your IP adress is {ip}")
    speak(f"your IP adress is {ip}")


def college_():
    print("The college name is IES college of technology bhopal")
    speak("The college name is IES college of technology bhopal")


def about_project_():  # about project
    print("""My name is sara and
i am created by Dhiraj kumar ,aman kumar and anam ali and
i am voice assistant and 
i developed in python and 
i work on the command whatever given by the user""")
    speak("""My name is sara and 
i am created by Dhiraj kumar,Aman kumar and Anam ali and
i am voice assistant and
i developed in python and 
i work on the command whatever given by the user""")


def love_():
    print(" yes i love you forever and i am always with you")
    speak(" yes i love you forever and i am always with you")


def relationship_():
    print("sorry i am already relationship with internet")
    speak("sorry i am already relationship with internet")


def cpu():
    usage = str(psutil.cpu_percent())
    print('CPU is at' + usage)
    speak('CPU is at' + usage)

    battery = psutil.sensors_battery()
    print('battery is at')
    print(battery.percent)
    speak('battery is at')
    speak(battery.percent)
    speak('percent')


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/dhira/Pictures/screenshot.png")


def joke():
    speak(pyjokes.get_joke())


def offline_():
    speak('have a good day and i am going to offline bose')
    quit()


def news():
    try:

        jsonObj = urlopen(
            "https://newsapi.org/v2/top-headlines?country=in&apiKey=×××××××××××××××")
        data = json.load(jsonObj)
        i = 1

        speak('here are some top news from the times of india')
        print('''=============== TOP HEADLINES ============''' + '\n')

        for item in data['articles']:

            print(str(i) + '. ' + item['title'] + '\n')
            print(item['description'] + '\n')
            speak(str(i) + '. ' + item['title'] + '\n')
            i += 1
            if i == 6:
                break

    except Exception as e:
        print(str(e))


def weather():
    api = "xxxxxxxxxxxxxx"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    print("for which city?")
    CITY = TakeCommand().lower()
    # CITY = input("city?: ")
    URL = BASE_URL + "q=" + CITY + "&units=imperial" + "&appid=" + api

    response = requests.get(URL)

    data = response.json()
    main = data['main']
    temperature = main['temp']
    humidity = main['humidity']
    pressure = main['pressure']
    report = data['weather']
    print(f"{CITY:-^30}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")
    speak(f"{CITY:-^30}")
    speak(f"Temperature: {temperature}")
    speak(f"Humidity: {humidity}")
    speak(f"Pressure: {pressure}")
    speak(f"Weather Report: {report[0]['description']}")


def write_a_note_():
    speak("What should i write bose? ")
    notes = TakeCommand()
    file = open('notes.txt', 'w')
    speak("bose should i include date and time?")
    ans = TakeCommand()
    if 'yes' in ans or 'sure' in ans:
        strTime = datetime.datetime.now().strftime("%H %M %S")
        file.write(strTime)
        file.write(':-')
        file.write(notes)
        speak('done taking notes, boss')
    else:
        file.write(notes)


def note_():
    speak("showing notes boss")
    file = open('notes.txt', 'r')
    print(file.read())
    speak(file.read())


def wishes():
    print("Welcome boss My name is Sara")
    speak("Welcome boss My name is Sara")
    # time_()
    # `date_()

    # greeting
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning boss How may i help you")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon boss How may i help you")
    elif hour >= 18 and hour < 24:
        speak("Good evening boss How may i help you")
    else:
        speak("Good night boss How may i help you")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.adjust_for_ambient_noise(source)
        # r.pause_threshold = 1
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please.....")
        # speak("Say that again please...")
        return "none"
    return query


if __name__ == "__main__":
    # clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    # clear()

    wishes()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()

        elif 'search in chrome' in query:
            search_in_chrome_()
        elif 'youtube' in query:
            youtube_()
        elif 'google' in query:
            google_()
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            joke()
        elif 'offline' in query:
            offline_()
        elif 'screenshot' in query:
            screenshot()
        elif 'write a note' in query:
            write_a_note_()
        elif 'note' in query:
            note_()
        elif 'introduction' in query:
            introduction_()
        elif 'project' in query:
            about_project_()
        elif 'love' in query:
            love_()
        elif 'relationship' in query:
            relationship_()
        elif "locate" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + " ")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'creator' in query:
            creator_()

        elif 'college' in query:
            college_()

        elif "command prompt" in query:
            os.system("start cmd")
        elif "ip address" in query:
            ip_address_()
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif "stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")
        elif "facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "twitter" in query:
            webbrowser.open("www.twitter.com")
        elif "weather" in query:
            weather()
        elif 'news' in query:
            news()

TakeCommand()
