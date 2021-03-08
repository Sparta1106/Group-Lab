
# Python code to reverse a string from user input  
 
  
# Function to reverse a string 
def reverse(string): 
    string = string[::-1] 
    return string 
  
string = input("Enter String: ")
  
print ("The original string  is : " + string )  
  
print ("The reversed string is : " + reverse(string))

