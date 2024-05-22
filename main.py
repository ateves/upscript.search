'''main.py - creates a menu and allows us to search how many times any one word is used in the moviescript.
'''

'''count for us to tally how many times a word appears in our movie script'''
count = 0

'''Function for us so that we can open the movie's script and scan it, and return with the number of hits'''
def check(word, count): 
    with open("upscript.txt") as datafile: 
        for line in datafile: 
            if word in line: 
                count += 1
                return count

'''Generic input ask we need, so that we can use a search word in the function'''
ask = input("what's the word you want to search the movie UP for?")

'''Placing a variable is_word in the search, and calling the function above. count is starting at 0. 'ask' word inputted as seen in above variable'''
is_word = check(ask, count)

'''Syntatic response that gives us in sentence form the result'''
print("The word ",ask," was used ",is_word, "times.")

'''
helpful link for the programmer
https://www.freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python/#:~:text=The%20readlines()%20method%20reads,as%20file%3A%20print(file.
'''

'''THIS PROGRAM WAS WRITTEN BY ANTHONY T'''