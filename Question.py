from random import shuffle
from json import load as loadJson


class Question():
	def __init__(self, prompt:str, answer:str, decoys:list[str]):
		self._prompt = prompt
		self._answer = answer
		self._decoys = decoys

		self._answerIndex = None

	def __str__(self) -> str:
		'''
		Question: <question>
			1. <answer1>
			2. <answer2>
			3. <answer3>
			...
		'''
		output = ''
		output += f'Question: {self._prompt}\n'

		# Creating a master options list
		options = [self._answer] + self._decoys
		shuffle(options)

		# Printing out each question
		for index, option in enumerate(options):
			output += f'    {index + 1}. {option}\n'

		# Tracking the index of our answer
		self._answerIndex = options.index(self._answer)

		return output

	def checkAnswer(self, guessIndex:int) -> bool:
		''' Check if the guess given matches the answer.

		This is expecting a zero-indexed value of options. I.e. first option would be index 0.

		Arguments:
			guessIndex(int): The value of the guess provided.

		Returns True if the guess matches the answer; False otherwise.
		'''
		return self._answerIndex == guessIndex

	def numberOfOptions(self) -> int:
		''' Returns the number of options given for this question.'''
		len(self._decoys + 1)


def collectQuestions():
	questionsDict = {}
	with open('questions.json', encoding='utf-8') as questionsFile:
		questionsDict = loadJson(questionsFile)

	questions = []
	for questionData in questionsDict:
		questions.append(Question(**questionData))

	return questions


if __name__ == '__main__':
	q1 = Question(
		prompt='Which of the following are an electric pokemon',
		answer='Pikachu',
		decoys=[
			'Whooper',
			'Eevee',
			'Bulbasaur',
		]
	)
	userAnswer = input(str(q1) + '  Answer: ')
	if q1.checkAnswer(int(userAnswer)-1):
		print('Good job!')
	else:
		print('oh, no. That\'s not right!')