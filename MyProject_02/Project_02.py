# MY PROJECT OF VOICE TRANSLATTER
import googletrans
import speech_recognition
import gtts
import playsound

# Set input and output languages
input_lang = "en"  
output_lang = "hi" 

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak now")  
# convert recognized speech to text to input language
    voice = recognizer.listen(source)  
    text = recognizer.recognize_google(voice, language=input_lang)  

# Translate the recognized text to the output language
translator = googletrans.Translator()
translation = translator.translate(text, dest=output_lang)
print(translation.text) 

# Convert the translated text to speech
converted_audio = gtts.gTTS(translation.text, lang=output_lang)
converted_audio.save("vikas.mp3") 
playsound.playsound("vikas.mp3")
