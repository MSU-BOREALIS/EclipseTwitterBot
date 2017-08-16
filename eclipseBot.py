import tweepy
import time
from credentials import *
import sys
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet = "#Eclipse2017 #EclipseBallooning #NASAspacegrant #Rexburg @MTSpaceGrant @MontanaState"

#api.update_status(tweet)
#api.update_with_media('SolarEclipse.jpg',tweet)

class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.jpg", "*.png"]

    def process(self, event):
        print("Processing")
    def on_modified(self, event):
        self.process(event)
        print("File Modified")
    def on_created(self, event):
        self.process(event)
        api.update_with_media(event.src_path,tweet)


if __name__ == '__main__':

    observer = Observer()
    #Modify path in following line of code to where the pictures will be stored.
    observer.schedule(MyHandler(), path='/home/trevor/Documents/Borealis/TwitterEclipseBot/', recursive = True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
