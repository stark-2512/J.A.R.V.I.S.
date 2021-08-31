from PIL.ImageOps import grayscale
import pyttsx3
from datetime import *
from pywhatkit.main import playonyt, search
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
import pyjokes 
import pyautogui
import requests
import socket
import geopy
import time
from bs4 import BeautifulSoup
from pywikihow import *
import psutil
import speedtest

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',190)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.now().hour)
    
    if(hour>=0 and hour<=12):
        speak("Good Morning Sir")
    elif(hour>12 and hour<=15):
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

def takeCommand():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)
        
    try:
       print("Recognizing...")
       query=r.recognize_google(audio,language='en-in')
       print("Arjun : ",query)
    except Exception as e:
        #print(e)
        print("Say That Again Sir...")
        return "none"  
    return query

def msg():
        num="+919166812091"
        speak("sir whom do you want to send the message")
        msg_to=takeCommand().lower()
        if(msg_to == "mummy"):
            num="#"
        elif(msg_to == "papa"):
            num="#"   
        elif(msg_to == "nana ji" or msg_to == "nanaji"):
            num="#"
        elif(msg_to == "tisha"):
            num="#"
        elif(msg_to == "vanshika"):
            num="#"
        elif(msg_to=="tanya"):
            num="#"
        elif(msg_to == "nitesh"):
            num="#"
        elif(msg_to == "utkarsh"):
            num="#"
        elif(msg_to == "ayush"):
            num="#"
        elif(msg_to == "shrusti"):
            num="#"
        elif(msg_to == "myself"):
            num="#"
        else:
            speak("sir please repeat that again")
            return msg()

        return num

