sentence=input("Enter a sentence: ")
values=[sentence]
for i in values:
    print(i)
def word_count(sentence):
    words=sentence.split()
    return len(words)
total_words=word_count(sentence)
print("Total number of words:", total_words)


number = int(input("Enter a number: "))
if number% 2 == 0:
    print("Even")
else:
    print("Odd")


