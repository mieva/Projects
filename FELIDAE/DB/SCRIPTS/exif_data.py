
import exifread
import os

# To get a specific field:
def get_field (tags,field) :
  for tag in tags.keys():
      if tag  == field:
          return tags[tag]

directory_in_str = "C:\\Users\\Michela\\Desktop\\ieva\\DATASCIENCE\\PROJECTS\\FELIDAE\\IMAGES\\SITE1\\batch1\\"

directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    print("########### New file ###########")

    filename = os.fsdecode(file)
    # Open image file for reading (binary mode)
    f = open(directory_in_str+filename, 'rb')
    #f = open(file, 'rb')

    # Return Exif tags, details = false to faster processing 
    tags = exifread.process_file(f, details=False)

    #for tag in tags.keys():
        #if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
    #    if tag == 'IMAGE':
    #        print(tag, tags[tag])

    trigger = get_field(tags, 'Image ImageDescription')
    date_and_time = get_field(tags, 'Image DateTime')


    print(trigger, date_and_time)