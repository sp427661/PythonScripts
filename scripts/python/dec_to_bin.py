# Function to print binary number for the  
# input decimal using recursion  
def decimalToBinary(n):  
  
    if(n > 1):  
        # divide with integral result  
        # (discard remainder)  
        decimalToBinary(n//2)  
  
      
    print(n%2, end=' ') 