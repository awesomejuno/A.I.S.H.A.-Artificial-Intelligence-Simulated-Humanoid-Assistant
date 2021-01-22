# A.I.S.H.A.-Artificial-Intelligence-Simulated-Humanoid-Assistant

Project Report
On¬¬¬
Virtual Assistant
A.I.S.H.A : Artificial Intelligence Simulated Humanoid Assistant
Submitted for the requirement of
BACHELOR OF ENGINEERING

COMPUTER SCIENCE & ENGINEERING

 

Submitted to :   Er. Tanu Dhiman            		                                                           Submitted by:
Kumar Arjun (18BSC15554), Ojas Bhimta(18BCS1569), 
Abhi Pathania(18BCS1574), Danish Mehra (18BCS1564)

			


DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
CHANDIGARH UNIVERSITY, GHARUAN
Nov 2020




CERTIFICATE





This is to certify that the work embodied in this Project Report entitled “Virtual Assistant A.I.S.H.A : Artificial Intelligence Simulated Humanoid Assistant” being submitted by  “ Kumar Arjun (18BSC15554), Ojas Bhimta(18BCS1569), Abhi Pathania(18BCS1574), Danish Mehra (18BCS1564) ”  -, 5th Semester for partial fulfillment of the requirement for the degree of  “ Bachelor of Engineering in Computer Science & Engineering ” discipline in “ Chandigarh University ” during the academic session July-Dec 2020  is a record of  bonafide piece of work, carried out by student under my supervision and guidance in the “ Department of Computer Science & Engineering ”, Chandigarh University.


APPROVED & GUIDED BY: ER. TANU DHIMAN








DECLARATION



I, student of Bachelor of Engineering in Computer Science & Engineering, 5th Semester , session: July – Dec 2019, Chandigarh University, hereby declare that the work presented in this Project Report entitled “Virtual Assistant A.I.S.H.A : Artificial Intelligence Simulated Humanoid Assistant” is the outcome of my own work, is bona fide and correct to the best of my knowledge and this work has been carried out taking care of Engineering Ethics. The work presented does not infringe any patented work and has not been submitted to any other university or anywhere else for the award of any degree or any professional diploma.


Student details and Signature


APPROVED & GUIDED BY: ER. TANU DHIMAN

































To our parents, teachers and all the well wishers out there . . 
















Abstract

This paper discusses about A.I.S.H.A : artificial intelligence simulated humanoid assistant. This voice-enabled virtual assistant can do a sentiment analysis of a particular user based on training data sets. Users can train this voice assistant by themselves with voice commands. This voice-enabled virtual assistant is also capable of doing basic operations. For sentimental analysis, this assistant uses a basic algorithm to identify the emotions of the user.
Keywords— artificial intelligence, machine learning, voice enabled, voice assistant, virtual assistant, sentimental analysis.















 
1.	Introduction

Developments in the field of automation in this modern era is making our world technology-driven. Machines are taking the place of third party workers and reducing human labor efforts with artificial intelligence technology. Artificial intelligent machines are capable of interacting with humans and performing various quantitative and qualitative tasks.
Artificial intelligence-enabled software and personal assistants, work on voice command are trending in this modern world. Those days are gone when setting reminders, sending emails, searching music, and other small tasks were hectic and done manually by the user. Nowadays, these things can be done with voice commands. A voice-enabled virtual assistant is one of the tremendous examples of artificial intelligence and machine learning. Voice-enabled virtual assistants like Google assistant from Google, Siri from Apple, Cortana from Microsoft, and many more can do specific tasks such as setting a reminder, sending messages, sending emails, opening applications, etc. 
In this project, we have tried to combine artificial intelligence and machine learning features to evaluate and analyze an individual's emotion based on the nature and feelings of the word associated with a particular user. 
A.I.S.H.A.: Artificial Intelligence Simulated Humanoid Assistant. Our virtual assistant performs various tasks such as opening applications, playing music, turning off the computer, Hibernate the computer, restart the computer, and many more. These things can be done by various virtual assistant products available on the market or community, but they lack analyzing the particular users' sentiment and emotion.
Our virtual assistant takes training on voice commands given by the user and asks for the user's particular emotion related to that word or scenario. This process helps the software to analyze the feeling of a person accurately and precisely.







2.	Literature Review
Voice-enabled virtual assistants are a fascinating topic for research and development in artificial intelligence and machine learning. Various voice assistants like Google personal assistant, Siri, and Cortana are in the market. These assistants can perform multiple tasks and operations based on global set standards for dependent variables. These voice-enabled virtual assistants can do basic operations and have many basic features but fail in emotion detection and sentiment analysis.
In the Python programming language, a library named N.L.T.K. library is used for sentiment analysis. Using this library, we can compute the score for emotions, which gives results in numeric format. Based on the numeric result, the program analyses and gives the predicted emotion as positive-negative, or neutral. Without providing any specific sentiment, this program only tells whether the text's emotion is positive-negative or neutral.
There have been various developments in the field of sentimental analysis and emotion detection. Using artificial intelligence and machine learning algorithms, emotion detection and sentiment analysis are possible. Our project takes training from the individual user, only discarding the limitation of dependency on global set variables of emotions. This specialized training helps the voice-enabled virtual assistant to precisely detect and predict particular user emotions.





















