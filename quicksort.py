import sys

def main(filename, args):
	stack = [] #Implementation is iterative, so keep track of positions in arr that need sorting
	arr = [123,10,43534,678,7897,8713,2314,1,3,56754,5,876,6786,3532,8,2315,6585,43634,2,7,4,9,6,12,875,234,879,11,90]
	stack.append((0, len(arr) - 1)) #Let's begin sorting our arr - so add our first iteration positions
	print("%s %s" % (arr, 'BEGIN...'))
	quicksort(arr, stack)
	print("%s %s" % (arr, 'DONE!'))

def quicksort(arr, stack):
	while(len(stack) > 0):
		positions = stack.pop()
		left = positions[0]
		right = positions[1]
		print("found positions %s, %s in stack" % (left, right))
		index = partition(arr, left, right)
		print("current index is %s" % (index))
		print("current arr is %s" % (arr))
		if (left < index - 1):
			stack.append((left, index - 1))
		if (index < right):
			stack.append((index, right))

def partition(arr, left, right):
	i = left
	j = right
	tmp = None
	pivot = arr[(left + right) / 2]
	print("current pivot is %s" % (pivot))
	while (i <= j):
		while (arr[i] < pivot):
			i+=1;
		while (arr[j] > pivot):
			j-=1;
		if (i <= j):
			swap(arr, i, j)
			i+=1;
			j-=1;
	return i


def swap(arr, i, j):
	print("swapping %s with %s" % (arr[i], arr[j]))
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

if __name__ == '__main__':
	main(__file__, sys.argv[1:])
