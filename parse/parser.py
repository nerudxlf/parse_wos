from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Parser:
    def __init__(self, path: str, link_profile: str = None):
        self._path = path
        self.__link_profile = link_profile

    def _get_chrome(self):
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(executable_path=self._path, chrome_options=options)

    def __get_soup(self):
        browser = self._get_chrome()
        browser.get(self.__link_profile)
        if browser.title != "Publons.com | Not found":
            try:
                WebDriverWait(browser, 5).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@class='left-bar-figure-help-icon']")))
            except:
                pass
        return BeautifulSoup(browser.page_source, "lxml")

    def parse_name(self, soup=None):
        if not soup:
            soup = self.__get_soup()
        try:
            return soup.find("div", {"class": "researcher-card-names"}).h2.text
        except AttributeError:
            return "Not found"
        except IndexError:
            return "Not found"

    def parse_h_index(self, soup=None):
        if not soup:
            soup = self.__get_soup()
        try:
            h_index = soup.find_all("p", {"class": "researcher-card-h-index-val"})[0].text
            if len(h_index) > 1:
                return h_index[0:-2]
            return h_index
        except AttributeError:
            return "Not found"
        except IndexError:
            return "Not found"

    def parse_publication(self, soup=None):
        if not soup:
            soup = self.__get_soup()
        try:
            return soup.find_all("div", {"class": "left-bar-figure"})[0].p.text
        except AttributeError:
            return "Not found"
        except IndexError:
            return "Not found"

    def parse_total_time_cited(self, soup=None):
        if not soup:
            soup = self.__get_soup()
        try:
            return soup.find_all("div", {"class": "left-bar-figure"})[1].p.text
        except AttributeError:
            return "Not found"
        except IndexError:
            return "Not found"
