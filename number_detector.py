# Ask a user to enter a number, 'user _no'
# Make sure "user_no" is actuallly a number (Validation)
# If the number is positive (user_no >= 0), print 'True'
# Else, print "False"

user_no = input("Enter a number: ")
try:  # Validation  if input is valid
    user_no= float(user_no)
    print("Hooray, You entered a number.")
    
    if user_no >= 0:
        print('True')
        
        
    else:
        print('False')
    
except:
    #validation, if input is invalid
    print("This is not a number!!")
    
