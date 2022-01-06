# ~/Documents/words.txt
import os
import time
MAX_TRIES = 7
num_of_tries = 0
HANGMAN_ASCII_ART = """ _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ ___
|  __  |/ _ '| '_  \/  _ | '_ ' _  \/ _' |  _  |
| |  | | (_| | | | |  (_|| | | | | | (_| | | | |
|_|  | |\__'_|_| |_|\_.  |_| |_| |_|\__'_|_| |_|
                   ___/  |
                  |_____/
"""
HANGMAN_PHOTOS = {"pic0" : "x-------x", "pic1" : """x-------x
|
|
|
|
|""", "pic2" : """x-------x
|       |
|       0
|       
|       
|""", "pic3" : """x-------x
|       |
|       0
|       |
|
|""", "pic4" : """x-------x
|       |
|       0
|      /|\ 
|
|""", "pic5" : """x-------x
|       |
|       0
|      /|\ 
|      /
|""", "pic6" : """x-------x
|       |
|       0
|      /|\ 
|      / \ 
|"""}

def choose_word(file_path, index):
    index_counter = 0
    file = open(os.path.expanduser(file_path), 'r')
    file_data = file.read()
    list_words = file_data.split((" "))
    for word in list_words:
        num = list_words.count(word)
        if num >= 2:
            list_words.pop(index_counter)
        index_counter += 1
    while index > len(list_words):
        index -= len(list_words)
    secret_word_sub_main = list_words[index]
    return secret_word_sub_main

def  check_valid_input(letter_guessed, old_letters_guessed):
	letter_guessed = letter_guessed.lower() # We want to use lower letter in  the game.
	check = len(letter_guessed) # We check if the user type more than one letter.
	value = letter_guessed.isalpha() # We check if the input is alphabetic.
	if(check > 1):
		return("false")
		
	elif(value == 0):
		return("false")
	
	else:
		if(letter_guessed in old_letters_guessed):
			return("false")
		else:
			return("true")

def check_win(secret_word, old_letters_guessed):
    global MAX_TRIES
    global num_of_tries
    list_secret_word = []
    currect_counter = 0
    currect_flag = 0
    list_secret_word[:0] = secret_word
    lenght = len(secret_word)
    for x in range(lenght):
        old_letters_guessed.append("_ ")
    print("\nLets Start!\n")
    print(' '.join(old_letters_guessed) + '\n')
    while num_of_tries < 7:
        guess_letter = input("Enter the gueesed letter: ")
        check_letters = check_valid_input(guess_letter, old_letters_guessed)
        while check_letters == "false":
            print("The letter already guessed or is'nt  valid!\n")
            guess_letter = input("Enter the gueesed letter: ")
            check_letters = check_valid_input(guess_letter, old_letters_guessed)
        for y in range(lenght):
            if guess_letter in list_secret_word[y]:
                old_letters_guessed[y] = guess_letter
                print(' '.join(old_letters_guessed))
                currect_counter += 1
                currect_flag += 1
        if currect_flag == 0:
            print(":(")
            print(HANGMAN_PHOTOS["pic" + str(num_of_tries)])
            num_of_tries += 1
        elif currect_counter == lenght:
            print(old_letters_guessed)
            print("You WIN")
            break
        currect_flag = 0
    if num_of_tries == 7:
        print("\n")
        print(old_letters_guessed)
        print("\nYou LOSE")
        time.sleep(3)


def main():
    main_old_letters_guessed = []
    print(HANGMAN_ASCII_ART,MAX_TRIES,"\n\n© Created by Agronov Oshri ©")
    time.sleep(3)
    os.system('clear')
    file_dest = input("\nEnter the destenation to check: ")
    index_word = int(input("\nPlease enter an index: "))
    index_word -= 1
    secret_word = choose_word(file_dest, index_word)
    check_win(secret_word,main_old_letters_guessed)

    
main()
