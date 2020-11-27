"""
Program to retrive random cat videos
"""
import os


def main():
    """
    Main Module, where program starts
    """
    print_header()
    # get or create output folder
    folder = get_or_create_output_folder()
    print(f'Found or created folder {folder}')
    # download cat pictures



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

if __name__ == '__main__':
    main()
