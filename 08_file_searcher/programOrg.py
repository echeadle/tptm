import os
import collections

SearchResults = collections.namedtuple('SearchResults', 
                                        'file, line, text')

def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location.")
        return
    text = get_search_text_from_user()
    if not text:
        print("We can't search for nothing!")
        return

    matches = search_folders(folder, text)
    match_count = 0
    for m in matches:
        match_count += 1

       # print(m)
        #print('------------ MATCH ------------')
        #print(f'file:    {m.file}')
        #print(f'line:    {m.line}')
        #print(f'match    {m.text.strip()}')
        #print()
    print(f'Number of matches for {text} is {match_count}')

def print_header():
    """
    Simple Show header method
    :params: None
    """
    print('-' * 40)
    print('           FILE SEARCH APP')
    print('-' * 40)
    print()


def get_folder_from_user():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None
    
    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]? ')
    return text.lower()

def search_folders(folder, text):

    all_matches = []
    items =  os.listdir(folder)
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            matches = search_folders(full_item, text)
            all_matches.extend(matches)
        else:
            matches = search_file(full_item, text)
            all_matches.extend(matches)

    return all_matches

def search_file(filename, search_text):
    matches = []
    with open(filename, 'r', encoding='utf-8') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResults(file=filename, line=line_num, text=line)
                matches.append(m)

        return matches

if  __name__ == "__main__":
    main()
