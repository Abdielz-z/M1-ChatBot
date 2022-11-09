import gtts
from playsound import playsound

def lee(palabra, src):
    if (src == "en"):
        leer= str(palabra+1)+".mp3"
        playsound(leer)
