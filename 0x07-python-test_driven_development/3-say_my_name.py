#!/ur/bin/python3
"""function to print name """


def say_my_name(first_name, last_name=""):
    """
    print out the  full name
    Args:
        first_name(str): first name
        last_name(str): last name
    """

    if type(first_name) is not str:
        raise TypeError("first_name mut be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
