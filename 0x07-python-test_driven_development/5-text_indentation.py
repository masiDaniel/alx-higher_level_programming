#!/usr/bin/python3
"""print text with two lines"""


def text_indentation(text):
    """ prints text with 2 lines after '.', '?' and ':'
        
        Args:
            text(str): text to print
    """
    
    flag = 0

    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
            flag = 1
        else:
            if flag == 1:
                if text[i] == " " or text[i] == "   ":
                    continue
                else:
                    print(text[i], end="")
                    flag = 0
            else:
                print(text[i], end="")