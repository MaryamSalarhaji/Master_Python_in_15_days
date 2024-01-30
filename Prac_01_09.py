# Create a program that takes a sentence as input and counts the number of words in it.
sentence = input("Enter a sentence:")
def count_num(sentence):
    count = 0
    words = sentence.split()
    for word in words:
        count = count + 1
    return "The number of words in the given sentence is:", count

print(count_num(sentence))
