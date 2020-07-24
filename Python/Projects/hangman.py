import random
from string import ascii_lowercase

class HangmanGame:
    WORD_LIST = 'python', 'java', 'kotlin', 'javascript'

    def __init__(self):
        self.good_guessed, self.bad_guessed = str(), str()
        self.answer = random.choice(HangmanGame.WORD_LIST)
        self.lives = 8
    
    def start(self):
        print('\nH A N G M A N')

        while True:
            command = ''
            while command != 'play':
                command = input(
                    'Type "play" to play the game, "exit" to quit: '
                )
                if command == 'exit':
                    exit()

            while self.lives and set(self.good_guessed) != set(self.answer):
                print()
                for c in self.answer:
                    if c not in self.good_guessed:
                        print('-', end='')
                    else:
                        print(c, end='')
                print()

                guessing = input("Input a letter: ")

                # bad input
                if len(guessing) != 1:
                    print('You should input a single letter')
                elif guessing not in ascii_lowercase:
                    print('It is not an ASCII lowercase letter')
                # bad guessing
                elif guessing in self.good_guessed \
                    or guessing in self.bad_guessed \
                :
                    print('You already typed this letter')
                elif guessing not in self.answer:
                    print('No such letter in the word')
                    self.bad_guessed += guessing
                    self.lives -= 1
                # good guess
                else:
                    self.good_guessed += guessing

            if not self.lives:
                print('You are hanged!')
            else:
                print(f'\n{self.answer}')
                print('You guessed the word!')
                print('You survived!\n')

def main():
    hangman = HangmanGame()
    hangman.start()

if __name__ == "__main__":
    main()