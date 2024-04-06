import os
import string
import re

def Read_file():

    path = os.path.relpath('farsi_NLP_preprocecing/raw_persian_text.txt')

    with open (path , 'r' ) as f:
        raw_text = f.readlines()

    return raw_text 