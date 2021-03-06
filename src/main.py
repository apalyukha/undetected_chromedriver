import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (X11; Ubuntu;'
                     ' Linux x86_64; rv:84.0)'
                     ' Gecko/20100101 Firefox/84.0')
options.add_argument('--disable-blink-features=AutomationControlled')

# DeprecationWarning:
# driver = webdriver.Chrome(
#     executable_path="../chromedriver",
#     options=options
# )

# new:
s = Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=s, options=options)

try:
    driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/'
               'chrome-headless-test.html')
    # driver.get('https://www.vindecoderz.com/EN/check-lookup/ZDMMADBMXHB001652')
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
