from ..spider import Spider

s = Spider()

s.down_img('http://i.meizitu.net/2017/09/23b01.jpg')
s.down_img_set(103636)
s.down_albums('http://www.mzitu.com/xinggan/', True)
