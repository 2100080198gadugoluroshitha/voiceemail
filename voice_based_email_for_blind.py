import speech_recognition as sr
import smtplib
import pyaudio
# import platform
# import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
tts = gTTS(text="Project: Voice based Email for blind", lang='en')
ttsname=("name.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
login = os.getlogin
print ("You are logging from : "+login())
print ("1. composed a mail.")
tts = gTTS(text="option 1. composed a mail.", lang='en')
ttsname=("hello.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
print ("2. Check your inbox")
tts = gTTS(text="option 2. Check your inbox", lang='en')
ttsname=("second.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
tts = gTTS(text="Your choice ", lang='en')
ttsname=("hello.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Your choice:")
    audio=r.listen(source)
    print ("ok done!!")
try:
    text=r.recognize_google(audio)
    print ("You said : "+text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
     
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
if text == 'composed a mail' or text == 'Composed a mail' or text == 'one':
    r = sr.Recognizer() #recognize
    with sr.Microphone() as source:
        print ("Your message :")
        audio=r.listen(source)
        print ("ok done!!")
    try:
        text1=r.recognize_google(audio)
        print ("You said : "+text1)
        msg = text1
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))    

    mail = smtplib.SMTP('smtp.gmail.com',587)    
    mail.ehlo() 
    mail.starttls() 
    mail.login('emailID','pswrd') 
    mail.sendmail('emailID','victimID',msg)
    print ("Congrates! Your mail has send. ")
    tts = gTTS(text="Congrates! Your mail has send. ", lang='en')
    ttsname=("send.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()   
    
if text == 'Check your inbox' or text == 'check your inbox' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' :
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993) 
    unm = ('2100080198ai.ds@gmail.com')  
    psw = ('GRoshitha123@')  
    mail.login(unm,psw)  
    stat, total = mail.select('Inbox') 
    print ("Number of mails in your inbox :"+str(total))
    tts = gTTS(text="Total mails are :"+str(total), lang='en') 
    ttsname=("total.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    unseen = mail.search(None, 'UnSeen') 
    print ("Number of UnSeen mails :"+str(unseen))
    tts = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
    ttsname=("unseen.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = mail.uid('fetch', new, '(RFC822)') #fetch
    raw_email = email_data[0][1].decode("utf-8") #decode
    email_message = email.message_from_string(raw_email)
    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    tts = gTTS(text="From: "+email_message['From']+" And Your subject: "+str(email_message['Subject']), lang='en')
    ttsname=("mail.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    stat, total1 = mail.select('Inbox')
    stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print ("Body :"+txt)
    tts = gTTS(text="Body: "+txt, lang='en')
    ttsname=("body.mp3") 
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    mail.close()
    mail.logout()
