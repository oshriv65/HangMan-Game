def show_hidden_word(secret_word, old_letters_guessed):
    list_secret_word = []
    list_secret_word[:0] = secret_word
    lenght = len(secret_word)
    for x in range(lenght):
        old_letters_guessed.append("_ ")
    print(' '.join(old_letters_guessed))
    for x in range(lenght):
        guess_letter = input("Enter the gueesed letter:\n")
        for y in range(lenght):
            if guess_letter in list_secret_word[y]:
                old_letters_guessed[y] = guess_letter
        print('\n' + ' '.join(old_letters_guessed))
    return old_letters_guessed

def main():
    main_old_letters_guessed = []
    while(1):
        main_secret_word = input("Enter a word:\n")
        print(" ".join(show_hidden_word(main_secret_word, main_old_letters_guessed)))
        print("\n" + main_secret_word)
main()