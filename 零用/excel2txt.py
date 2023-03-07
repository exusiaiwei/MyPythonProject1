import os
import xlrd

input_path = "C:\\Users\\魏子超\\OneDrive - whu.edu.cn\\学习\\毕业论文\\微博\\excel"
output_path = "C:\\Users\\魏子超\\OneDrive - whu.edu.cn\\学习\\毕业论文\\微博\\txt"

for root, dirs, files in os.walk(input_path):
    for file in files:
        if os.path.splitext(file)[1] == ".xlsx":
            file_name = root + "\\" + file
            book = xlrd.open_workbook(file_name)
            sheet = book.sheet_by_index(0)
            # 不包括k1列
            for row in range(1, sheet.nrows):
                with open(output_path + '\\' + os.path.splitext(file)[0] + ".txt", 'a', encoding="utf-8") as f:
                    f.write(str(sheet.cell(row, 10).value) + '\n')
            print("{} 已完成".format(os.path.splitext(file)[0]))