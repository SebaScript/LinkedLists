from dataclasses import dataclass

@dataclass
class Node:
	value:int
	next = None
	def __repr__(self):
		return f"{self.value}->"

@dataclass
class SinglyLinkedList:
	head:Node = None
	tail:Node = None
	
	#add_at_tail
	def add(self, value):
		if(self.head):
			self.tail.next = Node(value)
			self.tail = self.tail.next
		else:
			new_node = Node(value)
			self.head = new_node
			self.tail = new_node

	def traverse(self, current=None, first=True):
		if(first):
			current = self.head
			first = False
		if(current):
			print(current, end = "")
			self.traverse(current.next, first)
		else:
			print() #salto de línea al final

	#recibe una lista y agrega uno a uno al final
	def create_from_list(self, value_list):
		for value in value_list:
			self.add(value)


def E1(list):
	ll = SinglyLinkedList()
	ll.create_from_list(list)
	suma = 0
	current = ll.head
	while current:
		if current.value == "*":
			while current.value == "*":
				current = current.next
			suma += current.value
		if current.next and current.next.value == "*":
			suma += current.value
		current = current.next
		print(suma)


listE1 = [1,2,25,2,"*",4,6,"*","*","*","*",9,914124124]
E1(listE1)


def E2(list):
	ll = SinglyLinkedList()
	ll.create_from_list(list)
	index = 0
	greater_index = -1
	count = 0
	greater_count = 0
	current = ll.head

	while current:
		index += 1
		for i in current.value:
			if i not in "aeiou":
				count += 1

		if count > greater_count:
			greater_count = count
			greater_index += index
			index = 0
			count = 0
		current = current.next

	c=0
	current_2 = ll.head
	while c != greater_index:
		current_2 = current_2.next
		c += 1
		
	current_2.value = current_2.value.upper()
	ll.head.value.upper()
			 
	print(greater_index)
	ll.traverse()


listE2 = ["hola", "comommmmmmmmsvvvvvvvvvvvvvvvv", "estas", "bien", "y", "tututututtttttttttttttt"]
E2(listE2)


def E3(l1, l2):
	ll1 = SinglyLinkedList()
	ll1.create_from_list(l1)
	ll2 = SinglyLinkedList()
	ll2.create_from_list(l2)
	result = SinglyLinkedList()
	dicc = {}
	current_ll1 = ll1.head
	current_ll2 = ll2.head
	while current_ll2:
		for i in range(current_ll2.value):
			current_ll1 = current_ll1.next
		dicc[current_ll2.value] = current_ll1.value
		current_ll2 = current_ll2.next
		current_ll1 = ll1.head
	print(dicc)

	for i in dicc.values():
		result.add(i)
	result.traverse()

listE31 = ["h", "o", "l", "a","p"]
listE32 = [4, 3, 1, 2, 0]
E3(listE31, listE32)