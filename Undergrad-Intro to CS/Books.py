#  File: Books.py

#  Description: When the user enters two book files, finds the unique word frequency.


#  Student Name: Michell Li, Ali Prasla


#  Student UT EID: ml42322, anp2429


#  Course Name: CS 303E


#  Unique Number: 50865


#  Date Created: April 25, 2016


#  Date Last Modified: April 28, 2016


# Create word dictionary from the comprehensive word list 
word_dict = {'a':1}
def create_word_dict ():
 # open file for reading
    in_file = open ("words.txt", "r")
    

    for line in in_file:
        line = line.strip()
        line = line.lower()
        word_dict[line] = 1
    
    in_file.close()
    return word_dict



# Removes punctuation marks from a string

def parseString (st):

    s = ''
 
    for ch in st:
        if ch == "'":
            s += ch
            continue
        if ch.isalpha():
            s += ch
        else:
            s += ' '


    
    return s



# Returns a dictionary of words and their frequencies
def getWordFreq (file,dict):
    freq_dict = {}
    word_set = set()
    cap_words = []
    word_list = []
    count = 0
    for line in file:
        line = line.strip()
        line = parseString(line)
        line = line.split()
        for i in range(len(line)):
            
            if line[i] == 'protégé':
                line = line.remove('protégé')
                continue
            
            # put capital words on separate list
            if line[i][0] >= 'A' and line[i][0] <= 'Z':
                line[i] = line[i].lower()
                cap_words.append(line[i])
                continue
            
            #get rid of apostrophes
            if line[i][-1] == "'":
                line[i] = line[i][:-1]

            if  line[i][-2:]== "'s":
                line[i] = line[i][:-2]
   
   
            #add the word to the set
            word_set.add(line[i])
            count += 1



            if line[i] in freq_dict:
                freq_dict[line[i]] = freq_dict[line[i]] + 1
            else:
                freq_dict[line[i]] = 1
                    #freq_dict = sorted(freq_dict)             
    #proper noun?
    for i in range(len(cap_words)):
        for key in word_dict:
            if cap_words[i] == key:
                if cap_words[i] in freq_dict:
                    freq_dict[cap_words[i]] = freq_dict[cap_words[i]] + 1
                    count += 1
                else:
                    freq_dict[cap_words[i]] = 1
                    count += 1

    

    return freq_dict


# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
    #print author 1 information
    print(str(author1))
    #calculate total distinct words
    distinct1 = len(freq1)
    print("Total Distinct Words = " + str(distinct1))
    #calculate total words
    total1 = sum(freq1.values())
    print("Total words (including duplicates) = " + str(total1))
    #calculate ratio
    print("Ratio (% of total distinct words to total words) = " + str((distinct1 / total1)*100))
    print()
    #author 2 information
    #calculate total distinct words
    print(str(author2))
    distinct2 = len(freq2)
    print("Total Distinct Words = " + str(distinct2))
    #calculate total words
    total2 = sum(freq2.values())
    print("Total words (including duplicates) = " + str(total2))
    print("Ratio (% of total distinct words to total words) = " + str((distinct2 / total2)*100))
    print()
    #start actual comparisons
    set1 = set(freq1)
    set2 = set(freq2)
    print(author1 + " used " + str(len(set1 - set2)) +  ' words that ' + author2 + ' did not use.') 
    print("Relative frequency of words used by " +author1 + " not in common with " + author2 + " = " + str(((len(set1 - set2))/total1)*100))
    print()
    print(author2 + " used " + str(len(set2 - set1)) +  ' words that ' + author1 + ' did not use.')
    print("Relative frequency of words used by " +author2 + " not in common with " + author1 + " = " + str(((len(set2 - set1))/total2)*100))
    print()

def main():
  # Create word dictionary from comprehensive word list

    create_word_dict()


  # Enter names of the two books in electronic form
    book1 = input ("Enter name of first book: ")
    book2 = input ("Enter name of second book: ")
    print()
  
    book1 = open(book1, "r")
    book2 = open(book2, "r")

  # Enter names of the two authors
    author1 = input ("Enter last name of first author: ")
    author2 = input ("Enter last name of second author: ")
    print()
  


# Get the frequency of words used by the two authors
    wordFreq1 = getWordFreq (book1, word_dict)
    wordFreq2 = getWordFreq (book2,word_dict)



  # Compare the relative frequency of uncommon words used
  # by the two authors
    wordComparison (author1, wordFreq1, author2, wordFreq2)





main()


