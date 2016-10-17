import math

class LogWriter(object):


	def __init__(self, list_data, head_text):
		#7
		self.list_data = list_data
		self.head_text = head_text
		self.o_count = None
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
		index = text.find('list') + 4
		text = text[:index] +' (' +str(data)+ ') ' + text[index:]
		return text
		pass

	@staticmethod
	def count_o(text):
		#4
		return text.count('o') + text.count('O')

	def get_first_part(self):
		self.head_text=self.head_text+"_________\n After change: \n"
		tmp=self.head_text
		tmp=tmp+self.insert_data_in_text(self.head_text,self.list_data)
		tmp=tmp+str(self.count_o(self.head_text))
		return tmp

	@staticmethod
	def what_is_added_the_meaning_of_life(add):
		#6
		pass

	@staticmethod
	def what_is_your_quest(quest="holy grail"):
		#8
		if quest=="holy grail":
			return "To seek the holy grail"
		else:
			return "To seek the " + quest
		pass

	@staticmethod
	def get_second_word(text):
		#9
		pass

	def o_count_is_even(self):
		#10
		pass

	def get_movie_reference(self):
		is_even=o_count_is_even(self.o_count)
		if is_even:
		  return what_is_added_the_meaning_of_life(self.o_count)
		if not is_even:
		  words = string.split(self.head_text)
		  return what_is_your_quest(words[1])
		if self.o_count>7:
		  self.head_text.append(" ")
		  return what_is_your_quest()
		  

	@staticmethod
	def computation(x):
		#12
		return x**2 + math.sqrt(x) + math.sqrt(math.sqrt(x))

	def get_second_part(self, computation=None):
		#13
		pass

	def combining_method(self):
		#14
		return str(self.get_first_part()) + "0 O 0 O 0 O 0 O 0 O 0 O" + str(self.computation(self.get_second_part()))
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

