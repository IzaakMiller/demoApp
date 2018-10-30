#!/usr/bin/env python

#*******************************
# Izaak Miller
# CMPSC 300 Fall 2017
# Lab 5
# Date: 04 Oct, 2017

# Purpose: Comparing two different fasta files after some manipulation
# Honor code: The work submitted is my own unless cited otherwise
#*************************************

from Bio import SeqIO

#Function that compares two sequences and prints any differences
#and the position of the differences
def compare(seq1, seq2):
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            print "Position " + str(i+1) + " is not the same in both sequences"


#Getting files name and opening files
myFile_str = raw_input("Enter files to be compared: ")
myFile_split = myFile_str.split()
file1 = open(myFile_split[0])
file2 = open(myFile_split[1])


#for record in SeqIO.parse(my_file,'fasta'):
for record in SeqIO.parse(file1,'fasta'):
	id = record.id
	seq1 = record.seq

for record in SeqIO.parse(file2, 'fasta'):
    id = record.id
    seq2 = record.seq

file1.close()
file2.close()

#Comparing the two dna strings
print "Comparing the two DNA sequences: "
compare(seq1, seq2)

#Transcribing two DNA strings into RNA strings
print "\nComparing the two RNA sequences: "
RNAfromDNA_str1 = seq1.transcribe()
RNAfromDNA_str2 = seq2.transcribe()
compare(RNAfromDNA_str1, RNAfromDNA_str2)

#Translating the two RNA strings into Protein strings
print "\nComparing the two Proteins: "
PROTfromRNA_str1 = RNAfromDNA_str1.translate()
PROTfromRNA_str2 = RNAfromDNA_str2.translate()
compare(PROTfromRNA_str1, PROTfromRNA_str2)
