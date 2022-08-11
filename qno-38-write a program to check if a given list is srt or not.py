#Write a Python program to check if a given string contains an element, which ispresent in a list.
list=['.com', '.edu', '.tv']
string="https://www.w3resource.com/python-exercises/list/"
#Check if https://www.w3resou
i=0
while i<len(list):
    if list[i]in string:
        print("true")
    else:
        print("false")
    i+=1

