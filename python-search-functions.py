
#creating search function using pthon 


#linear search

def linear_search(value_list, target): #O(n)
#looping on all list to check value
    for i in range(len(value_list)):
        if value_list[i]==target:
            return i
    return -1



#using the function

my_list=[10,20,30,45,50,70]

print("your target value:", 50, " is on index :_", linear_search(my_list,50))