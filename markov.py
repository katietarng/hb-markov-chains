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

    for i in range(len(words) - 1):
        word_pair = ()
        
        while len(word_pair) < num: 
            word_pair += #Rebind tuple to tuple + next_word until len = num
            chains[word_pair] = chains.get(word_pair, []) #Initializing key,pair value for chains

            if i + 2 < len(words): #Appending word following word_pair
                chains[word_pair].append(words[i + 2])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    key = choice(chains.keys()) #Choosing random key from chains dict

    text = key[0] + " " + key[1] #Adding first word pair to text 

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
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
