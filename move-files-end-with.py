# Move all files and with a certain extension to a new folder
import shutil
import os

origin_file_path = 'C:/Users/samue/Pictures/iCloud Photos/Photos/'
destination_file_path = 'C:/Users/samue/Downloads/heic/'
extension = '.HEIC'

total_files_moved = 0

for file in os.listdir(origin_file_path):
    if file.endswith(extension):
        shutil.move(origin_file_path + file, destination_file_path + file)
        print(file + ' moved')
        total_files_moved += 1

print('Total files moved: ' + str(total_files_moved))
