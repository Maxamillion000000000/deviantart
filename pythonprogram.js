#import requersts, os, bs4
comicElem = soup.select('#dev-content-full img')
if comicElem == []:
    print('Could not find comic image.')
else:
    comicUrl = comicElem[0].get('src')    //add simulated click step to increase image to maximum size, else continue
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()
imageFile = open(os.path.join('deviantbackup', os.path.basename(comicUrl)), 'wb')
for chunk in resizeBy.iter_content(100000):
    imageFile.write(chunk)
    imageFile.close()
nextLink = soup.select('a[rel="prev"]')[0] //#need to change to Deviantart's "next" button
url = 'https://capi-larry.deviantart.com/favourites/' + nextLink.get('href')
print('Done')