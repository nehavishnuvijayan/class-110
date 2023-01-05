import random
response=input("Enter yes or no:")
def dice(response):
    if response=="yes":
        no=random.randint(1,6)
        if no == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        elif no == 3:
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
        elif no == 4:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
        elif no == 5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
    else:
        print("user don't want to roll the die")
dice(response)
'''
import time
#print(dir(time))
seconds=input("Enter the time in seconds:")
def counter(seconds):
    while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer = f'{mins}:{secs}'
        time.sleep(5)
        print(timer)
        seconds -=1
    print("Times up!")
counter(int(seconds))
'''