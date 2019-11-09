# Formatting Strings
# concept: https://www.youtube.com/watch?v=bQQqxysLIGE
# demo: https://www.youtube.com/watch?v=E850-MF22P0

# keyboard 
# we can use keyboard as an input to get informations or data (such as number or string) from users
first_name = input("What is your first name? ")
print('your first name is {}'.format(first_name))
last_name = input("What is your last name? ")
print('your last name is {}'.format(last_name))

your_full_name = first_name + last_name
print('Hello {}!'.format(your_full_name))

your_full_name = first_name.capitalize() + last_name.capitalize()
print('Hello {}!'.format(your_full_name))


