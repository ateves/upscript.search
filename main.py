'''main.py - creates a menu and allows us to search how many times any one word is used in the moviescript.
'''
count = 0

def check(word, count): 
    with open("upscript.txt") as datafile: 
        for line in datafile: 
            if word in line: 
                count += 1
                return count

ask = input("what's the word you want to search the movie UP for?")

is_word = check(ask, count)

print("The word ",ask," was used ",is_word, "times.")

'''
https://www.freecodecamp.org/news/how-to-read-a-file-line-by-line-in-python/#:~:text=The%20readlines()%20method%20reads,as%20file%3A%20print(file.
'''