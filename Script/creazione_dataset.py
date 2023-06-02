import cv2
import os
from os.path import join

def to_grayscale(imagepath):
    photo = cv2.imread(join('all', imagepath))
    cv2.imwrite(join('images', imagepath), photo)
    grayscaled = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(join('grayscaled_images', f'fgray-{imagepath}'), grayscaled)

def get_file_names(directory_path):
    file_names = []
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_names.append(filename)
    return file_names

if __name__ == '__main__':

    directory_path = 'images'
    file_names = get_file_names(directory_path)

    for image_name in file_names:
        to_grayscale(image_name)