import random
import re
#main functionality
def main():
    print("hello")
    #the user input of words
    sentence = input()
    rearrangeWords(sentence)

def uniqueShuffle(subStr):
    newShuffle = ''.join(random.sample(subStr, len(subStr)))
    if (len(subStr) > 3):
        while newShuffle == subStr:
            newShuffle = ''.join(random.sample(subStr, len(subStr)))
    return newShuffle
    

def rearrangeWord(word):
    if (len(word) != 1):
        subStr = word[1:len(word) - 1]
        counter = -1
        endCount = len(word) - 1
        end = ""
        while(word[counter] == "," or word[counter] == "." or word[counter] == "!" or not re.match(r'^\w+$', word[counter])):
            end += word[counter]
            counter -= 1
            endCount = counter
        alterWord = word[0] + uniqueShuffle(subStr[1: endCount]) + word[counter] + end
        return alterWord
    else:
        return word
    # for i in range(1,len(word)):
    #     print("unfinished")

def rearrangeWords(sentence):
    # newSentence = ""
    wordsList = sentence.split(" ")
    for word in wordsList:
        print(rearrangeWord(word))

if __name__ == "__main__":
    main()