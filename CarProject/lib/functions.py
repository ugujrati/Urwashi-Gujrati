import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class CarProjectClient:
    def __init__(self):
        self.reg = ''

    def get_num_plates(self):
        with open('car_input.txt') as f:
            lines = f.readlines()
            text = str(lines)
            self.reg = re.findall('[A-Z]{2}[0-9]{2}[A-Z]{3}|[A-Z]{2}[0-9]{2}\s[A-Z]{3}', text)
            return self.reg

    def get_veh_details(self, reg_no):
        driver = webdriver.Chrome()
        driver.get("https://cartaxcheck.co.uk/")
        driver.maximize_window()
        time.sleep(2)
        expected_title = 'Free Car Check'
        if expected_title not in driver.title:
            raise Exception(f'name {expected_title} not found')
        reg_input = driver.find_element_by_id("vrm-input")
        reg_input.send_keys(reg_no)
        reg_input.send_keys(Keys.ENTER)
        time.sleep(2)

        veh_reg = driver.find_element_by_xpath(
            """//*[@id="m"]/div[2]/div[5]/div[1]/div/span/div[2]/dl[1]/dd""").text
        veh_make = driver.find_element_by_xpath(
            """//*[@id="m"]/div[2]/div[5]/div[1]/div/span/div[2]/dl[2]/dd""").text
        veh_model = driver.find_element_by_xpath(
            """//*[@id="m"]/div[2]/div[5]/div[1]/div/span/div[2]/dl[3]/dd""").text
        veh_colour = driver.find_element_by_xpath(
                """//*[@id="m"]/div[2]/div[5]/div[1]/div/span/div[2]/dl[4]/dd""").text
        veh_year = driver.find_element_by_xpath(
                """//*[@id="m"]/div[2]/div[5]/div[1]/div/span/div[2]/dl[5]/dd""").text

        get_details = f'{veh_reg},{veh_make},{veh_model},{veh_colour},{veh_year}'
        driver.close()
        return get_details

    def verify_output(self, veh_info):
        with open('car_output.txt') as f:
            if veh_info in f.read():
                print(f'{veh_info} matches to car_output.txt')
            else:
                print(f'\033[91m{veh_info} DOES NOT match to car_output.txt\033[0m')
