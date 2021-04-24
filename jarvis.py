from twilio.rest import Client
import webbrowser     # Access Web portal through our code
import pyttsx3		 # Facilitate text to speech module
import speech_recognition as sr  # It is a speach recognition module as part of google Speech Api
import wikipedia	# Browse or surf anything on Wikipedia
import datetime		# Access System datetime
import os			# Lauch or Open System Folders and application
import random		# generate random numbers
import pyowm        #generating weather api
import pyautogui
import smtplib
from playsound import playsound
from plyer import notification
import ctypes
import psutil
from urllib.request import urlopen
import pyspeedtest
import requests
import pandas as pd 
from bs4 import BeautifulSoup as BS 
from tabulate import tabulate 
import numpy as np
import matplotlib.pyplot as plt 
import time
import cv2
import wave
import ctypes
import pyaudio
import sys
from mutagen.mp3 import MP3

from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 

from PyQt5.uic import loadUiType
from ui import Ui_MainWindow


a = datetime.datetime.now()
hour=int(a.strftime("%H"))
minute=int(a.strftime("%M"))

day= int(a.strftime("%d"))
month = int(a.strftime("%m"))
year = int(a.strftime("%Y"))


if day==26 and month==5 :
    notification.notify(title = "BIRTHDAY ALERT!!", message="it is Manashree's birthday, wish her to celebrate",app_icon="C:\\Users\\KIIT\\Downloads\\Google-Noto-Emoji-Food-Drink-32421-birthday-cake.ico", timeout = 5)
elif day==19 and month==7 :
    notification.notify(title = "BIRTHDAY ALERT!!", message="it is Haradhan's birthday, wish him to celebrate",app_icon="D:\\icons\\WhatsApp Image 2020-05-26 at 08.40.12 (2).ico", timeout = 5)
elif day==26 and month==1 :
    notification.notify(title = "BIRTHDAY ALERT!!", message="it is Moumita's birthday, wish her to celebrate",app_icon="D:\\icons\\moumita.ico", timeout = 5)
elif day==18 and month==3 :
    notification.notify(title = "BIRTHDAY ALERT!!", message="it is chandan's birthday, wish him to celebrate",app_icon="D:\\icons\\WhatsApp Image 2020-05-26 at 08.40.12 (1).ico", timeout = 5)
elif day==29 and month==8 :
    notification.notify(title = "BIRTHDAY ALERT!!", message="it is Babai's birthday, wish him to celebrate",app_icon="D:\\icons\\WhatsApp Image 2020-05-26 at 08.40.11.ico", timeout = 5)

    
else:
    notification.notify(title="NO BIRTHDAY TODAY AT THIS TIME!!", message="nobody is left to be wished today, check tomorrow", timeout= 5)


owm = pyowm.OWM('432bf8fe56c1cdb618a5cf45e8fbbe9b')
boston = owm.weather_at_place('Bhubaneswar, odisha, India')  ##forecasting weather
weather = boston.get_weather()

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
print(voices[1].id)  
engine.setProperty('voice',voices[1].id)     #set the audio of voice assistant as david
rate = engine.getProperty('rate')				# Go to Start Search for Microphone Setup
newrate = 130								# You will find  David as default voice
engine.setProperty('rate', newrate)			# We have encapsulated Hari with David's Voice
def speak(audio):
    engine.say(audio)						# Here is a function  to intake audio
    engine.runAndWait()
