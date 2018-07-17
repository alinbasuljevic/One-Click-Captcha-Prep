from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = input('Enter Your Email: ')
password = input('Enter Your Password: ')

def main_function():
    driver = webdriver.Chrome()
    driver.get('https://www.gmail.com')
    driver.find_element_by_id('identifierId').send_keys(email)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
    print ('Successfully logged into Gmail!...')
    time.sleep(7)
    print ('Starting Youtube Search on Google...')
    driver.get('https://www.google.com')
    time.sleep(4)
    driver.find_element_by_id('lst-ib').send_keys('1 Hour Long Youtube Videos' + Keys.RETURN)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[3]/div/div/h3/a').click()
    print ('Found Youtube Video...')
    print ('Watching Youtube Video ;)')
    time.sleep(25)
    print ('Finished Watching Youtube Video!')
    print ('')
    print ('Starting Randomized Google Searches...')

    driver.get('https://www.google.com')
    time.sleep(4)
    search_engine = driver.find_element_by_id('lst-ib')
    search_engine.send_keys('Elephants in the Wild' + Keys.RETURN)#if you want to edit the searches
    driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[2]/div/div/h3/a').click()
    time.sleep(10)

    driver.get('https://www.google.com')
    time.sleep(4)
    search_engine = driver.find_element_by_id('lst-ib')
    search_engine.send_keys('Gucci Gang Lil Pump' + Keys.RETURN)#if you want to edit the searches
    driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[2]/div/div/h3/a').click()
    time.sleep(20)

    driver.get('https://www.google.com')
    time.sleep(4)
    search_engine = driver.find_element_by_id('lst-ib')
    search_engine.send_keys('Lions in the Wild' + Keys.RETURN) #if you want to edit the searches
    driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[2]/div/div/h3/a').click()
    time.sleep(15)

    driver.get('https://www.google.com')
    time.sleep(4)
    search_engine = driver.find_element_by_id('lst-ib')
    search_engine.send_keys('Kayne is a Bitch' + Keys.RETURN)#if you want to edit the searches
    driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[2]/div/div/h3/a').click()
    time.sleep(10)

    print (email +' is 1-Click Captcha Prepped!')
    print ('')
    
    
    
start_time = time.time()
main_function()
print('Email prepped in ' + "--- %s seconds ---" % (time.time() - start_time))
    
    
    






