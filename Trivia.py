# [X] Load in questions - json
# [ ] iterate our questions
# [ ] Check for invalid inputs
# [ ] Provide way to quit
# [ ] final score

from Question import collectQuestions
from random import shuffle
from time import sleep


def intput(message:str, errorMessage:str='Invalid value, please give a valid integer.'):
	# infinite loop to try and get input until it's valid
	while True:
		userInput = input(message)

		# Checking if valid input received
		if userInput.isdigit():
			break

		# If invalid input, print message and repeat
		print(errorMessage)
		sleep(.5)

	return int(userInput)


# Grabbing our list of questions and randomizing order
questions = collectQuestions()
shuffle(questions)

# Tracking variables
answersGiven = 0
answersCorrect = 0

print('''
████████╗██████╗░██╗██╗░░░██╗██╗░█████╗░
╚══██╔══╝██╔══██╗██║██║░░░██║██║██╔══██╗
░░░██║░░░██████╔╝██║╚██╗░██╔╝██║███████║
░░░██║░░░██╔══██╗██║░╚████╔╝░██║██╔══██║
░░░██║░░░██║░░██║██║░░╚██╔╝░░██║██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚═╝

Enter '0' at any time to quit.

Enter the maximum number of questions you would like to answer.''')
numberQuestions = intput('  : ')

# Iterating our questions
for index, question in enumerate(questions):
	# Checking if our max question count has been reached
	if index >= numberQuestions:
		break

	# Prompt user
	print(question)
	answer = intput(
		'  Response: ',
		'    ERROR: Invalid response, please enter the index of your guess.'
	)

	# Checking if user requested exit
	if answer <= 0:
		break # Exit for each question

	# Checking if user is correct
	correct = question.checkAnswer(answer-1)

	# Adding to our total
	answersGiven += 1
	if correct:
		answersCorrect += 1

	# User feedback
	if correct:
		print('That\'s correct, great job!')
	else:
		print('That\'s wrong, sorry!')
	sleep(1)
	print('\n\n')

# Print summary of trivia
print(f'You guessed {answersCorrect} questions correct out of {answersGiven} questions answered!')
accuracy = answersCorrect / answersGiven * 100
print(f'That\'s an accurracy of {accuracy:.0f}%')








