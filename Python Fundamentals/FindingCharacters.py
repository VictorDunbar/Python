# Find a single character in the list of strings and prints a new set of strings containing that character.//
word_list = ['hello','world','my','name','is','Anna']
char = "n"

word_list1 = ["I", "feel", "it", "coming", "in", "the", "air", "tonight"]
char2 = "i"

def findChar(first, chr):
    new_list = []
    for text in first:
        if chr in text:
            new_list.append(text)
    print new_list

findChar(word_list1, char2)
findChar(word_list, char)
            
