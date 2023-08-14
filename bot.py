from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time
import os
import json

SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/home"

#install chrome driver

admin_info = os.getenv('ADMIN_JSON_INFO')
with open(admin_info, 'r') as file:
    contents = file.read()
    admin_json_info = json.loads(contents)

TWITTER_ID = admin_json_info['twitter']['my_account']['id']
TWITTER_PASSWORD = admin_json_info['twitter']['my_account']['password']

#install chrome driver
chrome_driver_path = admin_json_info['chrome_driver_path']
os.environ['webdriver.chrome.driver'] = chrome_driver_path

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.download = 0
        self.upload = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(60)                 #You can change the time sleeping to make sure the bot get internet speed value.
        down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].style.display = 'block';",
                              down)
        self.download = down.text

        up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].style.display = 'block';",
                              up)
        self.upload = up.text


    def tweet_at_provider(self):
        # options = Options()
        # options.add_experimental_option('detach', True)
        # self.driver = webdriver.Chrome(options=options)

        self.driver.get(TWITTER_URL)
        time.sleep(3)
        id = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        id.send_keys(TWITTER_ID)
        next = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        time.sleep(3)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        time.sleep(5)

        #You can write if statement to make bot write complaining tweet if the current internet speed value goes down a specific value. (the standard internet speed you set).

        tweet = f"Hey internet provider, why is my internet speed {self.download}down/{self.upload}up when I pay for 150down/10up?"

        write_tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        time.sleep(1)
        write_tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        write_tweet.send_keys(tweet)
        time.sleep(2)
        upload_twit = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span').click()
        time.sleep(2)






