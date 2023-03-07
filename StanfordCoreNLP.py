from stanfordcorenlp import StanfordCoreNLP
import json

#如果要用其他语言，需要单独设置
nlp = StanfordCoreNLP(r'C:\Research\stanford-corenlp-4.5.2')
nlp_ch= StanfordCoreNLP(r'C:\Research\stanford-corenlp-4.5.2', lang='zh')
sen='我希望所有喜欢我的人都能够幸福平平安安的过好这一辈子'
print(nlp_ch.pos_tag(sen))
print(nlp_ch.parse(sen))
