'''
Given an array of integers, return the second biggest value. For example if we have the following array
[1,4,0,9,3]
The function should return
4
Because 9 is the maximum value while 4 is the second one
 * @author  Francesco Fresta
 * @version 1.0, 16th April 2018
'''
def secondMax():
	numbers = []
	dim = 0
	while(dim<=0):
		dim = int(input("How many numbers would you like to insert? "))
	for i in range(dim):
		numbers.append(int(input("Please insert an integer: "))) #seeding array
	numbers = list(set(numbers)) #trick used to remove duplicates because set automatically excludes them
	numbers.sort()
	dim = len(numbers)
	return numbers[dim-2]
print ("The second biggest value is", secondMax())
