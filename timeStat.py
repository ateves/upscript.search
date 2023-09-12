#author: ANTHONY TEVES

#defauly python time module, has certain functions used in overall py file
import time

#Time class constructor function
class Time:
    def __init__(self, timeStat):
        #our constructor, unlike other classes for this project, only holds one variable
        self.timeStat = timeStat
    
    #string representation of the time class, used to return a string of the time
    def __str__(self):
        return f'{self.timeStat}' 

    #takes seconds and returns a string representation for a large amount of time (longer than an hour)
    #the representation is in format hours:minutes:seconds
    def seconds_splitter_big(num):
        number_of_seconds = num
        song_length_string = Time(str(time.strftime("%H:%M:%S", time.gmtime(number_of_seconds))))
        return song_length_string

    #takes seconds and returns a string representation for a smaller amount of time (less than an hour)
    #the representation is in format mins:seconds
    def seconds_splitter_small(num):
        number_of_seconds = num
        song_length_string_a = Time(str(time.strftime("%M:%S", time.gmtime(number_of_seconds))))
        return song_length_string_a
    
    #takes a string representation of mins:seconds and calcilates the time in seconds 
    def get_sec(time_str):
    #Get seconds from time.
        m, s = time_str.split(':')
        return int(m) * 60 + int(s)

#practice 'check' prompts
#print(Time.seconds_splitter_small((Time.get_sec('2:22'))))
