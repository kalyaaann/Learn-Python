import time
import winsound
#input to take the alarm time
alarm_time = input("Enter alarm time (HH:MM:SS): ")

while True:
    #convert the time to string format 
    #strftime: string format time
    current_time = time.strftime("%H:%M:%S")
    print("\rCurrent Time:", current_time, end="")

    if current_time == alarm_time:
        print("\n Alarm Ringing...")
        for i in range(5):
            winsound.Beep(1000, 1000)  # frequency, duration
        break

    time.sleep(1)