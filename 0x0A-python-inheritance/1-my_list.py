#!/usr/bin/python3
"""class inheriting class"""


class MyList(list):
    """inheritfrom list class"""

    def print_sorted(self):
        """print list in ascending order"""

        print(sorted(self))
