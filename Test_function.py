#Function of observed substrings
def substring(string, k):
    #creates an empty dictionary
    sub_dict = {}
    #loops through the range of the indices of the string
    for i in range(len(string)- k + 1):
        #extracts the substring you want
        sub = string[i : i + k]
        #checks if the substring is in the dictionary 
        if sub in sub_dict:
            #updates the dictionary if theres a same substring and increments it by 1
            sub_dict[sub] += 1
        else:
            #creates a new pair when encountering it for the first time
            sub_dict[sub] = 1  
    #returns the new dictionary with all the substrings within it 
    return sub_dict

#Function of possible substrings
def substring_poss(string, k):
    #checks to see if k is greater than the length of the string
    if k > len(string):
        #if so it returns 0
        return 0
    #if k is less than or equal to the length of the string it initalizes
    #a possible to 0
    possible = 0
    #iterates over the range of the strings length
    for i in range(len(string)- k + 1):
        #increments it with 1
        possible += 1
    #returns the possiblities 
    return possible

def complexity(string,k):
    #Empty dicttionaries for the substrings
    observation = {}
    possiblities = {}
    #Iterate over the substring and half of it
    for i in range(1, len(string) // 2 + 1):
        #Calculates observed and possile substrings of len k
        obs_sub = substring(string, i)
        pos_sub = substring_poss(string, i)
        #adds a count to the dictionaries of the observed and possible substring length
        observation[i] = len(obs_sub)
        possiblities[i] = pos_sub
    #Calculates the total of observation and possiblities substring
    obs_total = sum(observation.values())
    poss_total = sum(possiblities.values())
    
    #Returns the ling complexity
    return obs_total/poss_total









import pytest
#from Python import substring, substring_poss, complexity

def test_substring():
    #Test Case 1
    assert substring("AAAAAA", 2) == {'AA': 5}
    #Test Case 2
    assert substring("ATGTCTGTCTGTA", 3) == {'ATG': 1, 'TGT': 3, 'GTC': 2, 'TCT': 2, 'CTG': 2, 'GTA': 1}

def test_substring_poss():
    #Test Case 1
    assert substring_poss("ATGTCTGTCTGTA", 2) == 12
    #Test Case 2
    assert substring_poss("AAAAAA", 2) == 5
    
def test_complexity():
    #Test Case 1
    assert complexity("AAAAAA", 1) == 0.2
    #Test Case 2
    assert complexity("ATGTCTGTCTGTA", 2) == 0.5396825396825397



import sys
import os

def main():
    # Check and retrieve command-line arguments
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)   # Return a non-zero value to indicate abnormal termination
    fileIn  = sys.argv[1]
    fileOut = sys.argv[2]

    # Verify source file
    if not os.path.isfile(fileIn):
        print("error: {} does not exist".format(fileIn))
        sys.exit(1)

    # Verify destination file
    if os.path.isfile(fileOut):
        print("{} exists. Override (y/n)?".format(fileOut))
        reply = input().strip().lower()
        if reply[0] != 'y':
           sys.exit(1)

    # Process the file line-by-line
    with open(fileIn, 'r') as fpIn, open(fileOut, 'w') as fpOut:
        lineNumber = 0
        for line in fpIn:
            lineNumber += 1
            line = line.rstrip()   # Strip trailing spaces and newline
            fpOut.write("{}: {}\n".format(lineNumber, line))
            # Need \n, which will be translated to platform-dependent newline
        print("Number of lines: {}\n".format(lineNumber))

if __name__ == '__main__':
    main()