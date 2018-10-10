### 使用步骤
    from  lxml  import etree
    
    html_xpath  =  etree. HTML( html_text )
    
    info  =  html_xpath. xpath ( '//*[@id="ip_list"]/tr/td[2]' ) ---- xpath(css) 

### 语法例:

    from  lxml  import etree    
    
    page_html = etree.HTML(first_html)  
    
    last_page = page_html.xpath('//*[@id="body"]/div[2]/a[10]')[0]
    
    # 在获取单个标签的时候, info 单个元素, 获取大量相同标签的时候, info 就是一个列表
    # 获取多个 info 的时候, 遍历时候 可以使用 zip 进行压缩遍历----这时候的 zip 是不需要导入的

    info_list = page_html.xpath('//*[@id="ip_list"]/tr/td[7]/*[@class="bar"]/div/@style')
    
    day_list = page_html.xpath('//*[@id="ip_list"]/tr/td[9]')
    
    pri_day_list = page_html.xpath('//*[@id="ip_list"]/tr/td[10]')
    
    #  for ip,port,location,anonymous,https,info,day,pri_day in six.moves.zip(ip_list, port_list, location_list, anonymous_list, https_list, info_list,day_list, pri_day_list):
    
    for ip,port,location,anonymous,https,info,day,pri_day in zip(ip_list, port_list, location_list, anonymous_list, https_list, info_list,day_list, pri_day_list):
        
        print( ip,port,location,anonymous,https,info,day,pri_day )
        
* xpath在选择的时候. 选择语法类似于css选择器

### xpath语法
#### 选取节点

XPath 使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者 step 来选取的。

| 通配符             |描述                         |
|--------------------| :--------------------------|
|nodename            |选取此节点的所有子节点。      |
|/                   |从根节点选取。               |
|//                  |从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。|
|.                   |选取当前节点。               |
|..                  |选取当前节点的父节点。        |
|@                   |选取属性。                   |

##### 例如:

| 通配符              |描述                         |
|--------------------| :--------------------------|
|bookstore           |选取 bookstore 元素的所有子节点。|
|/bookstore          |选取根元素 bookstore。注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！|
|bookstore/book      |选取属于 bookstore 的子元素的所有 book 元素。|
|//book              |选取所有 book 子元素，而不管它们在文档中的位置。|
|bookstore//book     |选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。|
|//@lang             |选取名为 lang 的所有属性。|

#### 谓语选择
查找某个特定的节点或者包含某个指定的值的节点----被嵌在方括号中

| 通配符                         |描述                         |
|-------------------------------| :--------------------------|
|/bookstore/book[1]             |选取属于 bookstore 子元素的第一个 book 元素。|
|/bookstore/book[last()]        |选取属于 bookstore 子元素的最后一个 book 元素。|
|/bookstore/book[last()-1]      |选取属于 bookstore 子元素的倒数第二个 book 元素。|
|/bookstore/book[position()<3]  |选取最前面的两个属于 bookstore 元素的子元素的 book 元素。|
|//title[@lang]                 |选取所有拥有名为 lang 的属性的 title 元素。|
|//title[@lang='eng']           |选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。|
|/bookstore/book[price>35.00]   |选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。|
|/bookstore/book[price>35.00]/title  |选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。

#### 选取未知节点---- XPath 通配符可用来选取未知的 XML 元素。

| 通配符                         |描述                         |
|-------------------------------| :--------------------------|
|*                              |匹配任何元素节点。|
|@*                             |匹配任何属性节点。|
|node()                         |匹配任何类型的节点。|

##### 例如:
| 通配符                         |描述                           |
|-------------------------------| :-----------------------------|
|/bookstore/*                   |选取 bookstore 元素的所有子元素。|
|//*                            |选取文档中的所有元素。           |
|//title[@*]                    |选取所有带有属性的 title 元素.    |

#### 选取若干路径---- 使用“|”运算符，可以选取若干个路径。

| 通配符                         |描述                           |
|-------------------------------| :-----------------------------|
|//book/title | //book/price    |选取 book 元素的所有 title 和 price 元素。|
|//title | //price              |选取文档中的所有 title 和 price 元素。|
|/bookstore/book/title | //price  |选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。


### python_spider.py

    import requests
    import re
    from lxml import etree
    import six.moves
    
    
    def get_url_html(url, head,proxy):
        """返回当前访问的页面 HTML"""
        response = requests.get(url, headers=head,proxies=proxy)
        response.encoding = "gbk"
        if response.status_code == 200:
            return response.text
            print("无法访问...")


    def get_last_page(first_html):
        """从当前访问的网页源码中获取, 当前页面中的有效信息"""
        page_html = etree.HTML(first_html)
        
        # 使用 Xpath 语法的时候, 跟CSS语法很像--标签选择器
        last_page = page_html.xpath('//*[@id="body"]/div[2]/a[10]')[0]
        ip_list = page_html.xpath('//*[@id="ip_list"]/tr/td[2]')
        port_list = page_html.xpath('//*[@id="ip_list"]/tr/td[3]')
        location_list = page_html.xpath('//*[@id="ip_list"]/tr/td[4]/a')
        anonymous_list = page_html.xpath('//*[@id="ip_list"]/tr/td[5]')
        https_list = page_html.xpath('//*[@id="ip_list"]/tr/td[6]')
        info_list = page_html.xpath('//*[@id="ip_list"]/tr/td[7]/*[@class="bar"]/div/@style')
        day_list = page_html.xpath('//*[@id="ip_list"]/tr/td[9]')
        pri_day_list = page_html.xpath('//*[@id="ip_list"]/tr/td[10]')
        
        # 注意: 这里返回的是每个列表
        return ip_list, port_list, location_list, anonymous_list, https_list, info_list, day_list, pri_day_list


    def save_ip_info(ip_list, port_list, location_list, anonymous_list, https_list, info_list, day_list, pri_day_list): 
    """通过获取列表, 同时遍历获取里面的数据, 这里for遍历的时候用到 zip """
        for ip,port,location,anonymous,https,info,day,pri_day in six.moves.zip(ip_list, port_list, location_list, anonymous_list, https_list, info_list,day_list, pri_day_list):
            
            # 遍历之后, 可以将遍历的结果打印出来--检验之前的代码是否正确
            # print(ip.text,port.text,location.text,anonymous.text,https.text,info,day.text,pri_day.text) 
            content = ip.text,port.text,location.text,anonymous.text,https.text,info,day.text,pri_day.text
            with open('./ip_port.txt','a') as f:         
                 f.write(str(content) + '\n')  
                 print(ip.text,"ok")


    if __name__ == '__main__':  
        head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36"}   
        proxy = {"http":"222.223.40.221:8060"}    

        for num in range(10,3456):
            # 通过第一页的HTML--获得该标题下的所有页数(int类型)--首先就要解析这一页的HTML   
            url = "http://www.xicidaili.com/nn/%s" % num
            first_html = get_url_html(url, head,proxy)       
            ip_list, port_list, location_list, anonymous_list, https_list, info_list, day_list, pri_day_list = get_last_page(first_html)  
            save_ip_info(ip_list, port_list, location_list, anonymous_list, https_list, info_list, day_list, pri_day_list)    
            
            # 在测试的时候, 最好可以先break, 每次先使用一个链接尝试, 如果代码都没有问题, 再把break注释掉,节省时间
            # break
