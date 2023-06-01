import cv2
import os

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
        photo = cv2.imread(rf'images\{image_name}')
        grayscaled = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(rf"grayscaled_images\gray-{image_name}", grayscaled)