from playsound import playsound
import time
CLEAR = "\033[2J"
RED = "\033[0;31m"
CLEAR_AND_RETURN_TO_STARTPOSTN = "\033[H"
def alarm(seconds):
    time_elapsed =0
    print(CLEAR)
    print(RED)
    while time_elapsed<seconds:

        time.sleep(1)
        time_elapsed+=1
        time_left = seconds-time_elapsed
        minutes_left = time_left//60
        seconds_left = time_left % 60
        print(f"{CLEAR_AND_RETURN_TO_STARTPOSTN} {minutes_left:02d} : {seconds_left:02d}")
    playsound("alarm.mp3")

while True:
    minutes = input("How many minutes you want to keep alarm for?")
    if not minutes.isdigit():
        print("Enter valid minutes")
        continue
    else:
        minutes = int(minutes)
        break
while True:
    seconds = input("How many seconds you want to keep alarm for?")
    if not seconds.isdigit():
        print("Enter valid seconds")
        continue
    else:
        seconds=int(seconds)
        break

total_time = minutes*60 + seconds
alarm(total_time)