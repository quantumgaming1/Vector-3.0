#VECTOR VERSION 3.0

print ('loading......')

#import library
import win32com.client as wincl
import speech_recognition as sr
import sys
import webbrowser
import os
speak = wincl.Dispatch("SAPI.SpVoice")
# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

def main():
    with sr.Microphone() as source:
        print("Please Speak:")
        say = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=0.001)
        
          
        try:
            # using google speech recognition
            print("Text: "+r.recognize_google(say))
              
        except:
             print("Retry")
             
    #processin
    #mic in- see above





    #computing
    text = r.recognize_google(say)

    
    if text == "hi":
        speak.Speak("Hello")
        main()
    if text == "stop":
        sys.exit()
        main()
    if text == "help":
        print ('help, stop, hi, open web, shutdown')
        main()
    if text == "open web":
        speak.Speak("Opening Google")
        webbrowser.open('http://google.com', new=2)
        main()
    if text == "shutdown":
        speak.Speak("Shutting Down, Goodnight")
        os.system("shutdown /s /t 1")
        main()
    if text == "shut down":
        speak.Speak("Shutting Down, Goodnight")
        os.system("shutdown /s /t 1")
        main()   
    if text == "testing":
        speak.Speak('Hearing and speach test succesfull!')
        main()
    
    












    #processout


while True:
    main()












