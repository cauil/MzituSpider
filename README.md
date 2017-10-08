# MzituSpider
A Spider use to download photos for mzitu.com, support img set and category three ways.

## Install

python3 environment, not test in python2.

```
pip install -r requirements.txt
```

## Usage

The file is download to dir './downloads/' default.

```
from spider import Spider
s = Spider()
```

download a single img. just:
```
s.down_img('http://i.meizitu.net/2017/09/23b01.jpg')
```

download a img set. ie: `http://www.mzitu.com/103636`. just:
```
s.down_img_set(103636)
```

downlaod a category. just:
```
s.down_albums('http://www.mzitu.com/xinggan/')
```
if u want to download all the pagination of category, just:
```
s.down_albums('http://www.mzitu.com/xinggan/', True)
```
