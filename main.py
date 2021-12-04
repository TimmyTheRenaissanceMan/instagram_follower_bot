from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()

action = webdriver.common.action_chains.ActionChains(driver)

# Enter your credentials
INSTA_ACCT = "YOUR_INSTAGRAM_USERNAME"
INSTA_PASS = "YOUR_INSTAGRAM_PASSWORD"

# Enter Username of the account, whose followers will be targeted
ACCT_TO_FOLLOW = "USERNAME_TO_FOLLOW"


#go to instagram
driver.get("https://www.instagram.com/")

#accept cookies
driver.find_element(By.CSS_SELECTOR, ".aOOlW.bIiDR").click()
time.sleep(1)

#login
driver.find_element(By.NAME, "username").send_keys(INSTA_ACCT)
driver.find_element(By.NAME, "password").send_keys(INSTA_PASS)
action.send_keys(Keys.ENTER).perform()
time.sleep(2)

#open the account
driver.get(f"https://www.instagram.com/{ACCT_TO_FOLLOW}/followers/")
time.sleep(1)

#get follower list
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep(1)


#start following
while True:
    buttons = driver.find_elements(By.CSS_SELECTOR, ".sqdOP.L3NKy.y3zKF")
    buttons[0].click()
    time.sleep(1.5)
