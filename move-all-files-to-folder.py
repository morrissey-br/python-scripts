import shutil
import os

# ./exiftool.exe -r -d %s -tagsfromfile "%d/%F.json" "-GPSAltitude<GeoDataAltitude" "-GPSLatitude<GeoDataLatitude" "-GPSLatitudeRef<GeoDataLatitude" "-GPSLongitude<GeoDataLongitude" "-GPSLongitudeRef<GeoDataLongitude" "-Keywords<Tags" "-Subject<Tags" "-Caption-Abstract<Description" "-ImageDescription<Description" "-DateTimeOriginal<PhotoTakenTimeTimestamp" -ext "*" -overwrite_original -progress --ext json "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2009" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2010" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2011" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2012" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2013" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2014" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2015" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2016" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2017" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2018" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2019" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2020" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2021" "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2022"

destination_folder = "C:/Users/samue/Downloads/Compilation"
gif_destination_folder = "C:/Users/samue/Downloads/CompilationGifs"

folders_names = [
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2009",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2010",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2011",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2012",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2013",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2014",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2015",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2016",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2017",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2018",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2019",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2020",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2021",
    "C:/Users/samue/Downloads/Takeout/Google Fotos/Photos from 2022",
]

json_files_removed = 0
files_moved = 0
gif_files_moved = 0

# Remove all .json files from the folders
for folder in folders_names:
    for file in os.listdir(folder):
        if file.endswith(".json"):
            file_path = folder + "//" + file
            os.remove(file_path)
            gif_files_moved += 1

# Move all gif files to a new folder
for folder in folders_names:
    for file in os.listdir(folder):
        if file.endswith(".gif"):
            file_path = folder + "//" + file
            shutil.move(file_path, gif_destination_folder)
            files_moved += 1

# Move all files to the destination folder
for folder in folders_names:
    for file in os.listdir(folder):
        shutil.move(folder + "//" + file, destination_folder)
        files_moved += 1

print("Removed " + str(json_files_removed) + " json files")
print("Moved " + str(files_moved) + " files to " + destination_folder)
print("Moved " + str(gif_files_moved) +
      " gif files to " + gif_destination_folder)
