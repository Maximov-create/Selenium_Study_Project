import os


def clear_screens_directory():
    directory_path = r'./screens'
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        os.remove(file_path)
    print('SCREENS DIRECTORY CLEARED')
