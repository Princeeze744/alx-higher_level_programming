#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """print sorted list"""
        temp = self.copy()
        temp.sort()
        print(temp)
