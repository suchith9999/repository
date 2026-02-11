
from playsound import playsound
import threading
import time
# playsound("alarm-siren-sound.mp3")


def runner():

        threading.Thread(target=playsound("alarm-siren-sound.mp3"), daemon=True).start()





