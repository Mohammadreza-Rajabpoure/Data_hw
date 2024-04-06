
import string

def Delel_english(text):
    
    english_letters = []
    letter =string.ascii_letters
    for i in letter:
        english_letters.append(i)


    for letter in text:
        if letter in english_letters:
            
            text =text.replace(letter , ' ')
    
    return text