import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Pragma': 'no-cache',
        'Referer': 'http://www.mzitu.com'
        }
res = requests.get('http://i.meizitu.net/2017/10/06c03.jpg', headers=headers, stream=True)

with open('./1.jpg', 'wb') as fd:
   for chunk in res.iter_content(128):
       fd.write(chunk)
