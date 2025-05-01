#Write a function to reverse each word in a given string.

str = "Mohammed Junaid shaikh"

print(str[::-1])   

 #Write a function to capitalize the first letter of each word in a string.

str = "junaid shaikh"

print(str.capitalize())

 #Write a function to extract only the digits from a given string.

text = "My name is Junaid"
words = text.split()  # Splits into ['My', 'name', 'is', 'Junaid']
print(words[3])  # Output: "Junaid"

str = "Moammed Junaid"

vowels = "aeiouAEIOU"

count = {i: str.count(i) 
for i in vowels 
if i in str}
print(count)

#palindeome
def is_palindrome(s):
    
    cleaned_str = ''.join(s.split()).lower()
    

    return cleaned_str == cleaned_str[::-1]

# Example usage:
print(is_palindrome("madam"))  # True
print(is_palindrome("word"))  # False

def count_words(s):
    
    words = s.split()
    
    return len(words)

print(count_words("my name is junaid shaikh"))  # 5
print(count_words("   i am from solapur  "))  # 4


#Write a function to convert a given string into title case (capitalize the first letter of each word).

str = 'junaid sha ikh'	
print(str.title())



 #Write a function to remove duplicate characters from a string.

lst = [1, 2, 3, 1, 2, 3, 4, 5]

print(list(set(lst))) 

#[1, 2, 3, 4, 5]

#create a decorator that modifies the return value of a function
def my_decor(func1):
    def wrapper(*args, **kwargs):
        print("function before")
        func1(*args, **kwargs)
        print("function after")
    return wrapper

@my_decor
def say_hello(name):
    print(f"hello, {name}")
say_hello("junaid")
'''function before
hello, junaid
function after'''

