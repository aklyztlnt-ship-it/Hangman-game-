import string
alphabit1= string.ascii_lowercase
alphabit2=alphabit1.upper()
words =input("enter the sentence : ")
move=int(input("movement ? "))
#عمل وظيفه تشفير
def coding(words,move):
    cooded=""
    for letter in words:
        if letter in alphabit1:
            old_letter_index=alphabit1.index(letter)
            n_pos=(old_letter_index+move)%26
            new_letter=alphabit1[n_pos]
            cooded+=new_letter
        elif letter in alphabit2:
            old_letter_index=alphabit2.index(letter)
            n_pos=(old_letter_index+move)%26
            new_letter=alphabit2[n_pos]
            cooded+=new_letter
        else :
            cooded+=letter
             
    print(cooded)
coding(words,move)




