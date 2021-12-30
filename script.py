from datetime import datetime
from threading import Timer
import webbrowser

x=datetime.today()
y=x.replace(day=x.day, hour=0, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
    print ("Happy New Year 🎉")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    

print("WAITING..... ")
t = Timer(secs, hello_world)
t.start()