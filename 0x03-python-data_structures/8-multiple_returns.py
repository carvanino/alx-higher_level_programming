#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0:1]
    if sentence == "":
        return (length, None)
    return(length, first)
