# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.
from twisted.python.zipstream import countFileChunks
from Foundation import MAX

def freq_analysis(message):
    maxLetters = 26 # 26 letters from a to z
    freq_list = countFreq(maxLetters)
    freq_list = calcFreq(freq_list, message)
    freq_list = normalize(freq_list, message, maxLetters)
    return freq_list


def countFreq(maxN):
    letters = []
    i = 0 # index to be incremented 
    
    while i < maxN: 
        letters += [0]
        i += 1
        
    return letters


def calcFreq(list, msg):
    # switch to test letter & add 1 if letter is present
    for char in msg: 
        if char == 'a': 
            list[0] += 1 
        if char == 'b':
            list[1] += 1
        if char == 'c':
            list[2] += 1
        if char == 'd':
            list[3] += 1
        if char == 'e':
            list[4] += 1
        if char == 'f':
            list[5] += 1
        if char == 'g':
            list[6] += 1
        if char == 'h':
            list[7] += 1
        if char == 'i':
            list[8] += 1
        if char == 'j':
            list[9] += 1
        if char == 'k':
            list[10] += 1
        if char == 'l':
            list[11] += 1
        if char == 'm':
            list[12] += 1
        if char == 'n':
            list[13] += 1
        if char == 'o':
            list[14] += 1
        if char == 'p':
            list[15] += 1
        if char == 'q':
            list[16] += 1
        if char == 'r':
            list[17] += 1
        if char == 's':
            list[18] += 1
        if char == 't':
            list[19] += 1
        if char == 'u':
            list[20] += 1
        if char == 'v':
            list[21] += 1
        if char == 'w':
            list[22] += 1
        if char == 'x':
            list[23] += 1
        if char == 'y':
            list[24] += 1
        if char == 'z':
            list[25] += 1
        
    return list

def normalize(list, msg, maxN):
    numChar = len(msg)
    i = 0
    while i < maxN:
        list[i] = float(list[i]) / numChar
        i += 1
    return list


#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
