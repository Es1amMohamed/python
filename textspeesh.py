from gtts import gTTS 
import os

text1 = input('enter your text').strip()

adc = open(text1)

text = adc.read()


language = 'ar'

obj = gTTS(text = text ,  tld ='co.in' ,lang = language , slow = False )

obj.save('test.mp3')

os.system('test.mp3')