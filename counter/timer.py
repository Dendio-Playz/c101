import time

def counter(seconds):
    while seconds>0:
        mins = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{mins}:{secs}'
        print(timer)
        seconds -=1
    print('timeup')

seconds = input("Enter the time in seconds")
counter(int(seconds)) 