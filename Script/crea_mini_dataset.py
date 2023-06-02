from argparse import ArgumentParser
from sys import exit
from os import listdir
from os.path import join, isfile
from random import sample
from creazione_dataset import to_grayscale

def get_file_names(directory_path):
    file_names = []
    for filename in listdir(directory_path):
        if isfile(join(directory_path, filename)):
            file_names.append(filename)
    return file_names

if __name__ == '__main__':
    aparse = ArgumentParser()
    aparse.add_argument('--num', type=int, dest='num')
    a = aparse.parse_args()

    if a.num == None:
        print('Bro usa il parametro --num [numero imgs]')
        exit(1)

    dirname = 'all'
    filenames = get_file_names(dirname)
    prescelti = sample(filenames, a.num)
    for p in prescelti:
        print(f'Working with {p}')
        to_grayscale(p)
    