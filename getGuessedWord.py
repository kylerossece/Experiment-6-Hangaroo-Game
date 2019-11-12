def getGuessedWord(secretWord,lettersGuessed):
    for x in secretWord:
        if x not in str(lettersGuessed):
            secretWord=secretWord.replace(x,'_')
            return secretWord
