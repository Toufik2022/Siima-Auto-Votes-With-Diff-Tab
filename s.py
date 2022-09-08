from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread, Barrier


def func(barrier):
    
    driver = webdriver.Chrome()

    driver.get("https://siima.in/index.php/siima-votings-2022/") 
    
    time.sleep(8) #if your internet connection is good then change 8 to 7 

    driver.find_element_by_id("elementor-tab-title-1422").click()

    time.sleep(1)

    driver.find_element_by_css_selector('#field_irk0d-0').click()

    time.sleep(1)

    driver.find_element_by_css_selector('#field_mrqd2-2').click()
    
    time.sleep(1)

    driver.find_element_by_css_selector('#field_zx1nm-3').click()

    time.sleep(1)

    driver.find_element_by_css_selector('#form_kanada > div > fieldset > div > div.frm_submit > button').click()

    driver.close()
    
    #the below code was used from internet source for run

    barrier.wait()

    b.click()

number_of_threads = 10 #i entered 10 change to your required if your data is unlimited means change 10 to 20 tabs will open and vote automatically and close 

barrier = Barrier(number_of_threads)

threads = []

for _ in range(number_of_threads):
    t = Thread(target=func, args=(barrier,)) 
    t.start()
    threads.append(t)

for t in threads:
    t.join()

