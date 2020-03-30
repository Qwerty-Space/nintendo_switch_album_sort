import re
import os
import os.path as osp
from imghdr import what
from shutil import copy2
from datetime import datetime


## Config ##
# The Directory to sort from
sorting_dir = "sort"

# Whether to separate videos from images
separate_filetypes = True

# The directory to put images and videos (default "Photos" and "Videos")
images_dir = "Photos"
videos_dir = "Videos"

# The directory structure to sort into (supports strftime format codes)
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
path_format = ["%Y", "%m %B"]

# Whether to copy the files, or move them
copy_files = True

# Overwrite files if they exist
overwrite = False


def main():
    sort = list()
    for root, directories, filenames in os.walk(sorting_dir):  # Create a list of all files in "path"
        for filename in filenames:
            f = os.path.join(root, filename)
            # if ".mp4" or ".jpg" not in f:
            #     return
            sort.append(f)


    for f in sort: 
        # split the name by _ and extract required information
        fname = osp.basename(f)
        ftype = fname[-3:]
        print(ftype)
        if ftype == "jpg":
            fpath = images_dir
            name_prefix = "IMG"
        elif ftype == "mp4":
            name_prefix = "VID"
            fpath = videos_dir
        else:
            continue

        fyear = fname[:4]
        fmonth = fname[4:6]
        fday = fname[6:8]
        fhour = fname[8:10]
        fminute = fname[10:12]
        fsecond = fname[12:14]


        # create a datetime object from the file name info
        fdate = datetime(int(fyear), int(fmonth), int(fday), int(fhour), int(fminute), int(fsecond))
        new_name = f"{name_prefix}_{fyear}{fmonth}{fday}_{fhour}{fminute}{fsecond}.{ftype}"

        # this variable will be an empty string if separate_files is False, else it's equal to fpath
        basename = fpath if separate_filetypes else ""

        # use a splat operator to join every element of the path_format list
        pre_formatted_path = osp.join(*path_format)
        path = osp.join(fdate.strftime(pre_formatted_path), basename)

        os.makedirs(path, exist_ok=True) # make directories, unless they already exist

        new_path = osp.join(path, new_name) # the path of the file after being copied

        # check if the file exists if overwrite is False
        if not overwrite and osp.isfile(new_path):
            # overwrite if prompted
            ans = input(f"File exists:  {new_path}\noverwrite? (y/n)  ")
            if ans[0] == "n":
                print("Ignoring:  " + f)
                continue

        copy2(f, new_path) # copy2() preserves metadata
        print(f"Copying file:  {f} → {new_path}")

        if not copy_files: # delete old files?
            os.remove(floc)


if __name__ == "__main__":
    if not osp.isdir(sorting_dir): # make sort dir if it doesn't exist
        os.mkdir(sorting_dir)

    main()
