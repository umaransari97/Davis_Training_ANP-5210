def validate_login(user, pwd):
    # Checking if both username and password match
    if user == "admin" and pwd == "1234":
        return "Login Successful"
    else:
        return "Login Failed"

# Input and Function Call
u_name = input("Enter username: ")
p_word = input("Enter password: ")
print(validate_login(u_name, p_word))