class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass


def check_age(age):
     if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
     else:
        print("Access granted")

try:
    check_age(10)
except InvalidAgeError as e:
    print(e)
  
