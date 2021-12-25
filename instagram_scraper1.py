from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import pandas as pd
from dateutil import tz



##  assigning a driver 
class InstagramBot():
    def __init__(self, email, password):
        
        self.browser = webdriver.Chrome(r"C:\Users\91976\PycharmProjects\firstsele\drivers\chromedriver.exe")
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        print(self.browser.title)
        time.sleep(1)
        emailInput = self.browser.find_element_by_xpath("//input[@name='username']")
        passwordInput = self.browser.find_element_by_xpath("//input[@name='password']")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)


##  logging to instagram and navigating to feed
bot = InstagramBot('perc.eptrons', 'Myntra2020')
wait = WebDriverWait(bot.browser, 10)
bot.signIn()
time.sleep(3)
okay = bot.browser.find_element_by_class_name("sqdOP.yWX7d.y3zKF")
okay.send_keys(Keys.RETURN)
time.sleep(2)
notnow = bot.browser.find_element_by_class_name("aOOlW.HoLwm")
notnow.send_keys(Keys.RETURN)
time.sleep(1)


names = []
profiles = []
datetimelist = []
SCROLL_PAUSE_TIME = 1.6
#Get scroll height
 
last_height = bot.browser.execute_script("return document.body.scrollHeight")
for i in range (5):
    name1 = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "sqdOP.yWX7d._8A5w5.ZIAjV"))) ## geting proflie names
    date1 = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME , "_1o9PC.Nzb55")))             ## geting dates of posts  
    for n in name1:
        profile = n.get_attribute("text")
        profiles.append(profile)
    # Scroll down to bottom
    for d in date1:
        date = d.get_attribute("datetime")
        datetimelist.append(date)
    
      # Scroll down to bottom
    bot.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = bot.browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    
 
 # making csv
new_profile = []
for profile in profiles:
    profile = profile.replace("See All","")
    if profile != "":
        new_profile.append(profile)
df1 = pd.DataFrame(list(zip(new_profile)), 

               columns=['proflie_name'])
df1.to_csv('proflies.csv')

new_date = []
for date in datetimelist:
    date = date.replace("T"," ")[:-5]
    utc = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Asia/Kolkata')
    utc = utc.replace(tzinfo=from_zone)
    # Convert time zone
    central = utc.astimezone(to_zone)
    new_date.append(central)


df = pd.DataFrame(list(zip(new_date)), 

               columns=['datetimelist'])
df.to_csv('datetime.csv')

with open('profile.txt', 'w') as filehandle:
    for profile in new_profile :
        filehandle.write('%s,'% profile)
