import pandas as pd

# 读取Excel文件
df = pd.read_excel("C:\\Users\\魏子超\\OneDrive\\学习\\毕业论文\\知乎\\知乎-爬回答1.xlsx", sheet_name=0)

# 选取URL列，批量删除/answer及之后的部分
df['Url'] = df['Url'].apply(lambda x: x.split('/answer')[0])

# 保存Excel文件
df.to_excel("C:\\Users\\魏子超\\OneDrive\\学习\\毕业论文\\知乎\\知乎-爬回答1.xlsx", sheet_name='Sheet1')