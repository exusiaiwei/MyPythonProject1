import jsonlines
import json

with jsonlines.open(r"/MyPythonProject1/WeiboSpider-master/output/道诡异仙.jsonl", "r") as rfd:
    with open(r"C:\Users\魏子超\OneDrive\Pycharm\MyPythonProject1\WeiboSpider-master\output\道诡异仙.json", "w", encoding='utf-8') as wfd:
        for data in rfd:
            json.dump(data, wfd, indent=4, ensure_ascii=False)