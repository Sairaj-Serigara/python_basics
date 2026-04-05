import random
word=input("enter your word ")
letter="abcdefghijklmnopqrstuvwxyz"
lett=random.choice(letter)
lett1=random.choice(letter)
lett2=random.choice(letter)


le=random.choice(letter)
le1=random.choice(letter)
le2=random.choice(letter)


l=3
if len(word)>=3:
      new_word=word[1:len(word)]
      print(new_word)
      new_word=le+le1+le2+new_word+word[0]+lett+lett2+lett1
      print(new_word)

else:
    print(word[1]+word[0])
