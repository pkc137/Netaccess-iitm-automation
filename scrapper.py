


# Download selenium library

# install selenium by typing "pip instal selenium" in terminal

from selenium import webdriver
# Ubuntu - install chromium chrome driver by typing "sudo apt-get install chromium-chromedriver" 

chromedriver = "/usr/bin/chromedriver" # Driver loacation can be found by typing "whereis chromedriver"

driver = webdriver.Chrome(chromedriver)

# Widnows version- Download chrome driver from "https://chromedriver.chromium.org/"

# Unzip the file and copy the file into the same folder with the script.

#driver = webdriver.Chrome() #Remove the hash before this line

driver.get('https://netaccess.iitm.ac.in/account/login')

username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('CE19S020') # Enter your roll number

pwd = driver.find_element_by_xpath('//*[@id="password"]')
pwd.send_keys('pswd') # Enter your ldap password

# Finding and clicking buttons 
loginbutton = driver.find_element_by_xpath('//*[@id="submit"]')
loginbutton.click() 

approvebtn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/a/span')
approvebtn.click()

onedaybtn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/form/div[2]/label')
onedaybtn.click()

authorizebtn = driver.find_element_by_xpath('//*[@id="approveBtn"]')
authorizebtn.click()

driver.close()

print("lauda")

# Using task schedular in windows the script can be scheduled to run every day. "https://www.youtube.com/watch?v=Oh1lHFkuYJY"

# Use Cron in Linux to schedule the script "https://betterprogramming.pub/scheduling-python-scripts-on-linux-fa0d28a8f915"
