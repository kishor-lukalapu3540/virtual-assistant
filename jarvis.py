'''
import speech_recognition as sr
listener = sr.Recognizer()
va_name = 'kishore'          # dynamic way of kishore
                             # va_name (virtual assistant name)

try:
    with sr.Microphone() as source:
        print("lets speak man")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()  # it should get all letters in small letters only

        if va_name in command:  # you should mention the name kishore then only got output
            command = command.replace(va_name + ' ','')     # we have to say kishor
                                                           # but print text without kishor name using replace
                                                           # in the place of kishore we gave empty space
            print(command)    # now we can speech anything aftern run

except:
    print("check your microphone")     # if we got any error it will display by try and except concept
'''


'''
import speech_recognition as sr
import pyttsx3                     # this package for text to speech conversion



listener = sr.Recognizer()

speaker = pyttsx3.init()

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

""" RATE"""     # this rate will take after intialize of (speak)
rate = speaker.getProperty('rate')   # getting details of current speaking rate
                       #printing current voice rate
speaker.setProperty('rate', 150)     # setting up new voice rate

#speak('my name is kishor')
#speak ('this is python')
va_name = 'jarvis'          # dynamic way of kishore va_name (virtual assistant name)

speak('i am jarvis please tell me boss')    # call the function here





try:
    with sr.Microphone() as source:
        print("lets speak man")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()  # it should get all letters in small letters only

        if va_name in command:  # you should mention the name kishore then only got output
            command = command.replace(va_name + ' ','')     # we have to say kishor
                                                           # but print text without kishor name using replace
                                                           # in the place of kishore we gave empty space
            print(command)    # now we can speech anything aftern run
            speak(command)

           # speaker.say(command)    # this is for speak jarvis
           # speaker.runAndWait()     #in the place i gave direct function in above speake

except:
    print("check your microphone")     # if we got any error it will display by try and except concept
'''


import speech_recognition as sr
import pyttsx3                     # this package for text to speech conversion



listener = sr.Recognizer()

speaker = pyttsx3.init()

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

""" RATE"""     # this rate will take after intialize of (speak)
rate = speaker.getProperty('rate')   # getting details of current speaking rate
                       #printing current voice rate
speaker.setProperty('rate', 150)     # setting up new voice rate

#speak('my name is kishor')
#speak ('this is python')
va_name = 'hi'          # dynamic way of kishore va_name (virtual assistant name)

speak('i am jarvis please tell me boss')    # call the function here




def take_command():
    command = ''         # if error doesnt matter we can send empty command to code
    try:
        with sr.Microphone() as source:
            print("lets speak ...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()  # it should get all letters in small letters only

            if va_name in command:  # you should mention the name kishore then only got output
                command = command.replace(va_name + ' ','')     # we have to say kishor
                                                               # but print text without kishor name using replace
      #now im going commnet bellow 2 steps print,speak)        # in the place of kishore we gave empty space
                #print(command)    # now we can speech anything aftern run
                #speak(command)

               # speaker.say(command)    # this is for speak jarvis
               # speaker.runAndWait()     #in the place i gave direct function in above speake

    except:
        print("check your microphone")     # if we got any error it will display by try and except concept
    return command

while True:
    user_command = take_command()

    if 'close' in user_command:
        print('see you again boss')
        speak('see you again boss')
        break

    print(user_command)
    speak(user_command)
