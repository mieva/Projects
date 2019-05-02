from datetime import date 
import exifread
import shutil
import os

# To get a specific field:
def get_field (tags,field) :
  for tag in tags.keys():
      if tag  == field:
          return tags[tag]


def uploads(location, camera_name, directory_in_str) : 

    ##### Date of uplaods
    today = str(date.today())

    print("####", location, camera_name)
    print("####", today)

    #### How many images inside the batch
    directory = os.fsencode(directory_in_str)
    
    images_count = len(os.listdir(directory))
    print(images_count)

    #### Create the folder to save the images
    path = "Images\\"+location+"\\"+camera_name+"_"+today
    print(path)
    os.makedirs(path, exist_ok=True)


    for file in os.listdir(directory):
        print("########### New file ###########")

        filename = os.fsdecode(file)

        ## Copy the file into the new dir
        shutil.copy2(directory_in_str+filename, path)

        # Open image file for reading (binary mode)
        f = open(directory_in_str+filename, 'rb')

        # Return Exif tags, details = false to faster processing 
        tags = exifread.process_file(f, details=False)

        trigger = get_field(tags, 'Image ImageDescription')
        date_and_time = get_field(tags, 'Image DateTime')
        brand = get_field(tags, 'Image Make')


        print(trigger, date_and_time)


location = "SanFrancisco"
camera_name = "BUSHNELL"
directory_in_str = "C:\\Users\\Michela\\Desktop\\ieva\\DATASCIENCE\\PROJECTS\\FELIDAE\\IMAGES\\SITE1\\batch1\\"

uploads(location, camera_name, directory_in_str)