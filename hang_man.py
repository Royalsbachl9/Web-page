import random

# A list of words that
potential_words = ["lion", "code", "loop", "gene"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = [] # TIP: the number of letters should match the word
for i in word:
    current_word.append("_")

# Some useful variables
guesses = []
maxfails = 7
fails = 0
wordtoguess = []



while fails < maxfails:
    print("-------------------")
    print ("Lives Left:", maxfail - fail)
	guess = input("Guess a letter:")
    if guess in word:
        current_word[] = guess
# print(______________________________)

    for i in range(4):

	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")

    if(guess in word):
        print ("you got a letter!")

        if "_"









# word = "lion"
# list = ["_", "_", "_", "_" ]
