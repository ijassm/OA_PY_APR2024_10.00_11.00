##conditional statement

"""
switch = False

if switch == True:print("Lights ON")
else:print("Lights OFF")
"""


sys_user = "ocean"
sys_pass = "12345"

user_input = input("Enter your username: ")
pass_input = input("Enter your password: ")

if sys_user == user_input and sys_pass == pass_input:
    print("Logged in successfully☻")
else:print("invalid credentials")
