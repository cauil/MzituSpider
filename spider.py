import os
import re
import time
import requests
from bs4 import BeautifulSoup

class Spider(object):
    def __init__(self):
        super(Spider, self).__init__()
        self.base_url = 'http://www.mzitu.com/'

    def down_albums(self, url, recursive=False):
        pagination = 1
        if recursive:
            res = requests.get(url)
            html = res.text
            soup = BeautifulSoup(html, "html.parser")
            pagination = soup.select('.page-numbers')[-2].text

        print('')
        print('>>>>>>start download albums ' + url + '<<<<<<<<')
        print('')
        for i in range(1, int(pagination)+1):
            self.down_pagination(url, str(i))
        print('')
        print('>>>>>>download albums ' + url + ' complete<<<<<<<<')
        print('')

    def down_pagination(self, albums_url, pagination):
        pagination = str(pagination)
        res = requests.get(albums_url + 'page/' + pagination)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        albums = [re.split('/', a['href'])[-1] for a in soup.select('#pins > li > span > a')]

        print('')
        print('>>>>>>start download pagination ' + pagination + '<<<<<<<<')
        print('')
        for album in albums:
            self.down_img_set(album)
        print('')
        print('>>>>>>download pagination ' + pagination + ' complete<<<<<<<<')
        print('')


    def down_img_set(self, *kwg):
        for pic_set in kwg:
            pic_set = str(pic_set)
            res = requests.get(self.base_url+pic_set)
            html = res.text
            soup = BeautifulSoup(html, "html.parser")
            main_image = soup.select('.main-image')

            if not len(main_image):
                print('***warning***: picture set ' + pic_set + ' not exist')
                return

            (title, number) = self.get_title_number(soup)
            base_dir = self.make_dir(title, pic_set)

            print('')
            print('>>>>>start download set ' + pic_set + '<<<<<<<<')
            print('')

            for i in range(1, int(number)+1):
                page_url = self.base_url + pic_set + '/' + str(i)
                src = self.get_imgurl(page_url)
                self.down_img(src, str(i), base_dir)
                time.sleep(5)

            print('')
            print('>>>>>download set' + pic_set + ' complete<<<<<<<')
            print('')

    def get_title_number(self, soup):
        html_a = soup.select('div .pagenavi a')
        number = html_a[len(html_a)-2].select('span')[0].string
        title = soup.select('h2.main-title')[0].string

        return (title, number)

    def make_dir(self, title, pic_set):
        pic_set = str(pic_set)
        dir_name = './downloads/' + pic_set + '-' + title + '/'
        if(not os.path.exists(dir_name)):
            os.makedirs(dir_name)
        return dir_name

    def get_imgurl(self, page_url):
        html = requests.get(page_url).text
        sp = BeautifulSoup(html, "html.parser")
        src = sp.select('.main-image img')[0]['src']
        return src

    def down_img(self, src, number='1', base_dir='./downloads/'):
        if(not os.path.exists(base_dir)):
            os.makedirs(base_dir)
        number = str(number)
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'Pragma': 'no-cache',
                'Referer': 'http://www.mzitu.com'
                }

        res = requests.get(src, headers=headers, stream=True)
        file_name = ''.join([base_dir, '0'+number if len(number) < 2 else number, '.jpg'])
        print('=====>start download ' + file_name)
        with open(file_name, 'wb') as fd:
            for chunk in res.iter_content(128):
                fd.write(chunk)
        print('<=====download pic '+number+' success')


if __name__ == '__main__':
    s = Spider()
    # for page in range(104746, 104749):
        # s.down_img_set(str(page))
    s.down_albums('http://www.mzitu.com/xinggan/')
