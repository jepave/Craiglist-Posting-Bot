from xml.etree.ElementPath import find

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
import os.path

browser: WebDriver = webdriver.Chrome('C://Users//jessi//PycharmProjects//craighlistbot//chromedriver.exe')

browser.get("https://post.craigslist.org/")

# Select Location
browser.find_element_by_class_name('ui-selectmenu-text').click()

browser.find_element_by_xpath('//li[@id="ui-id-341"]').click()

browser.find_element_by_xpath('//button[@name="go"]').click()

# Post Type Page
browser.find_element_by_xpath('//input[@name="id" and @value="so"]').click()

# Category
browser.find_element_by_xpath('//input[@name="id" and @value="76"]').click()

# Main post page
title_area = browser.find_element_by_xpath('//input[@name="PostingTitle" and @id="PostingTitle"]')
title_area.send_keys('Get your website done today')

city = browser.find_element_by_xpath('//input[@name="geographic_area" and @id="geographic_area"]')
city.send_keys('Las Vegas, NV')

postal_code = browser.find_element_by_xpath('//input[@name="postal" and @id="postal_code"]')

postal_code.send_keys(89142)
time.sleep(1)

# main text section
main_text = browser.find_element_by_xpath('//textarea[@name="PostingBody" and @id="PostingBody"]')
main_text = browser.find_element_by_xpath('//textarea[@name="PostingBody" and @id="PostingBody"]')
main_text.send_keys('Performance Solution For Small Businesses')
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys(
    'Unlike those others, we never follow the stereotypical path. We only focus on what it takes and that is all! By educating our clients on digital marketing and how we work, they will be more than satisfied with us as a company.')
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys(
    "Web Development, Business Solutions, and Marketing Management. We do it all so you don't have to think about who does what and you only pay for one service who does it all for you.")
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys(
    'Do not let your business suffer when you can make as much money as you possibly can with a online presence.')
main_text.send_keys(Keys.ENTER)
main_text.send_keys(Keys.ENTER)
main_text.send_keys("Please Call Us at 702-325-0580")

# contact info
email = browser.find_element_by_xpath('//input[@name="FromEMail"]')
email.send_keys('test@gmail.com')

browser.find_element_by_xpath('//input[@name="show_phone_ok" and @value="1"]').click()

phone = browser.find_element_by_xpath('//input[@name="contact_phone"]')
phone.send_keys('702-325-0580')

browser.find_element_by_xpath('//button[@name="go" and @value="continue"]').click()

street = browser.find_element_by_xpath('//input[@name="xstreet0" and @id="xstreet0"]')
street.send_keys('Sahara Ave')
city_location = browser.find_element_by_xpath('//input[@name="city" and @id="city"]')
city_location.send_keys('Las Vegas')

find_location = browser.find_element_by_xpath('//button[@id="search_button"]').click()
time.sleep(1)

location_submit = browser.find_element_by_xpath('//button[@class="continue bigbutton"]').click()

# Send Pictures
browser.find_element_by_xpath('//a[@id="classic"]').click()

add_images: WebElement = browser.find_element_by_xpath('//input[@name="file"]')

img = []
path = '/Users/jessi/PycharmProjects/craighlistbot/random_house/'
valid_image = ['.jpg', '.gif', '.png', '.tga']
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_image:
        continue
    print(f)
    img.append(f'/random_house/{f}')

for i in sorted(img):
    if add_images != False:
        print(os.getcwd() + i)
        add_images.send_keys(os.getcwd() + i)
        add_images = WebDriverWait(browser, 3).until(find)
    else:
        continue

browser.find_element_by_xpath('//button[@value="Done with Images"]').click()
