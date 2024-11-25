'''Two dictionaries D1 and D2 can be merged to create a new dictionary D that has the following structure:

Each key-value pair in D is present either in D1 or D2.
Each key in D1 is also a key in D. Likewise, each key in D2 is also a key in D.

If a particular key is common to both D1 and D2, the value corresponding to this key in one of the two dictionaries is retained in D.

Write a function named merge that accepts the following arguments:

D1: first dictionary
D2: second dictionary
priority: The is a string variable that denotes the priority given to common keys while merging. That is, if both D1 and D2 have a key in common, then this variable will determine which value needs to be retained. More specifically, priority can take one of these two values:
"first": retain the value corresponding to the common key present in the first dictionary
"second": retain the value corresponding to the common key present in the second dictionary
You do not have to accept the input or print the output to the console. You just have to write the function definition.'''
def merge(D1, D2, priority):
    """
    Merge two dicts

    Arguments: 
        - D1: first dictionary
        - D2: second dictionary
        - priority: string
    Returns: D; merged dictionary
    """
    if priority == "first":
        # Start with D1, then update with unique keys from D2
        D = D1.copy()
        for key, value in D2.items():
            if key not in D:
                D[key] = value
    elif priority == "second":
        # Start with D2, then update with unique keys from D1
        D = D2.copy()
        for key, value in D1.items():
            if key not in D:
                D[key] = value
    return D