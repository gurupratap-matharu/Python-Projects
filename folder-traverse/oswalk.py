import shutil, os
# import major libraries we are going to use

for folderName, subfolders, filenames in os.walk('/Users/Admin/Desktop/webproject/'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE OF ' + folderName + ': ' + filename)

    print('')
                                                 
