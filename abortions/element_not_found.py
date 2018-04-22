import requests, os, bs4 
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
browser = webdriver.Firefox()
browser.get('https://www.deviantart.com/users/login?ref=https://capi-larry.deviantart.com/favourites/')

# if browser.current_url == 'https://www.deviantart.com/users/login?ref=https://capi-larry.deviantart.com/favourites/':
inputElement = browser.find_element_by_id('login_username')
inputElement = browser.find_element_by_id('login_username')
inputElement.send_keys("Capi-larry")
inputElement = browser.find_element_by_id('login_password')
inputElement.send_keys("halshlonger")
inputElement.submit()

while browser.current_url != 'https://capi-larry.deviantart.com/favourites/63976349/Art-Objects':
     try:
          browser.find_element_by_class_name('tv150').click()
     except: 
        print('still cant find it')

# try:
#     collection_clicker = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Art Objects'))).click()
# except TimeoutException:
#     print('cant find my dick with both hands!')
# collection_clicker.click()
    
# def downloadImage(img_url): 
#     print('Downloading image %s...' % (img_url))
#     res = requests.get(img_url)
#     res.raise_for_status()
#     imageFile = open(os.path.join('dev_favourites', os.path.basename(img_url)), 'wb')
#     for chunk in res.iter_content(100000):
#         imageFile.write(chunk)
#     imageFile.close()

# next_is_disabled = False

# while next_is_disabled == False: 
#     url = browser.current_url
#     res = requests.get(url)
#     res.raise_for_status()
#     soup = bs4.BeautifulSoup(res.text)
#     comicElem = soup.select('img.dev-content-full') 
#     if comicElem == []:
#         print('ERROR: Could not find comic image.')
#     else:
#         comicUrl = comicElem[0].get('src')   
#         downloadImage(comicUrl)
#         base_selector = 'a.gmbutton2.gmhuge.gmbutton2top.ntlast.minibrowse_next'
#         try:
#             linkElem = browser.find_element_by_css_selector(base_selector + '.disabled')
#             next_is_disabled = True
#         except:
#             linkElem = browser.find_element_by_css_selector(base_selector)
#             linkElem.click()
# print('Done')
# browser.quit