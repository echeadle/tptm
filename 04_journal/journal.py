import os

def load(name):
    # todo: populate from file if it exists.
    return []

def save(name, journal_data):
    filename = os.path.abspath(os.path.join('./journals/', name + '.jrl'))
    print(f'would load from: {filename}')
    #fout = open(filename, 'w')


def add_entry(text,journal_data):
    journal_data.append(text)