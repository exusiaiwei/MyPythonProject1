import os

# get the directory of the folder
folder_name = input(r'C:\Users\魏子超\OneDrive\Pycharm\MyPythonProject1\语料txt')
folder_path = os.getcwd() + '/' + folder_name + '/'

# iterate through the folder
for file in os.listdir(folder_path):

    # only process .txt files
    if file.endswith('.txt'):
        f = open(folder_path + file, 'r')
        lines = f.readlines()
        f.close()

        # remove empty lines
        lines = [line for line in lines if line.strip() != '']

        # write to the file
        f = open(folder_path + file, 'w')
        f.writelines(lines)
        f.close()

print('Done!')