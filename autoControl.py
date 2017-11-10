import pyautogui as gui
import speech_recognition as sr
import time
import pyttsx
import json
def changeLanguage():
    gui.keyDown("alt")
    gui.keyDown("shift")
    gui.keyUp("alt")
    gui.keyUp("shift")
def browse(url):
    width,height = gui.size()
    UrlLine = (180,49)
    gui.moveTo(0,height-1)
    gui.click()
    time.sleep(0.1)
    gui.typewrite("Chrome")
    time.sleep(1)
    gui.click()
    gui.moveTo(UrlLine)
    time.sleep(0.2)
    gui.click()
    gui.doubleClick()
    gui.typewrite("https://mail.google.com")
    gui.typewrite(["enter"])
engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2])
'''engine.say("sheli is our great and only leader and a true goddess")
engine.runAndWait()
time.sleep(0.7)
engine.say("sheli is a divine creature with divine appearence")
engine.runAndWait()'''
'''browse("www.one.co.il")#for now, address doesn't work
time.sleep(7.5)
engine.say("who do you want to mail")
engine.runAndWait()
r = sr.Recognizer()
with sr.Microphone() as src:
    audio = r.listen(src)
try:
    contact= r.recognize_google(audio)
except:
    engine.say("can you type that")
    engine.runAndWait()
    contact = raw_input()
file = open("contacts.json","r+")
st = file.read()
js = json.loads(st)
file.close()
if (not(contact.lower() in js.keys())):
    mail = raw_input("enter email manually")
else:
    mail = js[contact]'''
for i in range(0,30):
    gui.moveTo(92,225)
    gui.click()
    time.sleep(0.2)
    gui.moveTo(865,270)
    gui.click()
    gui.typewrite("ron200011@gmail.com")
    time.sleep(0.05)
    #gui.typewrite(["tab"])
    gui.click(865,315)
    gui.click(865,315)    
    #changeLanguage()
    gui.typewrite("hello"+str(i+1))
    time.sleep(0.05)
    gui.typewrite(["tab"])
    gui.click(865,345)
    gui.typewrite("hello")
    gui.typewrite(["enter"])
    gui.typewrite("(shut up)")
    gui.moveTo(865,665)
    gui.click()
    time.sleep(0.5)
    #changeLanguage()
'''gui.moveTo(145,180)
gui.click()
time.sleep(0.1)
gui.typewrite("rui pv")
time.sleep(0.1)
gui.moveTo(106,302)
for i in range(1,10):
    gui.click()
    time.sleep(0.3)
    gui.moveTo(520,696)
    gui.click()
    gui.typewrite("fprv")'''
'''printLocation = [500,685]
time.sleep(5)
gui.moveTo(89,256)
gui.click()
time.sleep(1)
gui.moveTo(printLocation)  
gui.click()
gui.typewrite("Yotam is not so good as he thinks")
gui.typewrite(["enter"])'''
'''gui.click(520,685)
time.sleep(1)
for i in range(1000):
    gui.typewrite("kapara")
    gui.typewrite(["enter"])
    time.sleep(0.05)'''