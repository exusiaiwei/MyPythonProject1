import os
import shutil

source_folder = r'C:\tmp'
target_folder = r'C:\Users\魏子超\OneDrive\学习\毕业论文\贴吧\txt'

# 遍历源文件夹及其子目录，找到所有.txt文件，并移动到目标文件夹
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.endswith('.txt'):
            source_path = os.path.join(root, file)
            target_path = os.path.join(target_folder, file)
            shutil.move(source_path, target_path)