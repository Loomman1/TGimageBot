import requests
import json
from fake_headers import Headers
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# HEADERS={"User-Agent": "OPR/112.0.0.0"}
URL = "https://yandex.ru/images/"
# HEADERS={"User-Agent": "Mozilla/5.0"}


class Size:
    def __init__(self):
        self.large = 'large'
        self.medium = 'medium'
        self.small = 'small'


class Preview:
    def __init__(self, url: str,
                 width: int,
                 height: int):
        self.url = url
        self.width = width
        self.height = height
        self.size = str(width) + '*' + str(height)


class Result:
    def __init__(self, title: (str, None),
                 description: (str, None),
                 domain: str,
                 url: str,
                 width: int,
                 height: int,
                 preview: Preview):
        self.title = title
        self.description = description
        self.domain = domain
        self.url = url
        self.width = width
        self.height = height
        self.size = str(width) + '*' + str(height)
        self.preview = preview


class YandexImage:
    def __init__(self):
        self.size = Size()
        self.headers = Headers(headers=True).generate()
        self.version = '1.0-release'
        self.about = 'Yandex Images Parser'

    def search(self, query: str, sizes: Size = 'large') -> list:
        #request = requests.get('https://yandex.ru/images/search',
        # response = requests.get(f"https://ya.ru/images/search?from=tabbar&text=Котики")
        # print(response.status_code)
        #
        # soup = bs4(response.text, 'html.parser')
        # pictures1 = soup.find_all("div", {"class": "SerpList"})
        # print(pictures1)
        # pictures = soup.find_all("div", {"class": "JustifierSkeletonItem JustifierRowLayoutSkeleton-Item"})
        # print(pictures)
        # # for child in soup.recursiveChildGenerator():
        # #     if child.name:
        # #         print(child)
        # response1 = requests.post(f"https://ya.ru/images/search?from=tabbar&text=Котики")
        #
        # # print(response1.text)
        # soup = bs4(response1.text, 'html.parser')
        # pictures1 = soup.find_all("div", {"class": "JustifierSkeletonItem JustifierRowLayoutSkeleton-Item"})
        # print(len(pictures))

        driver = webdriver.Firefox()
        driver.get(f"https://ya.ru/images/search?from=tabbar&text={query.text}")
        print(query.text)
        links =list()
        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "SerpItem")))
            elements=driver.find_elements(By.CLASS_NAME, "ContentImage-Image.ContentImage-Image_clickable")
            print(elements)
        finally:
            print("финали")
            # driver.quit()
        for element in elements:
            links.append(element.get_attribute("src"))
            print(element.get_attribute("src"))
        return links



