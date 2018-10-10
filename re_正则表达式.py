# re.match(尝试从字符创起始位置匹配一个模式，如果不是起始位置，match()就返回none，匹配成功就返回结果)
# import re
# 正则表达式，目标字符串，匹配模式
# re.match(pattern=,string=,flags=0)

# 正则表达式
# 是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑(非Python独有，re模块实现)
# \w      匹配字符数字及下划线
# \W      匹配非字母数字下划线
# \s      匹配任意空白字符，等价与[\t\n\r\f]
# \S      匹配任意非空白字符
# \d      匹配任意数字[0-9]
# \D      匹配任意非数字
# \A      匹配字符串开始
# \z      匹配字符串结束
# \Z      匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
# \G      匹配最后匹配完成的位置
# \n      匹配一个换行符
# \t      匹配一个制表符
# ^       匹配字符串的开头
# $       匹配字符串的末尾
# .       匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
# 2[...]   用来表示一组字符，单独列出:[amk--'a','m','k']
# [^...]  不在[]中的字符，[^abc]--匹配除任意a,b,c之外的字符
# ‘       匹配0个或多个的表达式
# +       匹配匹配一个或多个的表达式
# ?       匹配0个或1个由前面正则表达式定义的片段，非贪婪方式
# {n}     精确匹配n个前面测试
# {n,m}   匹配n到m次由前面的正则表达式定义的片段，贪婪方式
# a|b     匹配a或b
# ()      匹配括号内的表达式，也表示一个组


# 最常规的匹配
import re

content = 'hello 123 456 World_This is a Regex Demo'
print(len(content))
result = re.match('^hello\s\d\d\d\s\d{3}\s\w{10}.*Demo$',content)
print(result)
print(result.group())   # 返回匹配结果
print(result.span())    # 输出匹配结果的范围


#　范匹配
import re

content = 'hello 123 456 World_This is a Regex Demo'
result = re.match('hello.*?Demo$',content)
print(result)
print(result.group())
print(result.span())


# 获取匹配目标
import re

content = 'hello 1234567 World_This is a Regex Demo'
result = re.match('^hello\s(\d+)\sWorld.*Demo$',content)
print(result)
print(result.group(1))  #group(1)　选择第一个括号内的内容，也就是正则表达式中的括号内容
print(result.span())


# 贪婪匹配
import re

content = 'hello 1234567 World_This is a Regex Demo'
result = re.match('he.*(\d+).*Demo$',content)   # .*会尽可能多的匹配，最后把7留给(d+)
print(result)
print(result.group(1))


# 非贪婪匹配
import re

content = 'hello 123 456 World_This is a Regex Demo'
result = re.match('he.*?(\d+).*Demo$',content)  # ?匹配的过程中，因为有(\d+)如果看到后面匹配的数字就会停止匹配
print(result)
print(result.group(1))


# 匹配模式
import re

content = 'hello 123 456 World_This is a' \
          ' Regex Demo'
result = re.match('^he.*?(\d+).*?Demo$',content)    # .不能匹配换行符－－需要添加re.S
print(result)


import re

content = 'hello 123 456 World_This is a' \
          ' Regex Demo'
result = re.match('^he.*?(\d+).*?Demo$',content,re.S)
print(result)


# 转义
import re

content = 'price is $5.00'
result = re.match('price is $5.00',content) # 特殊字符在正则表达式中不能被匹配－－要加\
print(result)

import re

content = 'price is $5.00'
result = re.match('price is \$5\.00',content)
print(result)


# 总结：尽量使用泛匹配，使用括号得到匹配目标，尽量使用非贪婪模式，有换行符就用re.S






# re.search(扫描整个字符串并返回第一个成功的匹配)
import re
content = 'Extra stings Hello 1234567 World_ This is a Regex Demo Extra stings'
result = re.match('Hello.*?(d+).*?Demo',content)
print(result)

import re
content = 'Extra stings Hello 1234567 World_ This is a Regex Demo Extra stings'
result = re.search('Hello.*?(d+).*?Demo',content)
print(result.group(1))

# 总结：为匹配方便，能用search就不用match

# re.findall(查找所有符合条件的，全部编译出来)
# re.findall.strip(可以去除换行符)

# re.sub(替换字符串每一个匹配的子串后，返回替换后的字符串)
import re
content = 'Extra stings Hello 1234567 World_ This is a Regex Demo Extra stings'
content = re.sub('\d','',content)
print(content)

import re
content = 'Extra stings Hello 1234567 World_ This is a Regex Demo Extra stings'
content = re.sub('\d','say good bay',content)

import re
content = 'Extra stings Hello 1234567 World_ This is a Regex Demo Extra stings'
content = re.sub('(\d)',r'\1 8910',content) # r'\1 ' 表示把第一个括号中的内容替换掉




# re.compile(将正则字符串编译成正则对象，以便复用该匹配模式)
import re
result = 'hello 123456 World_This' \
         'is a Regex Demo'
pattern = re.compile('hell.*?Demo',re.S)
realise = re.match(pattern,result)
# realise = re.match('hell.*?Demo',result)
print(realise)



import requests # 获取网页源代码
import re

url = 'https://book.douban.com'
content = requests.get(url).text
# print(content)

pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
result = re.findall(pattern,content)
# print(result)

for results in result:
    url,name,author,date = results

    author = re.sub('\s','',author)
    date = re.sub('\s','',date)
    # 也可以用.strip()方法

    print(url,name,author,date)


