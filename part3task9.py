string = str(input("Enter: "))
print(string)
l = string.split(" ")
# l = string
result = l[::-1]
print(result) 
result = ' '.join(result)
print(result)
