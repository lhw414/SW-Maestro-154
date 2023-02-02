# BJ 11721

sentence = input()

for i in range(len(sentence)//10 + 1):
    print(sentence[10*i:10*(i+1)])