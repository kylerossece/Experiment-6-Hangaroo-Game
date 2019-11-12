def Hangaroo(secretWord):
 lettersGuessed=['']
 numberofguess=0
 while not isWordGuessed(secretWord, lettersGuessed):
     print('Number of wrong inputs:' , numberofguess)
     print('Missing letters:', getGuessedWord(secretWord, lettersGuessed))
     guess=input("Enter a letter:")
     guessinlowercase = guess.lower()
     if guessinlowercase not in lettersGuessed:
       lettersGuessed.append(guessinlowercase)
       if guessinlowercase not in secretWord:
         numberofguess += 1
         if numberofguess==6:
          return('No more available guesses :( ')
          if numberofguess==6:
             return('The correct answer is' , secretWord)
     else:
               print('You have already guessed that letter')
 return print('Secret Word:', getGuessedWord(secretWord, lettersGuessed), '|You have got the correct Word!!!|')
