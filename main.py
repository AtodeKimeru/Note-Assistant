"""
Project: python & mysql:
- Open assistant
- Login or register
- if we choose register, we create a user in the database
- if we choose login, we identify ourselves and the program will ask us:
- Create note, show notes, delete notes 
"""
from users import actions

print("""
Available actions:
    - register
    - login
""")

do = actions.Actions()
action = input("What do you want to do?: ")

if action in "register":
    do.register()
    
elif action in "login":
    do.login()

else:
    print("Invalid action")
