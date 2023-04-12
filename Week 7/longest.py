with open("file.txt",'r')as f:
    list_words=f.readlines()
    longest_word=list_words[0]
    for word in list_words:
        if len(word)>len(longest_word):
            longest_word=word

print(longest_word)
