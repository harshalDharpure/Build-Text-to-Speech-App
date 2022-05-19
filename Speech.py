from gtts import gTTS
import os

mytext="Hello My name is Harshal Dharpure"
language='en'

output=gTTS(text=mytext,lang=language,slow=False)
output.save("output.mp3")

os.system("start output.mp3 ")
