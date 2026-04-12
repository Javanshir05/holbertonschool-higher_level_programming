#!/usr/bin/env python3
"""
Module defining a VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications when items are
    added or removed from the list.
    """

    def append(self, item):
        """
        Appends an item to the list and prints a notification.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Extends the list with an iterable and prints a notification.
        """
        items_count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(items_count))

    def remove(self, item):
        """
        Removes an item from the list and prints a notification.
        Handles the edge case where the item is not in the list.
        """
        if item not in self:
            # Let the built-in list raise the standard ValueError
            super().remove(item)
            return

        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an item from the list at a given index and prints a notification.
        Defaults to the last item if no index is provided.
        """
        # Access the item first. If the index is out of bounds or the list 
        # is empty, this naturally raises an IndexError BEFORE printing.
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
