import hazm

def Tokenizer(text):

    word_tokenizer = hazm.WordTokenizer()

    word_tokens = word_tokenizer.tokenize(text)

    return word_tokens

