# 自动化测试工具，支持多种浏览器
# 爬虫中主要用来解决JavaScript渲染的问题，模拟网页加载

# 基本使用
from selenium import webdriver  # 浏览器驱动对象
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Firefox()
# 这里要下载geckodriverckod，https://github.com/mozilla/geckodriver/releases
# 解压后将geckodriverckod 存放至 /usr/local/bin/ 路径下即可
# sudo mv ～/Downloads/geckodriver /usr/local/bin/
# 否则无法调用浏览器(少内核)

try:
    browser.get('https:baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,10)
    wait.until(ec.presence_of_element_located((By.ID,'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()


# 声明浏览器对象
from selenium import webdriver  # 必须引入这个包
browser = webdriver.Firefox()
browser = webdriver.Chrome()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriver.Safari()

# 访问页面
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()

# 查找元素
# 单个元素
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')               # 寻找一个id为q的元素
input_second = browser.find_element_by_css_selector('#q')   # 使用css选择器选择元素
input_third = browser.find_element_by_xpath('//*[@id="q"]') # 使用xpath选择器选择元素
print(input_first,input_second,input_third)
browser.close()

# browser.find_element_by_name()                通过name查找
# browser.find_element_by_xpath()               通过xpath查找
# browser.find_element_by_link_text()           通过link
# browser.find_element_by_partial_link_text()   a
# browser.find_element_by_tag_name()            a
# browser.find_element_by_class_name()          通过class名查找
# browser.find_element_by_css_selector()        通过css选择器查找


# 通用的查找方式
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.baidu.com')
input_first = browser.find_element(By.ID,'q')   # 查找id为q的标签
print(input_first)
browser.close()


# 多个元素
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')   # find_element-->find_elements(多加了一个ｓ)
print(lis)  # 如果想要单个元素，使用索引[0]
browser.close()


# 元素交互操作
# 对获取的元素调用交互方法
from selenium import webdriver
import time

browser = webdriver.Firefox()                           # 选择Firefox浏览器
browser.get('https://www.taobao.com')                   # 使用选择的浏览器打开淘宝
input = browser.find_element_by_id('q')                 # 找到q标签(审查元素可以看到q标签就是搜索框)
input.send_keys('iPhone')                               # 发送关键字iPone
time.sleep(1)                                           # 等待1秒
input.clear()                                           # 将q标签的内容清空，也就是清空搜索框
input.send_keys('iPad')                                 # 再输入关键字iPad
button = browser.find_element_by_class_name('btn-search')#找到名为btn-search的class标签
button.click()                                          # 点击上一行代码找到的标签，也就是搜索



# 交互动作(将动作附加到动作链中串行执行)
# 模拟拖拽的动作
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)    # 调用浏览器，打开一个链接
browser.switch_to.frame('iframeResult') # 找到目标位置
source = browser.find_elements_by_css_selector('#draggable')    # 被拖拽
target = browser.find_elements_by_css_selector('#droppable')    # 要拖拽去的目标
actions = ActionChains(browser) # 先声明动作了链的对象
actions.drag_and_drop(source,target)    # 执行拖拽
actions.perform()


# 执行JavaScript(通过执行JS,完成进度条的拖拽)
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www,zhihu.com/explore')    # 打开知乎网站
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 把网页拉到最下方
browser.execute_script('alert("To Bottom")')    # 执行上述代码后，显示To Bottom



# 获取元素信息
# 获取属性(例子：获取知乎的logo属性，再把其内容打印出来)
from selenium import webdriver

browser = webdriver.Firefox()
url = 'http://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))


# 获取文本值
from selenium import webdriver

browser = webdriver.Firefox()
url = 'http://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)


# 获取id,位置，标签名，大小
from selenium import webdriver

browser = webdriver.Firefox()
url = 'http://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)         # id
print(input.location)   # 位置
print(input.tag_name)   # 标签名
print(input.size)       # 大小


# Frame
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult') # 传入frame的id，并寻找到该位置
source = browser.find_elements_by_css_selector('#draggable')
print(source)
# 在#draggable中不一定能查找logo，所以提前写好报错信息
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('No Logo')
# 切换到父frame中查找
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)


# 等待
# 隐式等待：当使用了隐式等待执行测试的时候，如果WebDriver没有在DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
# 换句话说，当查找元素，或元素并没有立即出现的时候，隐式等待将等待一段时间再查找DOM，默认的时间式０
from selenium import webdriver
browser = webdriver.Firefox()
browser.implicitly_wait(10) # 是指最长等待时间
browser.get('https://www.zihu.com/explone')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)


# 显式等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Firefox()
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser,10)
input = wait.until(ec.presence_of_element_located((By.ID,'q'))) # 判断该标签是否出现
button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'btn-search'))) # 判断该标签对应的链接是否是可点击的
print(input,button)


# 浏览器前进后退
import time
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()


# Cookies
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www,zhihu.com/explore')
print(browser.get_cookies())
browser.close()
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())


# 网页选项卡管理
import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.baidu.com')    # 用浏览器打开百度
browser.execute_script('window.open()') # 使用Json打开一个新的标签页
print(browser.window_handles)           # 返回所有窗口的引用
browser.switch_to_window(browser.window_handles[1]) # 切换到第二个选项卡
browser.get('https://taobao.com')   # 在第二个选项卡中打开淘宝
time.sleep(1)   # 等待一秒
browser.switch_to_window(browser.window_handles[0]) #　切换到第一个选项卡
browser.get('https://www.python.org')   # 打开Python


# 异常处理
# 找不到元素
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.baidu.com')
browser.find_element_by_id('hello')

# 修改
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException

browser = webdriver.Firefox()
try:
    browser.get('https://ww.baidu.com')
except TimeoutException:
    print('超时')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('没有找到元素，请核对代码')
finally:
    browser.close()
