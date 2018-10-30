#!/usr/bin/env python

#*******************************
# Izaak Miller
# CMPSC 300 Fall 2017
# Lab 4
# Date: 27 Sept, 2017

# Purpose: Reading, writing and couting the bases of FASTA files using the
# BioPython libraries
# Honor code: The work submitted is my own unless cited otherwise
#*************************************

#Function used to count the bases in the sequence ignoring cases
def basecounter(str_seq):
	numA = str_seq.count("A")
	numa = str_seq.count("a")
	numC = str_seq.count("C")
	numc = str_seq.count("c")
	numT = str_seq.count("T")
	numt = str_seq.count("t")
	numG = str_seq.count("G")
	numg = str_seq.count("g")
	print "Number of A's: ", numA + numa
	print "Number of C's: ", numC + numc
	print "Number of T's: ", numT + numt
	print "Number of G's: ", numG + numg

from Bio import SeqIO

#Getting file name and opening file
myFile_str = raw_input("Enter File :")
data_str = open(myFile_str)
data_str.close()

#my_file = open('Diabetes.fasta')
listt=[]

#for record in SeqIO.parse(my_file,'fasta'):
for record in SeqIO.parse(myFile_str,'fasta'):
	id = record.id
	seq = record.seq
	print 'Name: ', id
	print 'Size: ', len(seq)
	print "Counting bases"
	basecounter(seq)
	print 'Sequence: ', seq
	print

	if "tgc" in seq and "cgc" in seq:
		listt.append(record)
#myFile_str.close()

#Writing output as new file
outFileName_str = myFile_str + "_out.fasta"
outputFile_str = open(outFileName_str,"w")

SeqIO.write(listt, outputFile_str, "fasta")
outputFile_str.close()
