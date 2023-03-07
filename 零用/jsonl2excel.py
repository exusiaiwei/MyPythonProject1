#import pandas as pd

# 读取jsonl文件
#df = pd.read_json(r'C:\Users\魏子超\OneDrive\Pycharm\MyPythonProject1\WeiboSpider-master\output\人民日报.jsonl', lines=True)
# 将数据框导出为Excel表格
#df.to_excel(r'C:\Users\魏子超\OneDrive\Pycharm\MyPythonProject1\WeiboSpider-master\output\人民日报.xlsx')
import os
import pandas as pd

# 获取文件夹内文件路径
in_dir = r'/MyPythonProject1/WeiboSpider-master/output'
file_list = os.listdir(in_dir)

# 循环把文件转换为xlsx文件
for file in file_list:
    if file.endswith('.jsonl'):
        df = pd.read_json(os.path.join(in_dir, file), lines=True)
        df.to_excel(os.path.join(in_dir,os.path.splitext(file)[0]+'.xlsx'))