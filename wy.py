from selenium import webdriver
import csv

# 网易云音乐的歌单第一页的url
url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
# 用PhantomJS接口创建一个selenium的webDriver
driver = webdriver.PhantomJS()


# 准备好存储歌单的csv文件
csv_file = open('D:\wangyi\playlist.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['标题','播放次数','作者','链接'])

# 解析每一页，直到下一页为空
while url != 'javascript:void(0)':
    # 用webdriver加载页面
    driver.get(url)
    # 切换到内容的iframe
    driver.switch_to.frame('contentFrame')
    # 定位歌单标签
    data = driver.find_element_by_id('m-pl-container').find_elements_by_tag_name('li')
    # 解析一页中的所有歌单
    for i in range(len(data)):
        # 获取播放数
        nb = data[i].find_element_by_class_name('nb').text
        if '万' in nb and int(nb.split('万')[0]) > 5:
            # 获取播放数大于500万的歌单封面
            msk = data[i].find_element_by_class_name('msk')
            # 获取作者
            author = data[i].find_element_by_xpath('.//a[@class="nm nm-icn f-thide s-fc3"]').text
            # 把封面上的标题和链接连同播放次数一起写到文件中
            writer.writerow([msk.get_attribute('title'),nb,author,msk.get_attribute('href')])

    # 定位下一页的url
    url = driver.find_element_by_css_selector('a.zbtn.znxt').get_attribute('href')
csv_file.close()

