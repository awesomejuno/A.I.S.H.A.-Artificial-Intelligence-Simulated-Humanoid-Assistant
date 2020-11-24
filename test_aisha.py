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
import string
from collections import Counter
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
	speak("Entered in testing mode")

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

def test():
	text = open("test.txt", encoding="utf-8").read()
	lower_case = text.lower()

	# Removing punctuations
	cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

	# splitting text into words
	tokenized_words = cleaned_text.split()

	stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
	              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
	              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
	              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
	              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
	              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
	              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
	              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
	              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
	              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

	# Removing stop words from the tokenized words list
	final_words = []
	for word in tokenized_words:
	    if word not in stop_words:
	        final_words.append(word)

	# NLP Emotion Algorithm
	# 1) Check if the word in the final word list is also present in emotion.txt
	#  - open the emotion file
	#  - Loop through each line and clear it
	#  - Extract the word and emotion using split

	# 2) If word is present -> Add the emotion to emotion_list
	# 3) Finally count each emotion in the emotion list

	emotion_list = []
	with open('emotion.txt', 'r') as file:
	    for line in file:
	        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
	        word, emotion = clear_line.split(':')

	        if word in final_words:
	            emotion_list.append(emotion)
	if len(emotion_list)==0 :
		return
	speak("according to my analysis you are feeling")
	for x in emotion_list:
		speak(x)
		print(x)
	file = open("test.txt","r+")
	file. truncate(0)
	file. close()


if __name__ == '__main__': 
	clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file 
	clear() 
	wishMe() 

	
	while True: 
		speak("speak out your feelings")
		query = takeCommand().lower()
		if 'exit' in query:
			exit()
		file_relation = open("test.txt","a")
		file_relation.writelines(query)
		test()



