#  NOW HERE ARE ALL THE COMMANDS THAT ARE USED FOR STRINGS . 

# 1.CHANGING THE CASE:-
#i)to uppercase/capital letters
name = "harshit"
print(name.upper()) # it will convert all the characters to uppercase/capital letters.
 
#ii)to lowercase/small letters
name = "HARSHIT"
print(name.lower()) # it will convert all the characters to lowercase/small letters 

#iii)to capitalize only the first letter of the string
name = "hrsht"
print(name.capitalize()) # it will capitalize the first letter of the name

#iv) to capitalize every first letter of every word
name = "Harshit Yadav"
print(name.title()) #it will capitalize the first letter of every word 

#v) converts string to lowercase in aggressive way  
text= "HELLO WROLD"
print(text.casefold()) # now it will convert all the letters into lowercase

#vi) to swap cases from capital to lower and vice versa
text = "hELLO wORLD"
print(text.swapcase()) # now this will swap the cases


#2.Finding out information about the string:-
#i) to find the number of letters in the string
text = "india is my country"
print(len(text)) # it will now find the number of letters in the string

# ii) to count how many times a specific letter is used in the string
text = "india is my country and i am an indian"
print(text.count("i")) # now it will count the number of i used in the string

# iii)Checking if the starting starts with a specific letter in a string
text = "india is my country"
print(text.startswith("i")) # now it will check if the string starts with i

# iv) checking if the strings ends with a specifc letter or not
text = "india is my country"
print(text.endswith("b")) # now it will check if the string ends with a b or not

# v) to find the the index of a substring
text = "hello world"
print(text.find("e")) # now it will find the index of e inn the string

# vi) to find the last index of a substring
text = "hello world"
print(text.rfind("o")) # now it will find the last index of o in the

#3. Modifying & cleaning the strings:-
#i) to replace a part of the string with something else
text = "i love rainy season"
print(text.replace("rainy","summer")) # now "rainy" will be replaced by "summer"

# ii) to remove empty space in the start and en of the string
text = " india is my country. "
print(text.strip()) # now it will remove the empyty spaces in start and end of the string

#iii)  to remove empty spaces from left only
text = "  hello world"
print(text.lstrip()) #now it will remove the empty spaces from the left end only

#iv) to remove empty space from the right end only
text = "hello world      "
print(text.rstrip()) # now it will remove all the empty space from the right end only

# v) to remove the prefix of the string
text = "TestName"
print(text.removeprefix("Test")) #  now it will remove the prefix from the code

# vi) to remove the suffix froom the the string
text = "TestName"
print(text.removesuffix("Name")) # now it i]will remove the suffix from the string

 
# 4.Checking and validation Methods:-
#i) to check if the string is alphanemuric or not
text = "hello 1234"
print(text.isalnum()) # now it will check if the string is alphanumerica or not

#ii) to check if the string is alphabets only
text = "hello world"
print(text.isalpha()) #now it will check if the string is alphabet only

#iii) to check if the string is a standard ASCII or not
text = "hello world"
print(text.isascii()) #now it will check if the string is a standard ASCII or not

#iv) to check if the given string is a decimal or not
text = "1234"
print(text.isdecimal()) # now it will check if the string is a decimal or not

#v) to check if all the characters in the string are a digit or not
text = "1234"
print(text.isdigit()) # now it will check if all the characters are digit or not

#vi) to check if the string is a valid python python variable or not
text = "my_variable"
print(text.isidentifier()) # now it will check if the string is a valid python variable or not  

#vii) to check if a string is a specific type or not just add a ".is" before what type you want to check for example if you want to check


#5.Splitting & Joining Methods:-
#i) to split the string into a list of words
text = "h,e,l,l,o"
print(text.split(",")) # now it will split the string into a list of words


#6.Padding & alignment Methods:-
#i) to center the string within a specified width using space
text = "hello"
print(text.center(20)) # now it will center the string within a specified width using space

#ii) to align the string to the left side within a specific width
text = "hello"
print(text.ljust(20)) # now it will align the string to the left side within
#same goes for the right side just use rjust instead of ljust

#iii) to pad a numerica string on the left  side with zeros wntil it reaches width
text = "123"
print(text.zfill(10)) # now it will pad a numerica string on the left


#7.Advanced & Formatting Methods:-
# i)to insert variables into {} inside a string
text = "my name is {} "
name = "harshit"
print(text.format(name)) # now it will insert the variable into {} inside a string
