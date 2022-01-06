# ~/Documents/words.txt
import os
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
    secret_word = list_words[index]
    num_of_words = len(list_words)
    return (num_of_words, secret_word)

def main():
    file_dest = input("Enter the destenation to check: ")
    index_word = int(input("Please enter an index: "))
    index_word -= 1
    print(choose_word(file_dest, index_word))


main()