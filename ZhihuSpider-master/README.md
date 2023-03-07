# ZhihuSpider
知乎爬虫，用于爬取知乎上的内容，并且将爬取的内容解析为markdown保存到本地硬盘。

## 支持的内容
目前支持的内容包括：
- 特定问题下的所有(优质)回答
- 特定用户的所有回答、文章
- 专栏
- 话题精华
- 收藏夹
- 单个回答
- 单篇文章

## 爬虫工作方式
利用知乎api获得相应的内容，其中回答、文章的的主体内容是以html标签的形式包含在api返回的内容中。提取主体内容，将这部分内容解析转换成markdown文件保存到本地

## 启动方式
GrandConcourse.py是脚本的启动入口。以知乎的问题“[你见过哪些惊艳的句子？](https://www.zhihu.com/question/320078376)”为例。该问题的链接为：https://www.zhihu.com/question/320078376 ，末尾的“320078376”就是该问题唯一的id，将其粘贴到GrandConcourse.py下的“question_id”下即可启动爬取该问题下的优质答案，即`question_id = '320078376'`。

## 写在最后

私自大量爬取知乎的数据终究不好，请酌情使用，自行承担后果。野生程序员的第一个项目，有很多不足，有兴趣可以交流。QQ：1573687170