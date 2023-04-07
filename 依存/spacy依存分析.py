import spacy

# 加载中文模型
import pkuseg
import os
from stanfordcorenlp import StanfordCoreNLP

# 定义要分析的文本
text = "这是一个句子。"

# 对文本进行分词
seg = pkuseg.pkuseg()
words = seg.cut(text)

# 对文本进行依存分析
nlp = StanfordCoreNLP(os.path.join(os.getcwd(), "stanford-corenlp-full-2018-10-05"))
result = nlp.dependency_parse(text)

# 计算平均依存距离
total_distance = 0
for i in range(len(result)):
    if result[i][0] != 0:
        total_distance += abs(i - result[i][0])
average_distance = total_distance / len(result)

# 打印结果
print("Average dependency distance:", average_distance)