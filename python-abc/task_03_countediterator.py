#!/usr/bin/env python3
"""
Module defining the CountedIterator class.
"""


class CountedIterator:
    """
    A custom iterator that wraps an iterable and counts how many items
    have been iterated over.
    """

    def __init__(self, some_iterable):
        """
        Initializes the iterator object and the counter.
        
        Args:
            some_iterable (iterable): The data to iterate over.
        """
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """
        Returns the current number of items that have been iterated over.
        """
        return self.counter

    def __next__(self):
        """
        Fetches the next item from the original iterator and increments
        the counter.
        
        Raises:
            StopIteration: If there are no more items left to iterate.
        """
        # Fetching the item first ensures that if StopIteration is raised,
        # the counter does not erroneously increment.
        item = next(self.iterator)
        self.counter += 1
        return item

    def __iter__(self):
        """
        Returns the iterator object itself. This is required for the object
        to be used in standard standard loops (e.g., 'for item in counted_iter:').
        """
        return self
