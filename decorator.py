def password_required(func):
    def inner_func(*args, **kwargs):
        password = input("Enter the password ")
        if password == "1234":
            print("Access Given")
            return func(*args, **kwargs)
        else:
            print("Permission Denied !!")
    return inner_func