def task():
    wishme()
    while True:

        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'what are you doing' in query:
            speak("sir waiting for your orders")

        elif 'open google' in query:
            speak("sir what should i search on google")
            cm=takeCommand().lower()
            kit.search(cm)

        elif 'check message' in query:
            webbrowser.open("https://web.whatsapp.com/")   


        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open classroom' in query:
            webbrowser.open("https://classroom.google.com/u/0/h")

        elif 'whatsapp' in query:
                speak("sir personal or group")
                type=takeCommand().lower()
                if 'personal' in type:
                    num=msg()
                    speak("sir please tell the message")
                    msg_text=takeCommand().lower()
                    kit.sendwhatmsg_instantly(num,msg_text,7)
                elif 'group' in type:
                    speak("sir please tell the message")
                    msg_text=takeCommand().lower()
                    #h=datetime.now().hour()
                    #m=datetime.now().minute()
                    
                    kit.sendwhatmsg_to_group(group_id="#",message=msg_text,time_hour=22,time_min=55)
        elif 'play on youtube' in query:
            speak("What do you want to watch")
            play=takeCommand().lower()
            playonyt(play)
        
       
        elif 'rest' in query:
            speak("roger that sir")
            speak("Sir i am here you can call me any time")
            break
           
        elif 'are you there' in query:
            speak("yes sir i am here")
        
        elif 'tell me a joke' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)
        
        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")    

        elif 'where are we' in query or 'where i am' in query:
            try:
                res = requests.get('https://ipinfo.io/')
                data = res.json()
                city = data['city']
                country=data['country']
                print(city+" "+country)
                speak(city)
                speak(country)

               
                #ipAdd=requests.get("https://api.ipify.org").text
                #print(ipAdd)
                #url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                #geo_requests=requests.get(url)
                #geo_data=geo_requests.json()

                #city=geo_data['city']
                #state=geo_data['region']
                #country=geo_data['country']
                #speak(f"sir we are in the city {city} state {state} in country {country}")
            except Exception as e:
                speak("Sorry sir due to network issue i am not able to find that")

        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak("Sir please tell the name of the file")
            name=takeCommand().lower()
            speak("Sir please hold the screen for a sec I am taking screenshot")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Done Sir")

        elif 'shut down the system' in query:
            speak("Powering off , Bye Bye Sir")
            os.system("shutdown /s /t 5")
        
        elif 'restart the system' in query:
            speak("Restarting the system , Meet you soon Sir")
            os.system("shutdown /r /t 5")
        
        elif 'system sleep' in query:
            speak("System Going to Sleep")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            exit()
        
        elif 'file security' in query:
            speak("Sir do you wanna hide or make it visible")
            action=takeCommand().lower()
            if 'hide' in action:
                os.system("attrib +h /s /d")
                speak("all the files are hidden sir")

            elif 'visible' in action:
                os.system("attrib -h /s /d")
                speak("all the files are visible sir")
            
            elif 'leave it' in action:
                speak("Ok sir")
        
        elif 'good bye' in permission or 'goodbye' in query:
            speak("roger that sir")
            speak("Have a good day sir")
            exit()
        
        elif 'connect class' in query:
            speak("which Class Sir")
            sub= takeCommand().lower()
            
            if 'english' in sub:
                
                webbrowser.open("https://bit.ly/3wyUyHT")
                time.sleep(3.00)
                audio_off=pyautogui.locateCenterOnScreen("audio_off.png",grayscale="false")
                print(audio_off)
                pyautogui.click(audio_off)
                time.sleep(3.00)
                speak("sir we are ready to join")
                
                j=1
                while(j==1):
                    confirm=takeCommand().lower()
                    if 'join' in confirm:
                        speak("joining sir")
                        j=0
                        join=pyautogui.locateCenterOnScreen("join.png",grayscale="false")
                        print(join)
                        pyautogui.click(join)
                    else:
                        speak("Waiting for your confirmation")
                        j=1
                         
            elif 'manufacturing' in sub:
                
                webbrowser.open("https://bit.ly/3xr5J6C")
                time.sleep(3.00)
                audio_off=pyautogui.locateCenterOnScreen("audio_off.png",grayscale="false")
                print(audio_off)
                pyautogui.click(audio_off)
                time.sleep(3.00)
                speak("sir we are ready to join")
                
                j=1
                while(j==1):
                    confirm=takeCommand().lower()
                    if 'join' in confirm:
                        speak("joining sir")
                        j=0
                        join=pyautogui.locateCenterOnScreen("join.png",grayscale="false")
                        print(join)
                        pyautogui.click(join)
                    else:
                        speak("Waiting for your confirmation")
                        j=1

            elif 'physics' in sub:
                
                webbrowser.open("https://bit.ly/2SUogsR")
                time.sleep(7.00)
                audio_off=pyautogui.locateCenterOnScreen("audio_off.png",grayscale="false")
                print(audio_off)
                pyautogui.click(audio_off)
                time.sleep(3.00)
                speak("sir we are ready to join")
                
                j=1
                while(j==1):
                    confirm=takeCommand().lower()
                    if 'join' in confirm:
                        speak("joining sir")
                        j=0
                        join=pyautogui.locateCenterOnScreen("join.png",grayscale="false")
                        print(join)
                        pyautogui.click(join)
                    else:
                        speak("Waiting for your confirmation")
                        j=1

            elif 'chemistry' in sub:
                
                webbrowser.open("https://bit.ly/3xzCf6I")
                time.sleep(3.00)
                audio_off=pyautogui.locateCenterOnScreen("audio_off.png",grayscale="false")
                print(audio_off)
                pyautogui.click(audio_off)
                time.sleep(3.00)
                speak("sir we are ready to join")
                
                j=1
                while(j==1):
                    confirm=takeCommand().lower()
                    if 'join' in confirm:
                        speak("joining sir")
                        j=0
                        join=pyautogui.locateCenterOnScreen("join.png",grayscale="false")
                        print(join)
                        pyautogui.click(join)
                    else:
                        speak("Waiting for your confirmation")
                        j=1

        elif 'exit class' in query:
            speak("leaving the class sir")
            pyautogui.hotkey('ctrl','shift','b')
            
        elif 'weather' in query:
            speak("checking the temperature sir")
            s='temperature in alwar'
            url=f"https://www.google.com/search?q={s}"
            r=requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {s} is {temp}")
        
        elif 'tell me how to do this' in query:
            speak("yes sir tell me what should i search")
            what=takeCommand().lower()
            max_result=1
            how_to=search_wikihow(what,max_result)  #this returns a list
            assert len(how_to)==1
            how_to[0].print()
            speak(how_to[0].summary) 
        
        elif 'power we have' in query or 'battery' in query:
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speak(f"Sir we have {percentage} percent battery left")
            print(f"Sir we have {percentage} percent battery left")
            if percentage>=65:
                speak("sir we have enough battery we can continue our work")
            elif percentage<=65 and percentage>=40:
                speak("sir i think we should connect to the charging")
            elif percentage<=40 and percentage>=20:
                speak("sir we don't have enough power to work we should connect power to the system")
            elif percentage<20 and percentage>=10:
                speak("Sir we are very low on power connect battery or I will shut down the system")
            elif percentage<10:
                speak("sorry sir we can't continue now , i am turning off the system in 5 ,4 ,3 ,2 ,1 Bye Sir !!!")
                os.system("shutdown /s /t 5")
        
        elif 'internet speed' in query:
            speak("Testing sir wait for a second")
            st=speedtest.Speedtest()
            dl=int((st.download())/8000000)
            up=int((st.upload())/8000000)
            print(f"sir our downloading speed is {dl} MB second and upload speed is {up} MB per second")
            speak(f"sir our downloading speed is {dl} MB second and upload speed is {up} MB per second")
            
        elif 'control volume' in query:
            speak("sir do you wanna increase or decrease the volume or mute system")
            command=takeCommand().lower()
            if 'increase' in command:
                speak("how many times")
                vol=int(takeCommand().lower())       
                for i in range (1,vol):
                    pyautogui.press("volumeup")
            elif 'decrease' in command:
                speak("sir by how many")
                vol=int(takeCommand().lower())       
                for i in range (1,vol):
                    pyautogui.press("volumedown")
            if 'mute' in command:
                speak("sir system muted")
                pyautogui.press("volumemute")

        elif 'volume up' in query:
            pyautogui.press("volumeup")
        
        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")
        
        
        else:
            pass
        
if __name__ == '__main__':
    while True:
        permission=takeCommand().lower()
        if 'wake up' in permission or 'wakeup' in permission:
            task()
        elif 'good bye' in permission or 'goodbye' in permission:
            speak("roger that sir")
            speak("Have a good day sir")
            exit()
        
