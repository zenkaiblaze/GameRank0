def binary_search(list, item):
   low = 0
   high = len(list)-1
   while low <= high:
      mid = (low + high) // 2
      guess = list[mid]
      if guess == item:
         return mid
      if guess > item:
         high = mid - 1
      else:
         low = mid + 1
   return None
my_list = [1, 3, 5, 7, 9]
print (binary_search(my_list, 5))

def sum_elements(my_list):
   for i in range(len(my_list)):
       my_list[i]  = my_list[i] + 10 
   return my_list
elements = [1, 3, 5, 7, 9]
print(sum_elements(elements))

numbers = [1,-9,6,-5,1,-1,2,3,5,15,-4, 1]
#find average number of positive numbers 
def find_avg_from_pos(list):
   number = 0
   count = 0
   for num in list:
      if num > 0:
         number += num
         count += 1
   return number / count
print(find_avg_from_pos(numbers))

#Find average number of negative numbers
def find_avg_from_neg(list):
   number = 0
   count = 0
   for num in list:
      if num < 0:
         number += num
         count += 1 
   return number / count
print(find_avg_from_neg(numbers))

#Find biggest positive number
def find_big_pos(list):
   max_num = 0 
   for num in list:
      if num > 0 and num > max_num:
         max_num = num
   return max_num
print(find_big_pos(numbers))

#Find difference between biggest an smallest numbers
def find_diff(list):
   max_num = list[0]
   min_num = list[0]
   for num in list:
      if num > max_num:
         max_num = num
      if num < min_num:
         min_num = num
      
   return min_num - max_num 
print(find_diff(numbers))

#Find difference between biggest and average
def find_diff_big_avg(list):
   avg = 0
   for num in list:
      avg += num
   avg = avg / len(list)
   return max(list) - avg 
print(find_diff_big_avg(numbers))

#Find biggest number which is smaller than average
def find_big_small(list):
   big = list[0]
   avg = 0 
   for num in list:
      avg += num 
   avg = avg / len(list)
   for num in list:
      if num > big and num < avg:
         big = num
   return avg
print(find_big_small(numbers))
#Find biggest even number
def find_even(list):
   big = list[0]
   for num in list:
      if num %2 == 0:
         big = num
         break
   for num in list:
      if num %2 == 0 and num > big:
         big = num 
   return big 
print(find_even(numbers))

#Find biggest uneven number
def find_even(list):
   big = list[0]
   for num in list:
      if num %2 != 0:
         big = num 
   for num in list:
      if num %2 != 0 and num > big:
         big = num
   return big 
print(find_even(numbers))
#Bubble sort
def sort(list):
   for num in range(len(list) - 1):
      if list[num] > list[num + 1]:
         var = list[num]
         list[num] = list[num + 1]
         list[num + 1] = var
   for i in range(len(list) - 1):
      for num in range(len(list) - 1):
         if list[num] > list[num + 1]:
            var = list[num]
            list[num] = list[num + 1]
            list[num + 1] = var
   return list
print(sort(numbers))
   

#Insertion sort
def insertionSort(arr):
    n = len(arr)  # Get the length of the array
    
    if n <= 1:
       return  # If the array has 0 or 1 element, it is already sorted, so return
    
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
  
insertionSort(numbers)
print(numbers)







#Insertion sort


def insertion_sort(arr):
   n = len(arr)
   if n <= 1: 
      return
   for i in range(1, n):
      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
         arr[j+1] = arr[j]
         j-=1
      arr[j+1] = key
   return arr
print(insertion_sort(numbers))

#Selection sort

def selection_sort(arr):
   for i in range(0, len(arr) - 1):
      cur_min_idx = i 
      for j in range(i + 1, len(arr)):
         if arr[j] < arr[cur_min_idx]:
            cur_min_idx = j
      arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]
   return arr
print(selection_sort(numbers))

list1 = [1,2,5,7,9]
list2 = [3,4,8,10,11]

def reverse(arr):
   arr2 = []
   #while arr:
   for _ in range(len(arr)):
      a = arr.pop()
      arr2.append(a)
   return arr2
#print(reverse(list1))

def glue(arr:list, arr2:list):
   arr3 = []
   while arr and arr2:
      if arr[0] < arr2[0]:
         a = arr.pop(0)
         arr3.append(a)
      elif arr[0] > arr2[0]:
         a = arr2.pop(0)
         arr3.append(a)
   #for i in arr or arr2:
     # arr3.append(i)
   return arr3 + arr + arr2
print(f' lmao {glue(list1, list2)}')



def merge_arrays(arr1, arr2):
    return sorted(set(arr1+arr2))
print(merge_arrays(list1, list2))

def funk(n):
   if n==0:
      return 1
   if n%2 == 0:
      return n * funk(n-2)
   if n%2 != 0:
      return funk(n - 1)

print(funk(5))    # 4! = 4*3*2*1   # 3! = 3*2*1  1! = 1  0! = 1 

            # 4! = 4 * 2   6! = 6*4*2   5! = 4 * 2