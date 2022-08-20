from faker import Faker
from datetime import datetime
# def linear(arr,x):
#     for i in range(len(arr)):
#         if arr[i]==x:
#             return i
#     return -1

def binarySearch(array, x):
    low,high = 0,len(array)-1
    while low<= high:
        mid = (low +high)//2

        if array[mid]==x:
            return mid
        elif array[mid]< x:
            low = mid +1
        else:
            high = mid -1
    return -1

s= Faker()
lst = [s.name().split()[1] for i in range(1000)]

lst.sort()
print(lst)

x = input("\nKiriting: ")
t = datetime.now()

# result = linear(lst, x)
print(datetime.now()-t)
if result != -1:
    print("Topildi "+ str(result))
else:
    print("TOPILMADI")    



