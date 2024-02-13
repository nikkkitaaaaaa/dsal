size_array=int(input("Enter the size of array : "))
hash_table=[-1 for i in range(size_array)]



def user_input():
    for i in range(size_array):
        num=int(input("Eneter the element : "))
        quadratic_probe(mod(num),num)
        display_hash()

def mod(number):
    key=number%size_array
    return key

def linear_probe(keys,numbers):
    if hash_table[keys]==-1:
        hash_table[keys]=numbers
        
    else:
        for i in range(1,size_array):
            keys+=i
            keys=mod(keys)
             
            if hash_table[keys]==-1:
                hash_table[keys]=numbers
                break
            
def quadratic_probe(keys,numbers):
    if hash_table[keys]==-1:
        hash_table[keys]=numbers
    else:
        for i in range(1,size_array):
            keys+=i**2
            keys=mod(keys)
            if hash_table[keys]==-1:
                hash_table[keys]=numbers
                break



def display_hash():
    for i in range(size_array):
        print(i,"|",hash_table[i])
        
user_input()
