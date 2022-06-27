#!/usr/bin/env python

"""
Python miniscript for the ISM+D git workshop. Run by entering

  $ python helloworld.py

Author: Philipp Rosendahl, rosendahl@2phi.de
Date: 03/2021
"""

import sys


print('Hello ISMD.')
# but also add a comment up here.

# =======
# Write a random comment
# random comment
printstring = 'Hello world.'
print(printstring)

# Add a comment right here.

printstring = 'Bye world.'
print(printstring)

def dummyfunc():
    """This does nothign.
    """
    print("I do nothign.")

def wowsocool(blah):
    """This is a print function.

    Args:
        blah (string): pass the string you want to print
    """
    print(blah)

printstring = 'Good day madame.'
wowsocool(printstring)

print(sys.executable)
