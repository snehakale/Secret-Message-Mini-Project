import os

def rename_files():
    #getting a list of files
    file_list = os.listdir(r"D:\Sneha Data\FSWD_Data\secret message mini project\message")
    print(file_list)

    #renaming each file
    directory_path="D:\Sneha Data\FSWD_Data\secret message mini project\message\\"
    for file_name in file_list:
        old_file= directory_path+file_name
        print("old file name="+old_file)
        new_file=old_file.translate(old_file.maketrans('','','0123456789'))
        print("new file name="+new_file)
        os.rename(old_file,new_file)

rename_files()
