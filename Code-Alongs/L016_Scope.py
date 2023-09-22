# In Python we have 2 types of Scope, (life-time of a variable).
# Local scope: Only available localy in a function.
# Global scope: Available through execution of program.

name = "Sebastian"

def main():
    global name
    name = "Kalle"
    print(name)

print(name)
main()
print(name)

## Python doesn't have block scope, but this is used in most other languages, such as C#, C++, Java
# if name =="Sebastian":
#     last_name = "Fredin"

# print(last_name)

# for i in range(3):
#     print(i)
    
# print(f"i = {i}")