def wishMe():
    speak("Hello mister Prasun.")
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!! I am your JARVIS how can i help you?")					# This Function  is to greet the  Owner  as per System Time
    elif hour>=12 and hour<18:
        speak("Good Afternoon !!! I am your JARVIS how can i help you?")				# We can dyanamically modify as per requirements
    elif hour>=18 and hour<22:
        speak("Good Evening ! I am your JARVIS how can i help you?")
    else:
        speak(" It's beyond 10pm We must Sleep,now tell how can i help you after that you should sleep sir!")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()






    def takeCommand(self,ask = False):
        #It takes microphone input and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.non_speaking_duration = 0.6			# Actual Setup for Microphone based input
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print("User Said: "+r.recognize_google(audio))
            i = random.randrange(0,50)
            if i<25:								# Accepting voice and recognizing
                print("Copy that")
            else:
                print("Roger that")
        
        except Exception as e:
            #print(e)
            print("Sir I was unable to hear you Please Say again")   # if there occurs some exception It will ask to 
            speak("Sir I was unable to hear you Please Say again")		#Speak Again
            return "None"
            
        return query    
            
        
    def TaskExecution(self):
    
        
            wishMe()  # function has been called to greet the owner
            
            while True:    # Infinite  Loop  
                self.query = self.takeCommand().lower()    # Converting Voice commands to lower in order to 
                # logic for execution tasks based on query		# Relax for comparision
                if 'ok bro' or 'bro' in self.query:   			# Activation point
                    if 'wikipedia' in self.query:
                        speak("what wanna search for ?")
                        time.sleep(2)
                        speak('Searching Wikipedia...')  		# Surf to Wikipedia

                        res=wikipedia.summary('python',sentences=2)
                        speak("According to Wikipedia")    
                        print(res)
                        speak(res)

                    elif 'temperature' in self.query:
                        speak('the current temperature is')
                        
                        speak(weather.get_temperature('celsius')['temp'])
                        
                        speak('celcius')
                        
                    elif 'google search' in self.query: 
                        speak("what do you want to search on google?")                           ## search items on google
                        search = takeCommand("what do you want to search for?")
                        url = 'https://google.com/search?q=' + search
                        webbrowser.get().open(url)
                        speak(' here is what i found for ' + search)

                    elif 'search on youtube' in self.query: 
                        speak("what do you want to search?")                     ## search videos on youtube
                        search_term = takeCommand("what do you want to search for ?")
                        url = "https://www.youtube.com/results?search_query=" + search_term
                        webbrowser.get().open(url)
                        speak("wait a second . here is what i found for " + search_term + "on youtube")
                        speak("Enroll yourself for the top most score . You will learn everything and . you can make me better")

                    elif 'i need to learn' in self.query: 
                        speak("what do you want to learn ?")                                    ## search courses on udemy
                        search_term = takeCommand("what do you want to search for ?")
                        url = "https://www.udemy.com/courses/search/?src=ukw&q=" + search_term
                        webbrowser.get().open(url)
                        speak("wait a second . here is what i found for " + search_term + "course on udemy")
                        speak("Enroll yourself for the top most score . You will learn everything and . you can make me better")

                    elif 'find friends' in self.query:
                        speak("whom you want to search ??")                              ## search people on facebook by name 
                        search_term = takeCommand("what do you want to search for ?")
                        url = "https://www.facebook.com/search/top/?q=" + search_term
                        webbrowser.get().open(url)
                        speak("wait a second . here is what i found for " + search_term + "on facebook")
                    



                        
                    elif 'open youtube' in self.query:                            ## simply opening youtube home 
                        speak("Opening YouTube For You.")
                        webbrowser.open("https://www.youtube.com/")
                    #elif 'youtube' in query:                                #### opening several videos in youtube
                        #if 'python course' in query:
                            #speak("wait a second sir")
                            #webbrowser.open("https://www.youtube.com/results?search_query=python+course")
                        #elif 'machine learning' in query:
                            #speak("wait a second sir")
                            #webbrowser.open("https://www.youtube.com/results?search_query=ml+course")
                        #elif 'ethical hacking' in query:
                            #speak("wait a second sir")
                            #webbrowser.open("https://www.youtube.com/results?search_query=eyhical+hacking")
                        #elif 'bong guy' in query:
                            #speak("wait a second sir")
                            #webbrowser.open("https://www.youtube.com/channel/UCh5bICCatQ70Fx4-jwAmWKQ")
                        #elif 'carryminati' in query:
                            #speak("wait a second sir")
                            #webbrowser.open("https://www.youtube.com/user/AddictedA1")
                        #elif 'entertainment' in query:
                            #speak("wait a second sir")
                            #webbrowser.open("https://www.youtube.com/results?search_query=entertaining+videos")
                    

                        
                    elif 'check messenger' in self.query:              ## opening facebook home page
                        speak("Here all caught up sir.")
                        webbrowser.open("https://www.facebook.com/messages/t/100000845154756")
                    
                    
                    
                    elif 'check my inbox' in self.query:                  ## taking to inbox
                        speak("yupp let me take you to your inbox")
                        webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
                    
                    elif 'open my inbox' in self.query:                    ## opening mail id
                        speak("yupp let me take you to your inbox")
                        webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
                    
                    elif 'google' in self.query:            					# Browse to google Services
                        if 'maps' in self.query:
                            speak("Opening Google Maps For you.")
                            webbrowser.open("https://www.google.co.in/maps/")
                        elif 'drive' in self.query:
                            speak("Opening Google Drive for you.")
                            webbrowser.open("https://drive.google.com/drive/")
                        elif 'translate' in self.query:
                            speak("Opening Google translate for you.")
                            webbrowser.open("https://translate.google.co.in/")
                        else:
                            speak("Opening Google for you.")
                            webbrowser.open("https://www.google.co.in/") 
                    
                    elif 'find location' in self.query:                       ## finding a location
                        speak("what's the name of place??")
                        search_term = takeCommand("what do you want to search for ?")
                        url = "https://www.google.co.in/maps/place/" + search_term
                        webbrowser.get().open(url)
                        speak("wait a second . here is what i found for " + search_term + "on maps")

                    elif 'search live train status' in self.query:
                        speak("what is the train number you are looking for?")
                        print("what is the train number you are looking for?")
                        search_term = takeCommand("what do you want to search?")
                        url = "https://www.railyatri.in/live-train-status/"+ search_term
                        webbrowser.get().open(url)
                        speak("wait a second. here the train what i found for " + search_term)
                    
                    
                    
                    
                    
                                    
                    elif 'parents' in self.query:
                        speak("wait sir. I am searching for you")
                        kirtan_dir = "D:\\maa baba"
                        kirtans = os.listdir(kirtan_dir)							# show maa baba
                        os.startfile(os.path.join(kirtan_dir, kirtans[random.randrange(0,2)]))
                        speak("Prasun here is your parents in front of you , your dad is Tapas kumar Chakraborty , an police sub-inspector of west Bengal and the other one is your Mother , Dipty Chakraborty , a housewife, both of them are indian, they love you most...don't let them go .  ")

                    

                    elif 'set timer' in self.query:
                        def countdown(t):
                                while t > 0:
                                    print(t)
                                    t -= 1
                                    time.sleep(1)
                                print("time up")
                                speak("time up")
                                #playsound("C:\\Users\\KIIT\\Downloads\\fantasy-alarm-clock.mp3")
                        print("How many seconds to count down? Enter an integer:")
                        speak("How many seconds to count down?")
                        seconds = self.takeCommand("seconds")
                        speak("starting timer for")
                        speak(seconds)
                        speak("seconds")
                        while not seconds.isdigit():
                                    print("That wasn't an integer! Enter an integer:")
                                    seconds = takeCommand("seconds")
                        seconds = int(seconds)
                        countdown(seconds)
                                
                    elif 'news update' in self.query:
                        
                            # BBC news api 
                            main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=2de354f9f7364984916b779a4aad535d"
        
            # fetching data in json format 
                            open_bbc_page = requests.get(main_url).json() 
        
            # getting all articles in a string article 
                            article = open_bbc_page["articles"] 
                            results = [] 
                            for ar in article:
                                results.append(ar["title"])  
                            
                
                
                            for i in range(len(results)): 
                                print(i + 1, results[i]) 
                            
                            speak(results)
                
                        
                    elif 'corona update' in self.query:           ## world corona update
                        def get_info(url):
                            # getting the request from url  
                            data = requests.get(url)
                            soup = BS(data.text, 'html.parser')
                            total = soup.find("div", class_ = "maincounter-number").text
                            total = total[1 : len(total) - 2]
                            other = soup.find_all("span", class_ = "number-table")
                            recovered = other[2].text
                            deaths = other[3].text
                            deaths = deaths[1:]
                            ans ={'Total Cases' : total, 'Recovered Cases' : recovered,  
                                        'Total Deaths' : deaths}
                            return ans
                            
                        url = "https://www.worldometers.info/coronavirus/"
                        ans = get_info(url)
                        for i, j in ans.items():
                            speak(i + " : " + j)
            

                    
                            
                        
                    elif 'take selfie' in self.query:              ## taking pictures 
                        image=cv2.VideoCapture(0)

                        check,frame = image.read()
                        cv2.imshow("selfie",frame)
                        cv2.imwrite("selfie.jpg",frame)
                        speak("your photo has been clicked !! you can check this file in your python folder in d drive")
                        cv2.waitKey()
                        image.release()
                        cv2.destroyAllWindows()

                    
                    elif 'play music' in self.query:
                        kirtan_dir = "C:\\Users\\KIIT\\Music\\NIRMALA MISHRA"
                        kirtans = os.listdir(kirtan_dir)							# Play music  for refreshment
                        speak("Playing Music for You as refreshment")
                        os.startfile(os.path.join(kirtan_dir, kirtans[random.randrange(0,14)]))
                        continue

                    elif 'energetic' in self.query:
                        audio = MP3("C:\\Users\\KIIT\\Music\\01) Challenge Nibi Na Shala.mp3")
                        speak("Here is your most favourite music")
                        path="C:\\Users\\KIIT\\Music\\01) Challenge Nibi Na Shala.mp3"
                        os.startfile(path)
                        #time.sleep(audio.info.length)
                        continue
                    elif 'close' in self.query:
                        pyautogui.click(1900,35)

                    elif 'thank you' in self.query:
                        speak("You are Most Welcome sir . It's my Honor to help you.")            # Thank You          	   
                    
                    elif 'what is the time' in self.query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"The time is  {strTime}")

                    elif 'who are you' in self.query:
                        speak("I am jarvis sir. Your personal voice assistant to automate few tasks.")
                    
                    elif 'sleep' in self.query:
                        speak("No sir. I am always at your service. Call me when needed")

                    elif 'wake up' in self.query:
                        speak("yes sir I am here. Tell me what to do ?")

                    elif 'born' in self.query:
                        speak("one day Prasun was looking for learning something new. He was working on a Artificial Intelligence project.")
                        time.sleep(1)
                        speak("as far as I know he is a big fan of Iron man. So he just started working upon me to make his personal AI assistant like jarvis!")
                        time.sleep(1)
                        speak('Finally he did that and I can do certain programs as per my dads instruction. Prasun is my dad...Thank you')

                    elif 'send mail' in self.query:
                        speak("wait a moment sir. I am sending mails")
                        time.sleep(5)
                        speak("System generated mails have been sent to all the listed mail ids")

                    elif 'open sublime text' in self.query:
                        speak("openning sublime text for you!")
                        path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"  #  Another Example
                        os.startfile(path)

                    elif 'check my battery' in self.query:             ## checks the battery level
                       
                        speak("Your battery level is")
                        speak(psutil.sensors_battery().percent)
                        speak("percentage. No need to charge now")
                        

                    elif 'check the connection' in self.query:
                        speak("wait sir i'm checking...")
                        
                        print("checking...")
                        def status():
                            try:
                                urlopen('https://www.youtube.com/',timeout=1)
                                notification.notify(title="CONNECTION STATUS",message="You are connected to internet",app_icon="D:\\icons\\img_5bb560676100c.ico",timeout=5)
                                speak("you are connected to internet")
                                
                            except:
                                notification.notify(title="CONNECTION STATUS",message="You are not connected to internet",app_icon="D:\\icons\\5593_-_No_Wifi-512.ico",timeout=5)
                                speak("you are no connecteed to internet")
                                
                        status()
                    
                    elif 'check internet speed' in self.query:                          ## check internet speed
                        speed = pyspeedtest.SpeedTest("www.google.com")
                        print("what do you want to know : ping speed or download speed ?")
                        speak("what do you want to know : ping speed or download speed ?")
                        
                        speed1 = takeCommand()
                        if speed1=='pink speed':
                            print("your ping speed is :", speed.ping(),"ms")
                            speak("your ping speed is :") 
                            
                            speak(speed.ping())
                            
                            speak("ms")
                            
                        elif speed1=='download speed':
                            print("your download speed is:", speed.download(),"mbps")
                            speak("your download speed is:")
                            
                            speak(speed.download())
                            
                            speak("mbps")
                            
                        else:
                            speak("invalid query sir..")
                            
                            print("invalid option.")

                    elif 'last night' in self.query:
                        speak("Yes Prasun. You were teaching python to someone.")

                    elif 'open the file' in self.query:
                        speak("Opening sir")
                        path="C:\\Users\\KIIT\\Downloads\\time_series_covid_19_confirmed.xlsx"
                        os.system(path)
                        continue
                    elif 'ok' in self.query:
                        speak("yes do it faster . otherwise i will tel your girlfriend")
                    elif 'any' in self.query:
                        speak("oops ! that's unfortunate. No worries , here I am with you !")
                    elif 'hope' in self.query:
                        speak("Sure Prasun")

                    
                    elif 'alexa' in self.query:
                        speak("Yes, she is my senior person ! Amazon developed her.")
                    elif 'you may go now' in self.query:
                        speak("Okay Prasun ! I am going to sleep . Please call me when needed")
                        time.sleep(1)
                        speak("Bye Bye, have a good day!")
                        break

startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie=QtGui.QMovie("C:\\Users\\KIIT\\Desktop\\JarvisUI\\sFaoXq3.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("C:\\Users\\KIIT\\Desktop\\JarvisUI\\iron-man-jarvis-gif-5.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start() 

        self.ui.movie=QtGui.QMovie("C:\\Users\\KIIT\\Desktop\\JarvisUI\\BigheartedVagueFoal-size_restricted.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("C:\\Users\\KIIT\\Desktop\\JarvisUI\\hey.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()   

        self.ui.movie=QtGui.QMovie("C:\\Users\\KIIT\\Desktop\\JarvisUI\\jarvislogo.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("C:\\Users\\KIIT\\Desktop\\JarvisUI\\iron-man-jarvis-gif-5.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start() 
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time=QTime.currentTime()
        lable_time=current_time.toString("hh:mm:ss")
        self.ui.textBrowser.setText(lable_time)

app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())


                


            
             
           

         
            

    
        
        


        
            
