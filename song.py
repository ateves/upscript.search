# song.py - a class that represents a song
# Author:ANTHONY TEVES

#not used but here if needed, the timeStat helps calculate time in seconds and also formats time in hour:minutes:seconds or mins:seconds
import timeStat

#class for Song type
class Song:

    #constructor for any song object. includes 5 different variables
    def __init__(self, rank, artist, title, length, year):
        self.rank = rank
        self.artist = artist
        self.title = title
        self.length = length
        self.year = year
        """
        rank: int
        artist: String
        title: String
        len: Time
        year: int
        """


    def __str__(self):
        #string default when str() is called for the song class object. only includes title, uear, and artist.
        #editable for more flexibility if needed, since the song class also includes rank, length, and year
        return f'The title of the song is {self.title} and the year of the song is {self.year} and the artist is {self.artist}.'

        """Returns a string representation of the song that includes:
        1. its title
        2. its year
        3. its artist
        """

    #printable representation of the song object
    def __repr__(self):
        return f'Song(\'{self.rank}\', {self.artist}\', {self.title}\', {self.length}\', {self.year})'
#c = Song(2,'anthony teves','country roads','30:31',22)
#print(repr(c))
