import os
import shutil
import re

print(os.getcwd())

zip_to_unzip = os.getcwd() + "\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\unzip_me_for_instructions.zip"

output_folder = os.getcwd()

testlist = []

shutil.unpack_archive(zip_to_unzip, output_folder)


directory = os.getcwd() + "\\extracted_content"


for subdir, dirs, files in os.walk(directory):
    for filename in files:
        if (subdir + os.sep + filename).endswith(".txt"):
            openfile = subdir + os.sep + filename
            testfile = open(openfile, "r")
            filecontent = testfile.read()
            phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',filecontent)
            if phone is not None:
                testlist.append(phone)

print(testlist)

