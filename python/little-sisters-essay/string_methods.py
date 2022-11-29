from ctypes import BigEndianStructure
from distutils.command import clean
from tkinter import N


def capitalize_title(title):
    return title.title()


def check_sentence_ending(sentence):
    """

    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.
    """

    if sentence[-1] == '.':
        return True
    else:
        return False

def clean_up_spacing(sentence):
    while sentence != '':
        return sentence.strip()



def replace_word_choice(sentence, old_word, new_word):
    
    return sentence.replace(old_word, new_word)

