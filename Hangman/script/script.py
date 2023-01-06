#Author : Redoxymine
#Git : https://github.com/Redoxymine/

#HANGMAN GAME - SCRIPT

import random

WORD_LIST = ["BOOK","PENCIL","RUSSIA","UNITED_STATES","BOTTLE","PHONE",
            "TABLE","APPLE","HAT","AUSTRALIA","COMPUTER","LAMP"]

WORD = random.choice(WORD_LIST)

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

class Game():
    #Game Class

    def __init__(self,guess_word):
        self.guess_word = guess_word
        self.failed_attempts = 0
        self.progress = list(len(self.guess_word)*'_')
    
    def game_status(self):
        print("\n")
        print("\n".join(HANGMAN[:self.failed_attempts]),"\n")
        print("\n")
        print(" ".join(self.progress))
        print("\n")

    def update_progress(self,indexes,letter):
        #This method will update the game progress

        for self.index in indexes:
            self.progress[self.index] = letter

    def get_user_input(self):
        #We are getting user input

        user_input = input(" [H] What's your guess : ")
        user_input = user_input.upper()
        return user_input

    def find_indexes(self,letter):
        #We will break the word into letters
        return [i for i,char in enumerate(self.guess_word) if char==letter]
    
    def is_invalid_letter(self,user_input):
        return user_input.isdigit() or (user_input.isalpha() and len(user_input) > 1)
    
    def play(self):
        #Playing game

        while self.failed_attempts <= len(HANGMAN):
            self.game_status()
            self.user_input = self.get_user_input()

            if self.user_input in self.guess_word:
                self.indexes = self.find_indexes(self.user_input)    
                self.update_progress(self.indexes,self.user_input)

                #When it's done
                if self.progress.count('_') == 0:
                    print(" [H] YOU WON!")  
                    print(f" [H] The word is {self.guess_word}")           
                    quit()

            if self.user_input in self.progress:
                print(" [H] It's already in")
                continue

            if self.is_invalid_letter(self.user_input):
                print(" [H] It's not a letter")
                continue
            else:
                self.failed_attempts += 1
