from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from dbo.teacher import DBOTeacher
from parse.parser import Parser


class ParseList(Parser):
    def parse(self, arr_link: list) -> list:
        browser = self._get_chrome()
        return_arr = []
        for i in arr_link:
            browser.get("http://www.researcherid.com/rid/" + i)
            if browser.title != "Publons.com | Not found":
                try:
                    # if element not found, wait 7 second
                    WebDriverWait(browser, 7).until(
                        EC.visibility_of_element_located((By.XPATH, "//*[@class='left-bar-figure-help-icon']")))
                except:
                    pass
            soup = BeautifulSoup(browser.page_source, 'lxml')
            name = self.parse_name(soup)
            h_index = self.parse_h_index(soup)
            publication = self.parse_publication(soup)
            total_time_cited = self.parse_total_time_cited(soup)
            teacher = DBOTeacher(name, publication, total_time_cited, h_index)
            return_arr.append(teacher)
        return return_arr
