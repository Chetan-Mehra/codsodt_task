# importing the random module  
import random  
  
# defining a function to randomly generate the password  
def password_generator(char_length, num_length, symbol_length):  
    '''''This function will randomly generate a password on the 
    basis of the number of characters, numbers, and symbols'''  
  
    # list of characters, numbers, and symbols  
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  
    nums = "0123456789"  
    symbols = "!@#$%^&*()"  
  
    # using the random.sample() method to return a list,  5
    
    # which we have to convert it into a string before  
    # returning it  
    selectedChars = random.sample(chars, char_length)  
    selectedNums = random.sample(nums, num_length)  
    selectedSymbols = random.sample(symbols, symbol_length)  
  
    # creating a list representing the password  
    password_list = selectedChars + selectedNums + selectedSymbols  
    # using the random.shuffle() method to shuffle the  
    # elements of the list so that the numbers, characters,  
    # and symbols get shuffled  
    random.shuffle(password_list)  
  
    # converting the list into string  
    password_str = "".join(password_list)  
  
    # returning the password string  
    return password_str  
  
# main function  
if __name__ == "__main__":  
    # asking the user to input the number of the characters, numbers, and symbols  
    char_length = int(input("Enter the Number of the Characters that you need in the password : "))  
    num_length = int(input("Enter the Number of the Numbers that you need in the password : "))  
    symbol_length = int(input("Enter the Number of the Symbols that you need in the password : "))  
  
    # calling the password_generator() function by passing the number of  
    # characters, numbers, and symbols as the required parameters  
    password = password_generator(char_length, num_length, symbol_length)  
  
    # printing the generated password for the users  
    print("The Randomly Generated Password is :", password) 