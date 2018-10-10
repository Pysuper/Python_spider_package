# 安装 -- pip install pyquery

# 初始化
# 字符串初始化
from pyquery import PyQuery as pq
html = ''''''
doc = pq(html)
print(doc('li'))    # doc的参数传入需要选择的字段

# url初始化
from pyquery import PyQuery as pq
doc = pq(url='http://www.baidu.com')
print(doc('head'))

# 文件初始化
from pyquery import PyQuery as pq
doc = pq(filename='2.html')  # demo.html是一个本地文本
print(doc('li'))


# 基本CSS选择器
html = ''
from pyquery import PyQuery as pq
doc = pq(html)
print(doc('#container .list li'))   # id加# class加.　标签不用加
# 一层一层的查找


# 查找元素 #
# 子元素(打印的类型是PyQuery) 只要在它里面就行
html = ''
from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
print(type(items))
lis = items.find('li')  # 也可以使用层层嵌套的查找选择
print(type(lis))
print(lis)

# 查找所有直接子元素(可以传入一个参数，也就是CSS选择器)
lis = items.children()
print(type(lis))
print(lis)

lis = items.children('.active')
print(lis)


# 父元素
from pyquery import PyQuery as pq
html = ''
doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

# parents查找所有祖先节点,只要是祖先节点，都会被返回
from pyquery import PyQuery as pq
html = ''
doc = pq(html)
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)  # 所有祖先节点都会被返回

parent = items.parents('.wap')  # 使用CSS选择器再次选择class
print(parent)


# 兄弟元素
from pyquery import PyQuery as pq
html = ''
doc = pq(html)
li = doc('.list .item-0.active')    # 查找class为list下,同时包含item-0和active的标签
print(li.siblings())
print(li.siblings('.active'))



# 遍历
doc = pq(html)
lis = doc('.li').items()    # 生成产生器(.items)
print(type(lis))
for i in lis:   # 使用for遍历
    print(li)

# 获取属性
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.items-0.active a')    # 选择同时含有items-0,active的class，其中的a标签
print(a)
print(a.attr('href'))
print(a.attr.href)

# 获取文本
from pyquery import PyQuery as pq
html = ''
doc = pq(html)
a = doc('.items-0.active a')
print(a)
print(a.text()) # 获取被a标签包含的文字

# 获取HTML内容
from pyquery import PyQuery as pq
html = ''
doc = pq(html)
a = doc('.items-0.active a')
print(li)
print(li.html())


# DOM操作
# addClass、removeClass  # 动态的修改html
from pyquery import PyQuery as pq
html = ''
doc = pq(html)
li = doc('.items-0.active a')
print(li)
li.remove_class('active')
print(li)
li.add_class('.active')
print(li)

# attr、css
from pyquery import PyQuery as pq
html = ''
doc = pq(html)
li = doc('.items-0.active a')
print(li)
li.attr('name','link')  # 添加一个name-link的属性，如果本来就有，则会修改原来的属性
print(li)
li.css('font-size','14px')  # 添加一个style属性
print(li)

# remove
from pyquery import PyQuery as pq
html = ''
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove() # 通过remove删除原html中的一部分信息，然后再打印出来
print(wrap.text())


# 其他DOM方法
# 伪类选择器(选择特定标签)
from pyquery import PyQuery as pq
html = ''
doc = pq(html)
li = doc('li:first-child')  # 获取第一个li标签
print(li)
li = doc('li:last-child')   # 获取最后一个li标签
print(li)
li = doc('li:nth-child(2)') # 指定索引顺序为２的标签(从０开始的)奇数:2n+1
print(li)
li = doc('li:gt(2)')    # 获取比２大的标签，第二个之后的标签
print(li)
li = doc('li:nth-child(2n)')    # 获取所有偶数标签
print(li)
li = doc('li:contains(second)') # 获取包含second文本的li标签
print(li)
