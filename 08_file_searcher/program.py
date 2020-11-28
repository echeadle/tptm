import os

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

    search_folders(folder, text)

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
    text = input('What are you searching for [single phrases only]?')
    return text

def search_folders(folder, text):
    print(f'Would search {folder} for {text}.')


if  __name__ == "__main__":
    main()
