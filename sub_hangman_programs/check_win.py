def check_win(secret_word, old_letters_guessed):
    list_secret_word = []
    currect_counter = 0
    list_secret_word[:0] = secret_word
    lenght = len(secret_word)
    for x in range(lenght):
        old_letters_guessed.append("_ ")
    for x in range(lenght):
        guess_letter = input("Enter the gueesed letter:\n")
        for y in range(lenght):
            if guess_letter in list_secret_word[y]:
              old_letters_guessed[y] = guess_letter
              currect_counter += 1
    if currect_counter == lenght:
        print(old_letters_guessed)
        print("True")
    else:
        print(old_letters_guessed)
        print("False")


def main():
    main_old_letters_guessed = []
    while(1):
        main_secret_word = input("Enter a word:\n")
        check_win(main_secret_word, main_old_letters_guessed)
main()