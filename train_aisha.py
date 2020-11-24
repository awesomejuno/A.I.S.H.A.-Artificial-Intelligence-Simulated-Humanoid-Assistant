import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from twilio.rest import Client 
from clint.textui import progress 
#from ecapture import ecapture as ec 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen 
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 
def speak(audio): 
	engine.say(audio) 
	engine.runAndWait() 

def wishMe(): 
	
	assname =("AISHA : Artificial Intelligence Simulated humanoid assistant") 
	speak(assname) 
	speak("Entered in training mode. Kindly choose between emotion training or personal details training")



def takeCommand(): 
	
	r = sr.Recognizer() 
	
	with sr.Microphone() as source: 
		
		print("Listening...") 
		r.pause_threshold = 1
		audio = r.listen(source) 

	try: 
		print("Recognizing...")	 
		query = r.recognize_google(audio, language ='en-in') 
		print(f"User said: {query}\n") 

	except Exception as e: 
		print(e)	 
		print("Unable to Recognizing your voice.") 
		return "None"
	
	return query

def emotional_training():
	while True:
		speak("speak the word for emotional training")
		word = takeCommand().lower()
		if 'None' in word :
			emotion_training()
		elif 'relation' in word:
			relation_training()
		elif 'exit' in word:
			return
		speak("tell me the emotion associated with this word")
		emotion = takeCommand().lower()
		if 'None' in emotion :
			emotion_training()
		elif 'exit' in emotion:
			return
		bb=["'"+word+"'"+ ": '" +emotion+"',\n"]
		file_emotion = open("emotion.txt","a")
		file_emotion.writelines(bb)
		file_emotion.close()
def relation_training():
	while True:
		speak("speak the name for relational training")
		name = takeCommand().lower()
		if 'none' in name :
			return 'emotion'
		elif 'exit' in name:
			return
		speak("tell me the relation associated with this word")
		relation = takeCommand().lower()
		if 'none' in relation :
			relation_training()
		elif 'exit' in relation:
			return
		ab=["'"+name+"': '" +relation+"',\n"]
		file_relation = open("relation.txt","a")
		file_relation.writelines(ab)

		file_relation.close()

if __name__ == '__main__': 
	clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file 
	clear() 
	wishMe() 

	
	while True: 
		speak("tell me type of training : emotion or realation")
		query = takeCommand().lower()
		if 'emotion' in query:
			emotional_training()
		elif 'relation' in query:
			relation_training()
		elif 'exit' in query:
			exit()

