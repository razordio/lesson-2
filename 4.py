text = input()
each_word = text.split()
for i, word in enumerate(each_word):
    print(i, word[:10])