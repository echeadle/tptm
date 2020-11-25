import os

def load(name):
    # todo: populate from file if it exists.
    return []

def save(name, journal_data):
    filename = os.path.abspath(os.path.join('./journals/', name + '.jrl'))
    print(f'..... saving to: {filename}')

    fout = open(filename, 'w')

    for entry in journal_data:
        fout.write(entry)
    
    fout.close()

def add_entry(text,journal_data):
    journal_data.append(text)