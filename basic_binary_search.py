print("\n")
print(10*"-","Binary Search Algorithm" ,10*"-")
print("\n")



def binarySearch(array, n):
    for i in range(len(array)):
        if array[i] == n:
            print(f'Element is present at index {array.index(array[i])}')


list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
number = int(input("Introduce a number to search it: "))

binarySearch(list_of_numbers, number)

print("\n")
