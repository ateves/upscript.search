# playlist.py - a class that represents a playlist of songs

import song
import timeStat

class Playlist:
    """A playlist has a name and contains zero or more songs."""
    def __init__(self,name,playlist_content):
        self.name = name
        empty_list = []
        self.playlist_content = empty_list

        """Initialize the playlist by setting its name and the list of songs
	to empty.
	Hint: see the BadKangaroo example at the end of Chapter 17 and make sure
	you don't make the same mistake in your playlist code.
	"""
    #string representation of the playlist organizing name, number of songs in the playlist, and the time duration of the full playlist.
    #time is calculated outside of the string
    def __str__(self):
        return f'The title of the playlist is {self.name} and the number of songs it contains is {str(len(self.playlist_content))} and the duration of the playlist is' 
        #Return a string representation of the playlist that includes:
        #1. its name
        #2. the number of songs it contains
        #3. the total duration (calculated outside)

    #string representation of the playlist class. can be called for a simple string representation of the string that is stored in memory
    def __repr__(self):
        return f'Playlist(\'{self.name}\', {self.playlist_content})'
    
    #class that prints all the song titles in a/the playlist given
    def print_songs(playlist_name):
        print("The items in ",playlist_name.name," include:\n")
        for item in playlist_name.playlist_content:
            print(item.title,"\n")
    
    #the song length calculator code for finding the total length in seconds from a string of 'mins:seconds'
    #in main this is combined with the __str__ to complete the information read by the user
    #playlist length is going to be shorter than an hour
    def add_song_lengths_small(playlist_name):
        a = 0
        for element in playlist_name.playlist_content:
            y_item = timeStat.Time.get_sec(element.length)
            a += y_item
        time_split = timeStat.Time.seconds_splitter_small(a)
        return time_split
    
    #same function as above but used only for the calculation of the 500 playlist song
    #need this code and use of Time class because the length is more than one hour
    def add_song_lengths_big(big_playlist_name):
        a = 0
        for element in  big_playlist_name.playlist_content:
            y_item = timeStat.Time.get_sec(element.length)
            a += y_item
        time_split = timeStat.Time.seconds_splitter_big(a)
        return time_split
    
    #the song is added to the playlist via list appending in this function
    def add_song(song_name,playlist_name):
        playlist_name.playlist_content.append(song_name)
        #Adds the given song to the playlist
        return playlist_name
    
    #a song is deleted from the playlist based on an index search and then index deletion
    def del_song(song_name,playlist_name):
        index = playlist_name.playlist_content.index(song_name)
        del playlist_name.playlist_content[index]
    
    #a function that takes an artist searh term in string and scans the list of songs for the titles based on the search tern
    #prints a list of all songs by that artist
    def search(search_term,playlist_name):
        print("The following are all the songs by ",search_term,":\n")
        for item in playlist_name.playlist_content:
            if str(search_term.lower()) not in str(item.artist.lower()):
                pass
            else:
                print(item.title)
                
    #larger sort class function with given menu option
    def sort(playlist_name):

        how_to_sort = input("1.Rank highest to lowest\n2.Alphabetically by artist\n3.Alphabetically by title\n4.Shortest to longest song time length\n5.Least recent to most recent, year of release\nEnter a selection:\n")
        
        #if not 1 - 5, resets the menu prompt
        if str(how_to_sort) not in "12345":
            print("That was not a viable selection, decide again.")
            Playlist.sort(playlist_name)
        
        #option 1, sorts the playlist by ranking of songs, 1 is a higher ranking than 2 FYI
        elif str(how_to_sort) == "1":
            print("For ",playlist_name.name," the sorting by ranking of each song is as follows:\n") 
            sortedByRank = sorted(playlist_name.playlist_content, key=lambda song: song.rank)
            for item in sortedByRank:
                #print statment
                print(item.rank,": ",item.title)

        #option 2, sorts the playlist by artist alphabetically
        elif str(how_to_sort) == "2":
            print("For ",playlist_name.name," the sorting alphabetically by artist is as follows:\n")
            sortedByArtistName = sorted(playlist_name.playlist_content, key=lambda song: song.artist)
            for item in sortedByArtistName:
                #print statment
                print(item.artist,": ",item.title)
        #option 3, sorts the playlist by title alphabetically
        elif str(how_to_sort) == "3":
            print("For ",playlist_name.name," the sorting alphabetically by song title is as follows:\n")
            sortedBySongName = sorted(playlist_name.playlist_content, key=lambda song: song.title)
            for item in sortedBySongName:
                #print statement
                print(item.title,": ",item.artist)

        #option 4, sorts the playlist by time shortest to longest
        elif str(how_to_sort) == "4":
            print("For ",playlist_name.name," the sorting from shortest song length to longest is as follows:\n")
            #calculating code used to break song length down to seconds and arrange shortest to longest
            sortedBySongLength = sorted(playlist_name.playlist_content, key=lambda song: timeStat.Time.get_sec(song.length))
            for item in sortedBySongLength:
                #print statement
                print(item.length," - ",item.title)

        #option 5, sorts the playlist by least recent to most recent
        elif str(how_to_sort) == "5":
            print("For ",playlist_name.name," the sorting from least recent to most recent publishing date is as follows:\n")
            sortedByRelease = sorted(playlist_name.playlist_content, key=lambda song: song.year)
            for item in sortedByRelease:
                #print statement
                print(item.year,": ",item.title)

        #only takes 1-5 as options. if any other input is entered, resets the sort function
        else: 
            print("That was not a viable selection, decide again.")
            Playlist.sort(playlist_name)
            #sorted(playlist_name.playlist_content.self.rank, key=lambda)
            #for item in playlist_name.playlist_content:
            #    print(item.rank,item.title)
         #   print("For ",playlist_name.name," the sorting, alphabetically by artist is:\n")
          #  for item in playlist_name.playlist_content:
           #     playlist_name.playlist_content.sort(key=lambda Song: item.artist)
            #    print(item.artist,": ",item.title,"\n")
        #Sort the songs on the playlist based on a given field
	#You can use the built-in list function sort to sort on a given field:
	#list.sort(key=lambda song: song.rank)
	#Note: the less than operator must be defined to use the built-in sort function
	#Less than is already defined for ints and strings, but you will have to
	#overload the less than operator so that it works on your Time class.

    #code for calculating seconds from a string adding the seconds to a counter and then returning the seconds
    #converted back to a string in hours:mins:seconds form. This playlist wasnt used in main
    def duration(playlist_name):
        a = 0
        for items in playlist_name.playlist_content:
            song_time_seconds = timeStat.Time.get_sec(items.length)
            a += song_time_seconds
        return timeStat.Time.seconds_splitter_big(a)

"""Calculates the duration of a playlist by adding the length of all its songs."""

#This program was written by ANTHONY TEVES