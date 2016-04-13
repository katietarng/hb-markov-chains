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
    # Initialize empty dictionary
    chains = {}

    words = text_string.split()

    # Iterate over every word in list until there aren't enough words left to fill a tuple of [num] length
    for i in range(len(words) - (num - 1)): 
        n_gram = () #Empty tuple for keys
    
        #Add word at index [i], and all following words, until tuple is [num] words long
        for j in range(num):
            n_gram += (words[i + j],) 

        #If key does not exist in dictionary, initialize key with value = empty list    
        chains[n_gram] = chains.get(n_gram, [])

        #Append word following last word in key, if one exists
        if i + num < len(words): 
            chains[n_gram].append(words[i + num])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    key = choice(chains.keys()) #Choosing random key from chains dict

    text = text + key[0]

    for i in range(1,len(key)):    
        text = text + " " + key[i]  #Adding first word pair to text 

    while chains[key] != []:
        #Choosing random word from value list, append to text, generate new key, repeat

        next_word = choice(chains[key])
        text = text + " " + next_word
        key = key[1:] + (next_word,)

    return text

#Get variables from command line 
input_path = sys.argv[1]
input_num = int(sys.argv[2]) 

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text,input_num)

# Produce random text
random_text = make_text(chains)

print random_text
