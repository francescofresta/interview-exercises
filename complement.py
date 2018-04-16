''' Given two arrays of integers, return an array containing only the elements of the first array which does not belong to the second one. For exampe
 a = [2,1,3] b= [3,2], a-b = [1]
 * @author  Francesco Fresta
 * @version 1.0, 15th April 2018
 '''
firstArray = []
secondArray = []
complement = []
i = 0
j = 0
dimFirstArray = int(input("How many numbers should the first array cointain? "))
dimSecondArray = int(input("How many numbers should the second array cointain? "))
print("Seeding first array...\n")
for i in range(dimFirstArray):
    firstArray.append(int(input("Please insert an integer: \n")))
print("Seeding second array...\n")
for j in range(dimSecondArray):
    secondArray.append(int(input("Please insert an integer: \n")))
firstArray = list(set(firstArray))
secondArray = list(set(secondArray))
for number in firstArray:
    j = 0
    while(j<dimSecondArray):
        if (number == secondArray[j]):
            break
        else:
            j+=1
    if (j == dimSecondArray):
        complement.append(number)
print("The elements in the first array which does not belong to the second one are: ")
if (len(complement) == 0):
    print("Nothing.\n")
else:
    for number in complement:
        print("Number: ", number)
