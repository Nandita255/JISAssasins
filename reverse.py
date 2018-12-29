#Q.12 write  program to accept  a sentence from the user and reverse its each word.
msg=input("enter the string")
words=msg.split(" ")
words.reverse()
print(' '.join(words))