"""
Program to retrive random cat videos
"""
import os
import cat_service

def main():
    """
    Main Module, where program starts
    """
    print_header()
    folder = get_or_create_output_folder()
    # download cat pictures
    download_cats(folder)
    # display cats



def print_header():
    """
    Simple Show header method
    :params: None
    """
    print('-' * 40)
    print('           CAT FACTORY')
    print('-' * 40)
    print()

def get_or_create_output_folder():
    """
    Get or Create Output folder
    """
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Createing new directory at {full_path}')
        os.mkdir(full_path)

    return full_path

def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = f'lolcat_{i}'
    cat_service.get_cat(folder, name)


if __name__ == '__main__':
    main()
