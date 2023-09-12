# main.py - create two playlists and allow the user to interact with them.
# Author:

#uses a large number of imports from .py files in this directory to os, time, random, and csv
import song
import playlist
import timeStat
import time
import random
import os
import csv

#import data which generates song class objects inside two different playlist objects
#big playlist holds all 500 listed songs organized
#small playlist holds only 2% of the total 500
def import_data(big,small):
    #gives us a list of course names
    #big.playlist_content
    with open("upscript.txt", "r", encoding="utf8") as songs_file:
        tsv_reader = csv.reader(songs_file, delimiter="\t")
        for row in tsv_reader:
            (rank, artist, title, length, year) = row
            holder_song = song.Song(int(row[0]),str(row[1]),str(row[2]),str(row[3]),int(row[4]))
            playlist.Playlist.add_song(holder_song,big)
            #if the number rolled by two random generators is a 1 or a 2 then we add that given song being looped again to the small playlist
            #the percent chance here is 2% because the 1 or 2 has to match with a random generator between 1 and 100
            r1 = random.randint(0, 100)
            r2 = random.randint(0, 2)
            if r2 == r1:
                playlist.Playlist.add_song(holder_song,small)
    
    #check comments
    #print(big)
    #print(small)

#menu text function. (included in code)
def print_menu():
    print('1. Display small playlist info')
    print('2. Add a song to the small playlist')
    print('3. Delete a song from the small playlist')
    print('4. Sort small playlist')
    print('5. Search big playlist by artist')
    print('6. Exit')

#get choice function (included in code)
def get_choice():
    ch = ''
    while not ch.isdigit() or int(ch) < 1 or int(ch) > 6:
        ch = input('Choice: ')
    return int(ch)

#main function
if __name__ == '__main__':\
    #populates two playlists with empty lists and the title Big Playlist and Small Playlist
    empty_list = []
    big_playlist = playlist.Playlist("Big Playlist",empty_list)
    small_playlist = playlist.Playlist("Small Playlist",empty_list)
    #import_data(big_playlist, small_playlist)

    #calls the import data function in order to populate the empty lists with RollingStone text file data
    import_data(big_playlist, small_playlist)

    #generates a string of the big playlist's grand total time (always about 34 hours and some change
    time_check_big = playlist.Playlist.add_song_lengths_big(big_playlist)

    #prints the string of the big playlist info and as well as the time check we generated
    print(big_playlist,time_check_big)

    #duration also does the same but I am not opting to use it in this prograem (it exists though)
    #print(playlist.Playlist.duration(big_playlist))
    
    #print menu call
    #choice while loop and reset calls for in case we dont pick a viable option
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice()

        #choice 1 prints small playlist information including titles, playlist length, and duration
        if choice == 1:
            time_check_small = playlist.Playlist.add_song_lengths_small(small_playlist)
            print(small_playlist,time_check_small)
            small_playlist.print_songs()

        #choice 2 adds a song from small playlist
        elif choice == 2:    

            #Additional request print statement
            print("We will add a song from big playlist and add it to the small playlist.")
            song_title_input_b = str(input("What's the song's title?\n"))

            #for loop iterating through 500 song contents
            for items in big_playlist.playlist_content:

                #string changes to lower case for case match edge case
                items_title_hold = items.title.lower()
                song_title_input_b = song_title_input_b.lower()
                
                #if song string values match, creates a new song and adds that song to the small playlist.)
                if song_title_input_b == items_title_hold:
                    floating_song = song.Song(items.rank,items.artist,items.title,items.length,items.year)
                    playlist.Playlist.add_song(floating_song,small_playlist)
                else:
                    #if there is no string match, move on to the next song in big playlist
                    pass

            #prints out small playlist information including song content, playlist length, and time duration
            time_check_small = playlist.Playlist.add_song_lengths_small(small_playlist)
            print(small_playlist,time_check_small)
            
            #choice 3, deletes a song from small playlist
        elif choice == 3:

            #search term request
            song_title_input = str(input("What's the title of the song you want to remove from Small Playlist?\n"))
            
            #for loop that scans small playlist songs/items
            for items in small_playlist.playlist_content:

                #converst search term and item title to string lowercased. used for case match edge case
                items_title_hold = items.title.lower()
                song_title_input_a = song_title_input.lower()

                #if matching deletes item from small playlist
                if song_title_input_a == items_title_hold:
                    print(song_title_input," has been deleted.")
                    playlist.Playlist.del_song(items,small_playlist)
                #if not matching, iterate through next item in the small playlist
                else:
                    pass
        
        #option 4, sorts the small playlist by certain criteria
        elif choice == 4:
            #calls sort function from the playlist class
            playlist.Playlist.sort(small_playlist)

        #option 5, searches big playlist by a artist name and prints all song titles by that musician
        elif choice == 5:
            search_term_input_a = str(input("What's the artist that you want to search by?"))
            playlist.Playlist.search(search_term_input_a,big_playlist)
