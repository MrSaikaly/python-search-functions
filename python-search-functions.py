
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
        elif value_list[mid] > target:
            high_index= mid-1
        else:
            low_index=mid+1

    return -1

    print()


#using the function

my_list=[10,20,30,45,50,70]

print("your target value:", 50, " is on index :_", linear_search(my_list,51000))
print("your target value:", 50, " is on index :_", binary_search(my_list,10))