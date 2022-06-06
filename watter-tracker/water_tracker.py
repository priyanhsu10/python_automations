import time
from playsound import playsound
import pync
import datetime


def notify(message, title):
    pync.notify(title=title, message=message, sound="ping")


def track_watter():
    soundPath = "/Users/priyanshuparate/projects/python/python_automations/watter-tracker/water-filled-cup-9901.mp3"
    glasscount = 8
    currenthr = datetime.datetime.now().hour
    while True:
        if glasscount == 0 or currenthr > 23:
            break
        if currenthr > 9 and currenthr < 23 and glasscount > 0:

            notify("drink one glass of watter",
                   f"Drink water,{glasscount} yet to drink")

            glasscount -= 1
            playsound(soundPath)
            time.sleep(80*60)


if __name__ == "__main__":
    track_watter()
