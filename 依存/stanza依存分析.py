import os
import stanza

# 加载中文模型
stanza.download('zh')
nlp = stanza.Pipeline('zh')

# 定义要分析的目录和保存结果的目录
input_dir = r'C:\Users\魏子超\OneDrive\学习\毕业论文\语料txt\测试'
output_dir = os.path.join(input_dir, '依存分析结果')

# 如果保存结果的目录不存在，就创建它
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历目录下的所有txt文件
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        # 读取txt文件内容
        input_filepath = os.path.join(input_dir, filename)
        with open(input_filepath, 'r', encoding='utf-8') as f:
            text = f.read().strip()

        # 进行分词和依存句法分析
        doc = nlp(text)

        # 输出分析结果到新的txt文件
        output_filepath = os.path.join(output_dir, f'{filename[:-4]}_output.txt')
        with open(output_filepath, 'w', encoding='utf-8') as f:
            for sentence in doc.sentences:
                for word in sentence.words:
                    f.write(f'{word.text}\t{word.head}\t{word.deprel}\n')
                f.write('\n')