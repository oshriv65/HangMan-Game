HANGMAN_ASCII_ART = """ _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ ___
|  __  |/ _ '| '_  \/  _ | '_ ' _  \/ _' |  _  |
| |  | | (_| | | | |  (_|| | | | | | (_| | | | |
|_|  | |\__'_|_| |_|\_.  |_| |_| |_|\__'_|_| |_|
                   ___/  |
                  |_____/
"""
MAX_TRIES = 6
print(HANGMAN_ASCII_ART,MAX_TRIES)
guess_letter = input("Guess a letter:")
print(guess_letter)
