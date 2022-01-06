def  try_update_letter_guessed(letter_guessed, old_letters_guessed):
#:The function check if the input of the user is valid to the game rules.
#:param letter_guessed: The input of the user
#:type letter_guessed: string
#:return: The result of the check
#:rtype: string
# I need to update this description.
	letter_guessed = letter_guessed.lower() # We want to use lower letter in  the game.
	check = len(letter_guessed) # We check if the user type more than one letter.
	value = letter_guessed.isalpha() # We check if0 the input is alphabetic.
	if(check > 1):
		return("false")
		
	elif(value == 0):
		return("false")
	
	else:
		if(letter_guessed in old_letters_guessed):
			return("false")
		else:
			return("true")
		
def main():
	old_letters_guessed = []
	while(1):
		guessed_letter = input("Guessed a letter: ")
		guessed_letter = guessed_letter.lower()
		check = try_update_letter_guessed(guessed_letter, old_letters_guessed)
		if("true" == check):
			old_letters_guessed.append(guessed_letter)
			old_letters_guessed.sort()
			print("True")
		else:
			print("X\n")
			print("->".join(old_letters_guessed))
			print("\nFalse")
main()
 