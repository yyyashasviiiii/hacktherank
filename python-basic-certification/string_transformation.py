"""
Problem: Transform Sentence

Description:
Given a sentence, you need to transform each word by changing the case of each character based 
on the character that came before it.

Rules:
- If the current character comes after the previous character (lexicographically), convert it to UPPERCASE.
- If it comes before, convert it to lowercase.
- If it's the same, keep it unchanged.

Function Signature:
def transformSentence(sentence: str) -> str

Parameters:
- sentence (str): A sentence consisting of one or more words separated by spaces.

Returns:
- str: The transformed sentence, preserving word spacing.

Input Format:
A single line string containing space-separated words.

Output Format:
A single string containing the transformed sentence.

Sample Input:
cool dog

Sample Output:
cOOL doG

Explanation:
In the word 'cool', each character is compared to the one before it:
 - 'o' > 'c' → uppercase 'O'
 - 'o' == 'o' → stays 'o'
 - 'l' > 'o' → uppercase 'L'
In 'dog':
 - 'o' > 'd' → uppercase 'O'
 - 'g' > 'o' → uppercase 'G'
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def transformSentence(sentence):
    words = sentence.split()
    result = []
    
    for word in words:
        new_word = word[0]
        for i in range(1, len(word)):
            if word[i - 1].lower() < word[i].lower():
                new_word = new_word + word[i].upper()
            elif word[i-1].lower() > word[i].lower():
                new_word = new_word + word[i].lower()
            else:
                new_word = new_word + word[i]
        result.append(new_word)
    return " ".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()