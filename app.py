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

bill_amount = float(input("Enter the bill amount: "))
answer=input("What was the service quality (bad, okay, good, excellent):")

if answer == "bad":
        tip_percentage = 0
elif answer == "okay":
        tip_percentage = 0.15
elif answer == "good":
        tip_percentage = 0.20
elif answer == "excellent":
        tip_percentage = 0.25
print((bill_amount * tip_percentage)+bill_amount)

number=int(input("Enter a number: "))
factors=[]
for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)
print("The factors of", number, "are:", factors)


import math

number=int(input("Enter a number: "))
number2=int(input("Enter a second number: "))
for i in range (1, min(number, number2) + 1):
    if number % i == 0 and number2 % i == 0:
        gcf = i
print("The GCF of", number, "and", number2, "is:", gcf)