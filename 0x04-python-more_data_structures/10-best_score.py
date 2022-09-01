#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    if not a_dictionary:
        return None
    #  -----GETS THE LARGEST VALUE-------
    for key in a_dictionary:
        if a_dictionary[key] > best:
            best = a_dictionary[key]
    #  GETS THE KEY OF THE VALUE "BEST"---------
    for key in a_dictionary:
        if a_dictionary[key] == best:
            return key
