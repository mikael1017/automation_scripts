
# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(
    executable_path="/Users/jaewoocho/Desktop/personal_projects/automation_scripts/lol_champion_search/chromedriver")
driver = webdriver.Chrome(service=service)
champion_name = ""
# ask user for champion name
while champion_name == "":
    champion_name = input("챔피언 이름을 입력하세요: ")
    if champion_name == "":
        print("챔피언 이름을 입력하세요.")


driver.get("https://www.lolvvv.com/ko/champion")


input_element = driver.find_element(
    By.CSS_SELECTOR, 'input[placeholder="챔피언 검색"].w-full')
input_element.send_keys(champion_name + Keys.ENTER)

link_element = driver.find_element(By.CSS_SELECTOR, 'table tbody a')


driver.get(link_element.get_attribute("href"))

kr_button = driver.find_element(By.XPATH, '//button[text()="KR"]')
kr_button.click()

time.sleep(10)


# %%
