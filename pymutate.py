#!/usr/bin/python

import string
import random
import math
import sys
import argparse


# make a parser for some command line arguments
parser = argparse.ArgumentParser(description="A string mutation device for piped data")
parser.add_argument('--insert', action="store_true",
                   help="Insert a random character in a random location")
parser.add_argument('--delete', action="store_true",
                   help="Delete character in a random location")
parser.add_argument('--mutate', action="store_true",
                   help="Mutate a random character in a random location")
parser.add_argument('--crossover', action="store_true",
                   help="Cross two random characters")
parser.add_argument('--all', action="store_true",
                   help="Show results for all possible mutation types")
args = parser.parse_args()

#inputString = raw_input()
#inputString = "1234567890"
inputString = sys.stdin.read();

# Choose a random place within the string
def str_location(inputString):
	return random.randint(0, len(inputString)-1)

# generate a random character.  
def random_char():
	return chr(random.randint(0,254))

# Insertion
def insertion(inputString):
	loc = str_location(inputString)
	randomChar = random_char()
	return inputString[:loc] + randomChar + inputString[loc:]

# Mutation
def mutation(inputString):
	loc = str_location(inputString)
	randomChar = random_char()
	return inputString[:loc] + randomChar + inputString[loc+1:]

# Deletion
def deletion(inputString):
	loc = str_location(inputString)
	return inputString[:loc] + inputString[loc+1:]

# Crossover
def crossover(inputString):
	loc1 = str_location(inputString)
	loc2 = str_location(inputString)
	if (len(inputString) < 2):
		return inputString # no point in doing crossover
	while (loc1 == loc2):
		loc2 = str_location(inputString) # make sure we have different values
	if (loc1 > loc2):
		loc1, loc2 = loc2, loc1 #swap the values
	#print loc1, loc2
	crossedString = inputString[:loc1] + inputString[loc2] 
	#print crossedString
	crossedString += inputString[loc1+1:loc2] + inputString[loc1] + inputString[loc2+1:]
	#print crossedString
	return crossedString

finalString = inputString;
if (args.insert):
	finalString = insertion(inputString)
if (args.mutate):
	finalString = mutation(inputString)
if (args.delete):
	finalString = deletion(inputString)
if (args.crossover):
	finalString = crossover(inputString)
if (args.all):
	print "Original: " + inputString
	print "Insertion: " + insertion(inputString)
	print "Mutation: " + mutation(inputString)
	print "Deletion: " + deletion(inputString)
	print "Crossover: " + crossover(inputString)
	finalString = "That's all folks!"

if (finalString == inputString):
	# choose an operation at random
	choice = random.randint(0,3)
	if (choice == 0):
		finalString = insertion(inputString)
	elif (choice == 1):
		finalString = mutation(inputString)
	elif (choice == 2):
		finalString = deletion(inputString)
	else:
		finalString = crossover(inputString)

print finalString

