import time

import undetected_chromedriver as uc

try:
    driver = uc.Chrome()
    # driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    driver.get('https://www.vindecoderz.com/EN/check-lookup/ZDMMADBMXHB001652')
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