3.	Methodology
This paper proposes a naive algorithm for the analysis of sentiment and emotion of the individual user. As the name suggests, artificial intelligence simulated humanoid assistant; it learns from the user. It uses a simple algorithm for the detection of emotion.
It can also perform basic things like telling date and time, current temperature, setting a reminder, opening applications like Google Chrome, calculator camera, and others, telling jokes, and other operations.

 
Figure 1 Modes of virtual Assistant

The features of this voice-enabled virtual assistant can be categorized into three categories:

The first category is doing basic operations like opening applications telling jokes, date and time updates, weather updates, playing music, Wikipedia search, or opening any website.
 
Figure 2 Performing basic operations

The second category is the training mode. Training mode consists of two modes, namely emotional training, and relational training. In emotional training, the user first saves the specific word as intent by giving the command speech input. After that user can tell the emotion associated with that particular word. All these intents are saved in a specific format into the text file in the module.
In relational training mode, the user speaks up the name of a person, and then the assistant asks for the relation intent associated with that person. These intents are also saved in specific format into the text file in the module.
 
Figure 3 Training Mode

The third mode is the testing mode, which is an essential part of this project. After entering into this mode, the assistant asks for voice input, and after processing that voice input as text input, it gives the analysis of emotion. After applying the algorithm to the speech input, the software provides the study of emotions and sentiments present in the user's feedback.
 
Figure 4  Testing Mode
























4.	Implementation

Python programming language has been used for the development and implementation of this virtual assistant.
Many inbuilt libraries and APIs like Google speech recognition have converted the user's voice input into text.
For basic operations like DateTime, telling jokes, setting a reminder, opening applications, searching Wikipedia, etc., specified API has been used.
A primary data file handling system has been used in training mode for saving personal and relational training contents.
The testing model uses the algorithm based on a basic search for sentiment analysis. Before processing the data for sentiment analysis, unnecessary text and punctuations have been removed from the voice input.

N.L.P. Emotion Algorithm
	# 1) Check if the word in the final word list is also present in emotion.txt
	#  - open the emotion file
	#  - Loop through each line and clear it
	#  - Extract the word and emotion using split

	# 2) If word is present -> Add the emotion to emotion_list
	# 3) Finally count each emotion in the emotion list



















5.	Requirements

•	subprocess 
•	wolframalpha 
•	pyttsx3 
•	tkinter 
•	json 
•	random 
•	operator 
•	speech_recognition 
•	datetime 
•	wikipedia 
•	webbrowser 
•	os 
•	winshell 
•	pyjokes 
•	feedparser 
•	smtplib 
•	ctypes 
•	time 
•	requests 
•	shutil 
•	twilio.rest -> Client 
•	clint.textui -> progress 
•	string
•	collections -> Counter
•	bs4 -> BeautifulSoup 

•	win32com.client -> wincl 
•	urllib.request -> urlopen










6.	Results and Discussion

The result of the sentimental analysis of the voice input given by the user was satisfying. The assistant produced the list of all emotions and sentiments associated with the user's voice input. But 100% accuracy has not been achieved. The analysis of sentiments and emotion is based on the intents saved in the module. Users have to train the model properly before using the testing mode. The leading cause of the error that causes failure in achieving 100% accuracy is distortion or interruption in voice commands. The model also depends upon the training given by the user. This assistant requires high-speed internet connectivity for better text to speech conversions.






7.	Conclusion

Voice-enabled virtual assistants are one of the best applications of artificial intelligence and machine learning. This paper discusses the basic algorithm used for sentiment analysis of individual users. This paper also concerns the methodology and implementation of this voice-enabled virtual assistant to understand the results sufficiently. Due to voice interruption and training errors, it misses achieving 100% accuracy. We can attain 100% accuracy if the individual user itself trains the model, and there is no interruption in the voice input.














8.	Future Enhancements

Our goal was to achieve 100% accuracy. To achieve 100% accuracy in the future, there must be some advancement and modification in text to speech API and training algorithms. In the end, this voice-enabled virtual assistant can be used as a lifesaver. If the user feels demotivated or stressed, it can send SMS to inform the close relatives or friends from the intents saved in relation training. This voice assistant can also be used for or reporting the closed one in social circles about the user's present emotion and sentiment.


References


[1]	"AI Based Voice Assistant Using Python", International Journal of Emerging Technologies and Innovative Research (www.jetir.org), ISSN:2349-5162, Vol.6, Issue 2, page no.506-509, February-2019, Available :http://www.jetir.org/papers/JETIR1902381.
[2]	Artificial intelligence (AI), sometimes called machine intelligence. https://en.wikipedia.org/wiki/Artificial_intelligence
[3]	B. Marr, The Amazing Ways Google Uses Deep Learning AI..
[4]	Cortana Intelligence, Google Assistant, Apple Siri.
[5]	Hill, J., Ford, W.R. and Farreras, I.G., 2015. Real conversations with artificial intelligence: A comparison between human–human online conversations and human–chatbot conversations. Computers in Human Behavior, 49, pp.245-250.
[6]	K. Noda, H. Arie, Y. Suga, T. Ogata, Multimodal integration learning of robot behavior using deep neural networks,
          Elsevier: Robotics and Autonomous Systems, 2014.
[7]     "CMUSphnix Basic concepts of speech - Speech Recognition   process".
         http://cmusphinx.sourceforge.netlwiki/tutorialconcepts

