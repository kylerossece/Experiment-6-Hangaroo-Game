# -*- coding: utf-8 -*-
def getAvailableLetters(lettersGuessed):
   import string
   Alphabet = string.ascii_lowercase
   for x in Alphabet:
    if x in str(lettersGuessed):
                Alphabet = Alphabet.replace(x,'')
   return Alphabet
             

