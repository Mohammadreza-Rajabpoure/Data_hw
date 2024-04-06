from nlpsrc.delet_english import Delel_english
from nlpsrc.file_reader import Read_file
from nlpsrc.normalize import Normalize
from nlpsrc.punctuation import Punctuation_delet
from nlpsrc.tokenizer import Tokenizer
import hazm
def main():

    raw_text = Read_file()
    just_farsi = Delel_english(raw_text)
    text = Punctuation_delet(just_farsi)
    normalized_text  = Normalize(text)
    tokenized_text = Tokenizer(normalized_text)
    return tokenized_text

