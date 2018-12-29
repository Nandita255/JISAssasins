#4 Program to accept n numbers from user store these numbers into an array and sort these numbers of an array usimg function:
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
lst.sort()
print(lst)
