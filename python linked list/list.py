class Node:
	def __init__(self, name, number):
		self.name = name
		self.number = number
		self.next = None
	def print_data(self):
		print(f"Name: {self.name}  Number: {self.number}")

class List:
	def __init__(self):
		self.first =None
		self.last = None

	def pushBack(self, name, number):
		pEl = Node(name, number)
		if(self.first == None):
			self.first = self.last = pEl
		else:
			self.last.next= pEl
			self.last = pEl

	def popFront(self):
		pEl	 = self.first
		if self.first == None:
			print("List is empty men!")
		else:
			first = pEl.next
			pEl = None

	def display_all(self):
		pEl	 = self.first
		if self.first == None:
			print("List is also empty men!")
		else:
			while pEl != None:
				pEl.print_data()
				pEl = pEl.next



one = Node("Jeffrey", 1)
list1 = List()

list1.pushBack("Jeffrey", 1)
list1.pushBack("Jennifer", 2)
list1.pushBack("Emmanuella", 3)
list1.pushBack("Treasure", 4)
# list1.first.print_data()

# list1.popFront()
# list1.first.print_data()
list1.display_all()
