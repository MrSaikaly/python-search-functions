
#creating search function using pthon 


#linear search

def linear_search(value_list, target): #O(n)
#looping on all list to check value
    for i in range(len(value_list)):
        if value_list[i]==target:
            return i
    return -1


#binary search

def binary_search(value_list,target):
    #creating the binary search

    low_index=0 #setting low index
    high_index=len(value_list)-1 # setting high index

    while(low_index<=high_index): #while loop
        mid =(low_index + high_index) //2 #setting middle index 

        if value_list[mid] == target : # we found our index
            return mid
        elif value_list[mid] > target: # if list value on index mid bigger than target move the high index 
            high_index= mid-1
        else:# else list value on index mid smaller than target move the low index 
            low_index=mid+1

    return -1

#binary search that return all results

def binary_search_first_index(value_list,target):
    #creating the binary search

    low_index=0 #setting low index
    high_index=len(value_list)-1 # setting high index
    first=-1

    while(low_index<=high_index): #while loop
        mid =(low_index + high_index) //2 #setting middle index 

        if value_list[mid] == target : # we found our index
            first= mid
            high_index=mid-1

        elif value_list[mid] > target: # if list value on index mid bigger than target move the high index 
            high_index= mid-1
        else:# else list value on index mid smaller than target move the low index 
            low_index=mid+1

    return first

def binary_search_last_index(value_list,target):
    #creating the binary search

    low_index=0 #setting low index
    high_index=len(value_list)-1 # setting high index
    last=-1

    while(low_index<=high_index): #while loop
        
        mid =(low_index + high_index) //2 #setting middle index 

        if value_list[mid] == target : # we found our index
            last= mid
            low_index=mid+1

        elif value_list[mid] > target: # if list value on index mid bigger than target move the high index 
            high_index= mid-1
        else:# else list value on index mid smaller than target move the low index 
            low_index=mid+1

    return last
#using the function

my_list=[100,20,30, 10,10,10 ,45,50,70]
my_list.sort()
print(my_list)

print("your target value:", 50, " is on index : ", linear_search(my_list,50))
print("your target value:", 10, " is on index : ", binary_search_first_index(my_list,10))
print("your target value:", 10, " is on index : ", binary_search_last_index(my_list,10))
