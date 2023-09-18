import sys

def main(filename, args):
	#print(filename)
	#print(args)
	print('START ###################')

	count = 0
	if len(args) > 0:
		count = int(args[0])
	fibonacci = Fibonacci(count)
	fibonacci.out()

	print('DONE ####################')

class Fibonacci():

	__count = 0

	def __init__(self, count):
		self.__count = count

	def out(self):
		print('First %s Fibonacci numbers:' % self.__count)
		last = 0
		next = 1
		for x in range(0, (self.__count)):
			print(last)
			tempLast = last
			last = next
			next = tempLast + next

if __name__ == '__main__':
	main(__file__, sys.argv[1:])
