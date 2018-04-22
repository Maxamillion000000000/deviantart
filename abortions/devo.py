import requests, os, bs4 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

browser = webdriver.Firefox()
browser.get('https://www.deviantart.com/users/login?ref=https://capi-larry.deviantart.com/favourites/68337927/Overflow')
#how to pass age gate, even when logged in interferes with find_element
inputElement = browser.find_element_by_id('login_username')
inputElement = browser.find_element_by_id('login_username')
inputElement.send_keys("Capi-larry")
inputElement = browser.find_element_by_id('login_password')
inputElement.send_keys("halshlonger")
inputElement.submit()
def wait_click(class_name):
    try:
        thumb_click =WebDriverWait(browser, 1).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, class_name)
            )
        )
       
        # thumb_click = browser.find_element_by_class_name('torpedo-thumb-link')
        EC.element_to_be_clickable(thumb_click)
        thumb_click.click()
    except: 
        print('still cant find it')

while browser.current_url != 'https://capi-larry.deviantart.com/art/Merchant-of-Venus-335561983':
    wait_click('torpedo-thumb-link')
# try:
#     # EC.element_to_be_clickable()
#     thumb_click = WebDriverWait(browser,1).until(browser.find_element_by_class_name,'torpedo-thumb-link')
#     thumb_click.click()
# except:
#     TimeoutException: print('waiting for first thumbnail to load')

def downloadImage(img_url): 
    print('Downloading image %s...' % (img_url))
    res = requests.get(img_url)
    res.raise_for_status()
    imageFile = open(os.path.join('devOverflow', os.path.basename(img_url)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

next_is_disabled = True

while next_is_disabled == True: 
    url = browser.current_url
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    comicElem = soup.select('img.dev-content-full') 
    if comicElem == []:
        print('ERROR: Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')   
        downloadImage(comicUrl)
        base_selector = 'a.gmbutton2.gmhuge.gmbutton2top.ntlast.minibrowse_next'
        try:
            linkElem = browser.find_element_by_css_selector(base_selector + '.disabled')
            next_is_disabled = False
        except:
            linkElem = browser.find_element_by_css_selector(base_selector)
            linkElem.click()
print('Done')
browser.quit