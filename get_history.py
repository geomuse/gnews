from dataclasses import dataclass
import requests

from bs4 import BeautifulSoup
import os , sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

current_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "..\..")
path = r'c:\Users\boonh\Downloads\genv'
sys.path.append(path)

from notification_bot.telegram_chat import telegram_send
from notification_bot.loguru_notification import loguru_notf
logger = loguru_notf(current_dir)
logger.add('history')

from data_collection_bot.http_status import check_status
import streamlit as st 

# 设置Chrome浏览器驱动路径
driver_path = 'C:/Users/boonh/Downloads/genv/data_collection_bot/geckodriver-v0.33.0-linux64'

@dataclass
class news_download:

    def init_browser(self):
        service = Service(executable_path=driver_path)
        options = webdriver.FirefoxOptions()
        return service , options

    def run(self,url):
        # service , options = self.init_browser()
        browser = webdriver.Firefox()
        browser.get(url)

    def get(self,url):
        response = requests.get(url)
        if check_status(response.status_code) in [200]:
            soup = BeautifulSoup(response.text,'html.parser')
            title = soup.find_all('ul',{'class':'list'})
            text = f"{title[0].text}"
            text = text.split()

        for _ , __ in enumerate(text):
            print(_ , __)    
        
if __name__ == '__main__':

    url = 'https://news.ltn.com.tw/list/breakingnews/world'
    nd = news_download()
    nd.get(url)

    ts = telegram_send()
    ts.send_message('200.')