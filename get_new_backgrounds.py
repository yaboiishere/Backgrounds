import shutil
import os
from PIL import Image
oc_directory = os.path.expanduser(
    "~") + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
new_directory = os.getcwd() + "\\new"


for f in os.listdir(oc_directory):
    try:
        image = Image.open(oc_directory+"\\"+f)
        witdth, height = image.size
         if witdth >= 1920 and height >= 1080:
            shutil.copy(oc_directory+"\\"+f, new_directory)
    except FileExistsError:
        os.rmdir(new_directory+"\\"+f)
        continue

for filename in os.listdir(new_directory):
    try:
        if filename.endswith(".jpg") or filename.endswith(".py") or os.path.isdir(filename):
            continue
        else:
            os.rename(new_directory+"\\"+filename,
                      new_directory+"\\"+filename + ".jpg")
            continue
    except FileExistsError:
        os.remove(new_directory+"\\"+filename)
        continue
