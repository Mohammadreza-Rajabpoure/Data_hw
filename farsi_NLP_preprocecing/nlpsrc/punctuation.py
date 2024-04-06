import string

def Punctuation_delet(text):

    punc_list = []
    for i in string.punctuation :
        punc_list.append(i)

    for letter in text:
        if letter in punc_list:
            text = text.replace(letter, ' ')

    return text
