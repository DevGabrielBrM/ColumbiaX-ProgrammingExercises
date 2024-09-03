word = input("Type the word to check if it is a palindrom: ")
lower_word = word.lower()
word_cleared = lower_word.replace(" ","")
word_cleared = word_cleared.replace("'","")
word_cleared = word_cleared.replace("?","")
word_cleared = word_cleared.replace(",","")
word_backwards = word_cleared[::-1]
if word_backwards == word_cleared:
    print("Its' a Palindrom!\n=D")
else:
    print("It's not a Palindrom!\n=(")