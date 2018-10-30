#!/usr/bin/python

def dnaChecker(strand):
    stringLen = len(strand)
    count = 0
    for i in range(len(strand)):
        if "a" in strand[i] or "A" in strand[i]:
            count =+ count + 1
        elif "t" in strand[i] or "T" in strand[i]:
            count =+ count + 1
        elif "g" in strand[i] or "G" in strand[i]:
            count =+ count + 1
        elif "c" in strand[i] or "C" in strand[i]:
            count =+ count + 1
    if count == stringLen:
        return "Yes"
    else:
        return "No"

def rnaChecker(strand):
    stringLen = len(strand)
    count = 0
    for i in range(len(strand)):
        if "a" in strand[i] or "A" in strand[i]:
            count =+ count + 1
        elif "u" in strand[i] or "U" in strand[i]:
            count =+ count + 1
        elif "g" in strand[i] or "G" in strand[i]:
            count =+ count + 1
        elif "c" in strand[i] or "C" in strand[i]:
            count =+ count + 1
    if count == stringLen:
        return "Yes"
    else:
        return "No"

def proChecker(strand):
    stringLen = len(strand)
    count = 0
    for i in range(len(strand)):
        if "f" in strand[i] or "F" in strand[i]:
            count =+ count + 1
        elif "l" in strand[i] or "L" in strand[i]:
            count =+ count + 1
        elif "i" in strand[i] or "I" in strand[i]:
            count =+ count + 1
        elif "m" in strand[i] or "M" in strand[i]:
            count =+ count + 1
        elif "v" in strand[i] or "V" in strand[i]:
            count =+ count + 1
        elif "s" in strand[i] or "S" in strand[i]:
            count =+ count + 1
        elif "p" in strand[i] or "P" in strand[i]:
            count =+ count + 1
        elif "t" in strand[i] or "T" in strand[i]:
            count =+ count + 1
        elif "a" in strand[i] or "A" in strand[i]:
            count =+ count + 1
        elif "y" in strand[i] or "Y" in strand[i]:
            count =+ count + 1
        elif "h" in strand[i] or "H" in strand[i]:
            count =+ count + 1
        elif "q" in strand[i] or "Q" in strand[i]:
            count =+ count + 1
        elif "n" in strand[i] or "N" in strand[i]:
            count =+ count + 1
        elif "k" in strand[i] or "K" in strand[i]:
            count =+ count + 1
        elif "d" in strand[i] or "D" in strand[i]:
            count =+ count + 1
        elif "e" in strand[i] or "E" in strand[i]:
            count =+ count + 1
        elif "c" in strand[i] or "C" in strand[i]:
            count =+ count + 1
        elif "w" in strand[i] or "W" in strand[i]:
            count =+ count + 1
        elif "r" in strand[i] or "R" in strand[i]:
            count =+ count + 1
        elif "g" in strand[i] or "G" in strand[i]:
            count =+ count + 1
    if count == stringLen:
        return "Yes"
    else:
        return "No"

strand = raw_input("Enter a DNA, RNA or protein strand: ")
print "You entered: " + strand
print "Is this strand DNA?: " + dnaChecker(strand)
print "Is this strand RNA?: " + rnaChecker(strand)
print "Is this strand Protein?: " + proChecker(strand)
