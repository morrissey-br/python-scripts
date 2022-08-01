from os import listdir
from os.path import isfile, join
import json
from datetime import datetime
import piexif
jsonDir = 'C:/Users/samue/Downloads/Takeout/Google Fotos/json'
photosDir = "C:/Users/samue/Pictures/iCloud Photos/Photos"

totalReplaced = 0
filesWithoutInformation = 0
photosDontFinded = 0
photosWithCorrectDate = 0
nonJpegFiles = 0

listOfJsonFilesNames = listdir(jsonDir)
listOfPhotosFilesNames = listdir(photosDir)

totalFiles = len(listOfJsonFilesNames)
filesProcessed = 0
processPorcentage = 0

for jsonName in listOfJsonFilesNames:
    filesProcessed += 1
    processPorcentage = int(filesProcessed * 100 / totalFiles)
    print("Processing file: " + str(filesProcessed) + " of " +
          str(totalFiles) + " (" + str(processPorcentage) + "%)")
    # Read JSON file and get the photo title and photo taken date.
    jsonFile = open(jsonDir + "/" + jsonName, "r", encoding="utf8")
    jsonData = json.load(jsonFile)
    title = jsonData["title"]
    date = datetime.fromtimestamp(
        int(jsonData["photoTakenTime"]["timestamp"])).strftime('%Y:%m:%d %H:%M:%S')

    # If title or date is empty, skip this file.
    if title == "" or date == "":
        filesWithoutInformation += 1
        continue

    # If the file is not a jpeg, jpg or tiff, skip it.
    canRead = title.lower().endswith(".jpg") or title.lower().endswith(
        ".jpeg") or title.lower().endswith(".tiff") or title.lower().endswith(".tif")
    print(title, canRead)
    if not canRead:
        nonJpegFiles += 1
        continue

    # If the photo with the same title doesn't exist, skip this file.
    if title not in listOfPhotosFilesNames:
        photosDontFinded += 1
        continue

    # Get the photo file exif data.
    photoData = piexif.load(photosDir + "/" + title)

    if(photoData):
        # If the photo date is equal to the JSON date, skip this file.
        if(piexif.ImageIFD.DateTime in photoData["0th"]):
            if(photoData["0th"][piexif.ImageIFD.DateTime].decode('utf-8') == date):
                photosWithCorrectDate += 1
                continue
        # Change the date of the photo.
        photoData["0th"][piexif.ImageIFD.DateTime] = date.encode(
            'ascii')
        # Save the photo file exif data.
        piexif.insert(piexif.dump(photoData), photosDir + "/" + title)
        totalReplaced += 1
    else:
        print("No exif data found for " + title)

print("Replaced " + str(totalReplaced) + " files.")
print("Skipped " + str(filesWithoutInformation) +
      " files without information.")
print("Skipped " + str(photosWithCorrectDate) + " files with correct date.")
print("Skipped " + str(photosDontFinded) + " files with no photo.")
print("Skipped " + str(nonJpegFiles) + " non jpeg files.")
