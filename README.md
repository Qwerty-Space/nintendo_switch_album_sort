# nintendo_switch_album_sort
Sorts Nintendo Switch albums into something more navigable 
Will sort photos and videos with the format `YYYmmDDHHMMSS....jpg` into pre-determined directories, with filenames similar to Android photos (`IMG_YYYYmmDD` or `VID_YYYYmmDD`).

## Requirements
• >= python 3.7

## Usage
Save `nintendo_sort.py` into the folder you want your albums saving into, create a `sort` directory, and put the folders copied from your Nintendo Switch in there.  Then run `python nintendo_sort.py`

Default directory structure is:
```
nintendo_sort.py
sort/
  2020/
    03/
      29/
        files_to.jpg
        sort.mp4
        2020032919262400-86ASHDG6D7D5265ASD.jpg
      30/
        2020033018254100-86ASHDG6D7D5265ASD.jpg
        2020033019125000-86ASHDG6D7D5265ASD.mp4
        
2020/
  03 March/
    Photos/
      IMG_20200330_182541.jpg
      IMG_20200330_192624.jpg
    Videos/
      VID_20200330_191250.mp4
```


## Default Configuration
```
# The Directory to sort from
sorting_dir = "sort"

# Whether to separate videos from images
separate_filetypes = True

# The directory to put images and videos
images_dir = "Photos"
videos_dir = "Videos"

# The directory structure to sort into (supports strftime format codes)
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
path_format = ["%Y", "%m %B"]

# Whether to copy the files, or move them
copy_files = True

# Overwrite files if they exist
overwrite = False
```
