import string
from ps5 import *

phrase = 'Purple COw green'
text = 'The Purple!!# $COW!green!! is*)() soft and cuddly'
# text_low = text.lower()
# punctuation = string.punctuation

# for c in punctuation:
#     text_low = text_low.replace(c,"")

# print(phrase in text_low)




# text = text.lower()
# phrase = phrase.lower()
# punctuation = string.punctuation
        
# for c in punctuation:
#     text = text.replace(c," ")
            
# text_lst = text.split()
# phrase_lst = phrase.split()

# t = any(phrase_lst == text_lst[i:i+len(phrase_lst)] for i in range(len(text_lst) -1))
            
# print(t)

# from datetime import datetime

# date = '3 Oct 2016 17:00:10'

# date_converted = datetime.strptime(date, "%d %b %Y %H:%M:%S" )

# print(date_converted)

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
        
        

    print(dict) # for now, print it so you see what it contains!
    print(lst)

read_trigger_config("triggers.txt")

t1 = TitleTrigger("election")
t2 = DescriptionTrigger("Trump")
t3 = DescriptionTrigger("Clinton")
t4 = AndTrigger(t2, t3)
triggerlist = [t1, t4]

# print(triggerlist)
        