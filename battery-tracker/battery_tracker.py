from operator import imod
from numpy import tile
import psutil
import time
import pync
from playsound import playsound


def notify(title, message):
    pync.notify(message=message, sound='ping', title=title)


def track_battery():
    playpath = "/Users/priyanshuparate/projects/python/python_automations/battery-tracker/mixkit-tropical-bird-squeak-27.wav"
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        if battery.power_plugged:
            # Optimazation for proper cpu utilizaiton
            if percent > 30 and percent <= 60:
                time.sleep(30*60)

          # check for the 80 persent and raise alarm
            if percent >= 80:
                notify("batter charged", f"battery charged {percent}")
                playsound(
                    playpath)
                time.sleep(120)

        if not battery.power_plugged:
            # Optimazation for proper cpu utilizaiton
              if percent > 30:
                time.sleep(30*60)

            # check for less than 20 persent and raise alarm
            if percent <= 20:
                notify("batter Low", f"Please charge {percent}")
                playsound(
                    "")
                time.sleep(120)


if __name__ == "__main__":
    notify("test", "this is notification")
