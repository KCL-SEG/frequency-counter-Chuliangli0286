"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    frequencies = dict((i, items.count(i)) for i in set(items))

    return frequencies
