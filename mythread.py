# Threads concept

"""
def print_odd_numbers():
	for odd_number in range(1, 10, 2):
		print(odd_number)
		
def print_even_numbers():
	for even_number in range(2, 11, 2):
		print(even_number)

print_odd_numbers()
print_even_numbers() 
"""

import threading

def print_odd_numbers():
	for odd_number in range(1, 10, 2):
		print(odd_number)
		
def print_even_numbers():
	for even_number in range(2, 11, 2):
		print(even_number)

odd_thread = threading.Thread(target = print_odd_numbers).start()
even_thread = threading.Thread(target = print_even_numbers).start()
print("Making a change")
