import math

class LogWriter(object):


	def __init__(self, list_data, head_text):
		#7
		pass

	@staticmethod
	def get_every_second_element(data):
		#1
		pass

	@staticmethod
	def avg_every_second_element(data):
		#2
		pass

	@staticmethod
	def insert_data_in_text(text, data):
		#3
		pass

	@staticmethod
	def count_o(text):
		#4
		pass

	def get_first_part(self):
		#5
		pass

	@staticmethod
	def what_is_added_the_meaning_of_life(add):
		#6
		pass

	@staticmethod
	def what_is_your_quest(quest="holy grail"):
		#8
		pass

	@staticmethod
	def get_second_word(text):
		#9
		pass

	def o_count_is_even(self):
		#10
		pass

	def get_movie_reference(self):
		#11
		pass

	@staticmethod
	def computation(x):
		#12
		pass

	def get_second_part(self, computation=None):
		#13
		pass

	def combining_method(self):
		#14
		pass

	def __str__(self):
		return self.combining_method()

if __name__=="__main__":
	head_text ="""
	Stil liist shilts list 1ist tilst iist l1ist? 'WHAT DID THE 0NE SNO0WMAN SAY TO THE OTHER SNOWMAN? 00O0O'
	"""
	list_data = [1,2,34,4]
	test_instance = LogWriter(list_data, head_text)
	print test_instance

#
#examplary output is below
#
"""

Stil liist shilts list 1ist tilst iist l1ist? 'WHAT DID THE 0NE SNO0WMAN SAY TO THE OTHER SNOWMAN? 00O0O'
_________
 After change: 

Stil liist shilts list ([1, 2, 34, 4]) 1ist tilst iist l1ist? 'WHAT DID THE 0NE SNO0WMAN SAY TO THE OTHER SNOWMAN? 00O0O'
0 O 0 O 0 O 0 O 0 O 0 O7.34846922835
To seek the holy grail
2218.4739851
"""

