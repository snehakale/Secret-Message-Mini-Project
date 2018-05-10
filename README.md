## Project Title
### Secret Message Mini Python Project
This is a *secret message mini python project*. It contains a python program which renames files from a folder and these renamed files will reveal a secret message by their names after getting re-arranged.

## Pre-Requisites and Installation
1. Download the given project folder named as *secret message* and a python file *rename_files_project.py*.
2. Download [Python](https://www.python.org/downloads/).
3. Install python step-by-step on your machine. Refer these links, for [windows](https://www.howtogeek.com/197947/how-to-install-python-on-windows/) and for [Mac](https://docs.python.org/3/using/mac.html)
4. Before running this project, copy and paste the secret message folder address in *rename_files_project.py* for `file_list` and `directory_path`.
for example: `file_list = os.listdir(r"D:\GitHub Projects\...\secret message")`
Refer the link below for need to write r before path name.
4. Run **rename_files_project.py**.

## Code Examples 
**rename_files_project.py** 
1) It uses os module. It creates a list of files in the given folder 
eg. `file_list = os.listdir(......`
also uses `rename(old_file, new_file)` method to rename the files.
2) It makes use of translate function to translate the file name.
eg. `new_file=old_file.translate(old_file.maketrans('','','0123456789'))`

## References 
1. [Python Documentation](https://docs.python.org/3/)
2. [Python OS Module](https://docs.python.org/3.2/library/os.html#module-os)
3. [Python Translate Method](https://stackoverflow.com/questions/41708770/translate-function-in-python-3/41708804)
4. [r Before Path Name](https://stackoverflow.com/questions/42654934/need-of-using-r-before-path-name-while-reading-a-csv-file-with-pandas)

