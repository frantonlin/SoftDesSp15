""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import re

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    f = open(file_name,'r')
    lines = f.readlines()
    start_line = 0
    while lines[start_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        start_line += 1
    end_line = start_line
    while lines[end_line].find('END OF THIS PROJECT GUTENBERG EBOOK CANDIDE') == -1:
    	end_line +=1

    lines = lines[start_line+1:end_line-1]

    words = []
    for line in lines:
        words = words + [word.lower() for word in re.findall("\w+'?\w*", line, re.UNICODE)]

    return words

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequently occurring
    """
    freq = {}
    for word in word_list:
        freq[word] = freq.get(word, 0) + 1

    sort_list = [(k, v) for k, v in freq.iteritems()]
    sort_list.sort(key=lambda tup: tup[1], reverse = True)
    return [pair[0] for pair in sort_list[:n]]

print get_top_n_words(get_word_list('pg19942.txt'), 100)
