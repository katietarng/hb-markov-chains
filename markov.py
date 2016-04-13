from random import choice
import sys

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    the_file = open(file_path)
    file_text = the_file.read()

    the_file.close()

    #Note the new line characters still exist in super string
    return file_text


def make_chains(text_string, num):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - (num - 1)): #Only initialize n_gram if there are enough words to fill
        n_gram = () #Empty tuple for keys
    
        for j in range(num):
            #Add words to n_gram as tuple, in order, until desired length reached
            n_gram += (words[i + j],) 

        chains[n_gram] = chains.get(n_gram, []) #Initializing key,pair value for chains

        if i + num < len(words): #Appending word following n_gram to value list
            chains[n_gram].append(words[i + num])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    key = choice(chains.keys()) #Choosing random key from chains dict

    for i in range(len(key)):    
        text = text + " " + key[i]  #Adding first word pair to text 

    print text

    while chains[key] != []:
        #Choosing random word from value list, append to text, generate new key, repeat

        next_word = choice(chains[key])
        text = text + " " + next_word
        key = (key[1], next_word)

    return text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text,3)

# Produce random text
random_text = make_text(chains)

print random_text
