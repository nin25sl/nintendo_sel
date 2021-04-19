import os
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import traceback

def setup_class(cls):
    cls.driver = webdriver.Chrome(ChromeDriverManager().install())

def set_driver(driver_path, headless_flg):
    options = ChromeOptions()
    if headless_flg == True:
        options.add_argument('--headless')
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          
    Chrome(executable_path=os.getcwd() + "/" + driver_path, options=options)
    ChromeDriverManager().install()
    return Chrome(executable_path=os.getcwd() + "/" + driver_path, options=options)

def mysearch_keyword(driver):
    driver.get("https://store-jp.nintendo.com/customize/switch/")
    time.sleep(5)

def writelog(logCentents):
    path = './log.txt'
    with open(path, mode = 'a') as f:
        f.write(logCentents)

def main():
    if os.name == 'nt': 
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': 
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

    driver.get("https://store-jp.nintendo.com/customize/switch/")
    # driver.get("https://store-jp.nintendo.com/customize/lite/?pid=HDH_S_PAZAA")
    time.sleep(5)
    
    try:    
        button_exist = driver.find_element_by_class_name('productDetailSwitchCustomize--addToCart__button')
        print("Can buy it")

    except:
        button_notexist = driver.find_element_by_class_name('productDetailSwitchCustomize--addToCart__button--soldOut')
        print("Cant by it")
        driver.quit()
        return False

    driver.quit()

    return True
if __name__ == "__main__":
    main()