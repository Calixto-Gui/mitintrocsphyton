# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from tkinter import *
from datetime import datetime
import pytz
import collections
collections.Callable = collections.abc.Callable



#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
            # pubdate = pubdate.astimezone(pytz.timezone('EST'))
            # pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        '''
        Used to safely access self.guid outside of the class
        
        Returns: self.guid
        '''
        return self.guid
    
    def get_title(self):
        '''
        Used to safely access self.title outside of the class
        
        Returns: self.title
        '''
        return self.title
    
    def get_description(self):
        '''
        Used to safely access self.description outside of the class
        
        Returns: self.description
        '''
        return self.description
    
    def get_link(self):
        '''
        Used to safely access self.link outside of the class
        
        Returns: self.link
        '''
        return self.link
    
    def get_pubdate(self):
        '''
        Used to safely access self.pubdate outside of the class
        
        Returns: self.pubdate
        '''
        return self.pubdate
    

#======================
# Triggers
#======================

class Trigger(object):
    # def __init__(self, story):
    #     self.story = story
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError
    
    def __str__(self):
        return str(self)

    
        
# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
        self.text = ''
        
        
    def get_phrase(self):
        return self.phrase
    
    def get_text(self):
        return self.text
    
    def set_phrase(self, newphrase):
        self.phrase = newphrase
        
    def set_text(self, newtext):
        self.text = newtext
    
    
    def is_phrase_in(self):
        
        text = self.get_text()
        text = text.lower()
        phrase = self.get_phrase()
        phrase = phrase.lower()
        punctuation = string.punctuation
        
        for c in punctuation:
            text = text.replace(c," ")
            
        text_lst = text.split()
        phrase_lst = phrase.split()
            
        return any(phrase_lst == text_lst[i:i+len(phrase_lst)] for i in range(len(text_lst) -1))
        
        
        

# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
       PhraseTrigger.__init__(self, phrase)
       
    def evaluate(self, story):
        self.story = story
        self.set_text(story.get_title())
        return self.is_phrase_in()
        
    

# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
       PhraseTrigger.__init__(self, phrase)
       
    def evaluate(self, story):
        self.story = story
        self.set_text(story.get_description())
        return self.is_phrase_in()

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self):
        self.time = ''
        
    def get_time(self):
        return self.time
    
    def set_time(self, newtime):
        
        # self.time = datetime.strptime(newtime, "%d %b %Y %H:%M:%S" )
        self.time = newtime.replace(tzinfo=pytz.timezone("EST"))
        
        
        

# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
    def __init__(self, time_trigger):
        self.time_trigger = datetime.strptime(time_trigger, "%d %b %Y %H:%M:%S" )
        # time_trigger = time_trigger.replace(tzinfo=pytz.timezone("EST"))
        
    def get_time_trigger(self):
        return self.time_trigger.replace(tzinfo=pytz.timezone("EST"))
        
    def evaluate(self, time):
        self.time = time
        self.set_time(time.get_pubdate())
        return self.get_time_trigger() > self.get_time()
    
class AfterTrigger(TimeTrigger):
    def __init__(self, time_trigger):
        self.time_trigger = datetime.strptime(time_trigger, "%d %b %Y %H:%M:%S" )
        # time_trigger = time_trigger.replace(tzinfo=pytz.timezone("EST"))
        
    def get_time_trigger(self):
        return self.time_trigger.replace(tzinfo=pytz.timezone("EST"))
        
    def evaluate(self, time):
        self.time = time
        self.set_time(time.get_pubdate())
        return self.get_time_trigger() < self.get_time()


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
    
    def __init__(self, trigg):
        self.trigg = trigg
        
    def get_trigg(self):
        return self.trigg
    
    def evaluate(self, news):
        
        x = self.get_trigg().evaluate(news)
        
        return not x
    
        

# Problem 8
# TODO: AndTrigger

class AndTrigger(Trigger):
    
    def __init__(self, trigg1, trigg2):
        self.trigg1 = trigg1
        self.trigg2 = trigg2
        
    def get_trigg1(self):
        return self.trigg1
    
    def get_trigg2(self):
        return self.trigg2
    
    def evaluate(self, news):
        
        x1 = self.get_trigg1().evaluate(news)
        x2 = self.get_trigg2().evaluate(news)
        
        return x1 and x2

# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
    
    def __init__(self, trigg1, trigg2):
        self.trigg1 = trigg1
        self.trigg2 = trigg2
        
    def get_trigg1(self):
        return self.trigg1
    
    def get_trigg2(self):
        return self.trigg2
    
    def evaluate(self, news):
        
        x1 = self.get_trigg1().evaluate(news)
        x2 = self.get_trigg2().evaluate(news)
        
        return x1 or x2


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    fired_story = []
    
    for trig in triggerlist:
        for story in stories:
            if trig.evaluate(story):
                fired_story.append(story)
    
    return fired_story



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    
    dict={}
    lst=[]
    for c in lines:
        x = c.split(",")
        if x[1] == 'TITLE':
            dict[x[0]] = TitleTrigger(x[2])
        elif x[1] == 'DESCRIPTION':
            dict[x[0]] = DescriptionTrigger(x[2])
        elif x[1] == 'BEFORE':
            dict[x[0]] = BeforeTrigger(x[2])
        elif x[1] == 'AFTER':
            dict[x[0]] = AfterTrigger(x[2])
        elif x[1] == 'NOT':
            dict[x[0]] = NotTrigger(x[2])
        elif x[1] == 'AND':
            dict[x[0]] = AndTrigger(x[2],x[3])
        elif x[1] == 'OR':
            dict[x[0]] = OrTrigger(x[2],x[3])
        if x[0] == 'ADD':
            for y in range(1,len(x)):
                lst.append(dict[x[y]])

    # print(lines) # for now, print it so you see what it contains!
    return lst



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("Lula")
        t2 = DescriptionTrigger("EUA")
        t3 = DescriptionTrigger("caças")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

