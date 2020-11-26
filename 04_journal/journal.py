"""
This module implements the Journal.
"""

import os


def load(name):
    """
    This method creates and loads a new journal.
    :param name: This is the base name of the journal to load.
    :return: A new joural data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename, 'r') as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data

def save(name, journal_data):
    """
    This method saves the journal to disk
    param name: This is the base name of the new journal.
    param journal_data: This is the list of entries to save.
    """
    filename = get_full_pathname(name)
    print(f'..... saving to: {filename}')

    #fout = open(filename, 'w')
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')
    #fout.close()


def get_full_pathname(name):
    """
    This method returns the full path to Journal
    param name: This is the base name of the journal.
    """
    filename = os.path.abspath(os.path.join('./journals/', name + '.jrl'))
    return filename


def add_entry(text,journal_data):
    """
    This method adds an entry to the Journal.
    param text: This is the text of a new journal entry.
    param journal_data: is the journal data structure.
    """
    journal_data.append(text)
