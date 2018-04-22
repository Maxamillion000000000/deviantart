import requests, os, bs4
url = 'https://capi-larry.deviantart.com/favourites/70883670/Foe-Toe-Sculpt'
os.makedirs('devtestbackup', exist_ok=True)
while not url.endswith('#'):
    print ('downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
#click first thumbnail link in gallery, to go to first artpage, before beginning download of images and clicks to the next page in the gallery 
soup.select('https://t00.deviantart.net/r5Dh5yQLZRPw9Joe_uOjrLe2EsU=/fit-in/700x350/filters:fixed_height(100,100):origin()/pre00/b4aa/th/pre/f/2018/064/7/5/hollow_swing01_by_shocksplash-dc50xiu.jpg')
comicElem = soup.select('#dev-content-full img') #'#dev-view-deviation'.
if comicElem == []:
    print('Could not find comic image.')
else:
    comicUrl = comicElem[0].get('src')    #add simulated click step to increase image to maximum size else continue
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()
imageFile = open(os.path.join('devtestbackup', os.path.basename(comicUrl)), 'wb')
for chunk in res.iter_content(100000):
    imageFile.write(chunk)
    imageFile.close()
nextLink = soup.select('a[rel="Next"]')[0] #need to change to Deviantart's "next" button
url = 'https://t00.deviantart.net/r5Dh5yQLZRPw9Joe_uOjrLe2EsU=/fit-in/700x350/filters:fixed_height(100,100):origin()/pre00/b4aa/th/pre/f/2018/064/7/5/hollow_swing01_by_shocksplash-dc50xiu.jpg' + nextLink.get('href')
print('Done')