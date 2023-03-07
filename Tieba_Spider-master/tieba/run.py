from apscheduler.schedulers.blocking import BlockingScheduler
import os

# 存放所有任务的列表，每个任务用字典表示
spiders = [
    {'name': '人工智能', 'cmd': 'scrapy crawl 人工智能'},
    {'name': 'chatgpt', 'cmd': 'scrapy crawl chatgpt'},
    {'name': '彩礼', 'cmd': 'scrapy crawl 彩礼'},
    {'name': '道诡异仙', 'cmd': 'scrapy crawl 道诡异仙'},
    {'name': '东野圭吾', 'cmd': 'scrapy crawl 东野圭吾'},
    {'name': '俄亥俄', 'cmd': 'scrapy crawl 俄亥俄'},
    {'name': '俄乌战争', 'cmd': 'scrapy crawl 俄乌战争'},
    {'name': '考研', 'cmd': 'scrapy crawl 考研'},
    {'name': '流浪地球', 'cmd': 'scrapy crawl 流浪地球'},
    {'name': '满江红', 'cmd': 'scrapy crawl 满江红'},
    {'name': '明日方舟', 'cmd': 'scrapy crawl 明日方舟'},
    {'name': '人口', 'cmd': 'scrapy crawl 人口'},
    {'name': '三体', 'cmd': 'scrapy crawl 三体'},
    {'name': '少女前线', 'cmd': 'scrapy crawl 少女前线'},
    {'name': '星际争霸2', 'cmd': 'scrapy crawl 星际争霸2'},
    {'name': '星穹铁道', 'cmd': 'scrapy crawl 星穹铁道'},
    {'name': '易烊千玺', 'cmd': 'scrapy crawl 易烊千玺'},
    {'name': '疫情', 'cmd': 'scrapy crawl 疫情'},
    {'name': '原神', 'cmd': 'scrapy crawl 原神'},
    # 添加其他任务......
]

# 当前要执行的任务索引
current = 0

# 创建定时任务
def run_spider():
    global current
    spider = spiders[current]   # 取出当前任务
    os.chdir(r'C:\Users\魏子超\OneDrive\Pycharm\MyPythonProject1\Tieba_Spider-master')
    os.system(spider['cmd'])    # 执行当前任务
    current = (current + 1) % len(spiders)   # 切换到下一个任务

# 创建调度器
scheduler = BlockingScheduler()

# 添加定时任务，间隔时间为30秒，重复执行10次
scheduler.add_job(run_spider, 'interval', seconds=30, id='job_id', max_instances=10)

# 定义结束执行的回调函数，它会等待任务执行完毕后再等待1分钟后继续执行
def on_job_end():
    global current
    current = 0
    scheduler.add_job(run_spider, 'interval', minutes=1, id='job_id')

# 添加结束回调任务
scheduler.add_listener(on_job_end, 'job_executed')

# 开始执行调度器
scheduler.start()

