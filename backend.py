import string
import random

def password_generator(password_length, use_symbols):

    if password_length < 4 or password_length > 50:
        return "Sorry! value must be between 4 and 50"
    
    random_password = string.ascii_letters + string.digits

    if use_symbols:
        random_password += string.punctuation
        return "".join(random.choices(random_password, k=password_length))
    
    else:
        return "".join(random.choices(random_password, k=password_length))