'''Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.'''

arr = [17,18,5,4,6,1]

length = len(arr)  
print(f'Length of arr {length}')   

for i in range(length):
    if i == length-1:
        arr[i] = -1
        print(arr)
    else:
        temp = max(arr[i+1:length])
        print(f'Choosen max in temp: {temp}')
        arr[i] = temp
            
print(arr)