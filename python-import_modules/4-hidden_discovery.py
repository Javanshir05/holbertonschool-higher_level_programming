#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all names in the module
    names = dir(hidden_4)
    
    # Sort and filter names that don't start with "__"
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
