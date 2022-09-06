#task 1
# def mydivision():
#     x = int(input("Type the numerator:"))
#     y = int(input("Type the denominator:"))
#     if y == 0:
#         print("No division by O, type the arguments again")
#     else:
#         print(f"{x} divided by {y} is {x/y}")
# mydivision()

#task 2
# def yellowpages():
#     lname = input("Type a person's last name ")
#     fname = input("Type the person's first name ")
#     yob = input("Type the person's year of birth ")
#     city = input("Type their city of residence ")
#     email = input("Now, type their email ")
#     tel = input("Lastly, type their telephone number ")
#     print(f"Personal info: {fname} {lname}, born in {yob}, resides in {city}. Their e-mail is {email}, and their telephone number is {tel}")
# yellowpages()

#task 3 for any number of elements
def my_func(x, y, z):
    l = list(input("Type x, y and z, separated by spaces"))
    n = 0
    while n < len(l):
        if l[n] > l[n+1]:
            y = l[n]
            break
        else:
            y = l[n+1]
            n = n + 1
    l.remove(y)
    while n < len(l):
        if l[n] > l[n + 1]:
            y1 = l[n]
            break
        else:
            y1 = l[n + 1]
            n = n + 1
    return y + y1
print(f"The sum of the two largest numbers in your input, {y} and {y1}, is {my_func}")











