import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
import json


def get_html_page():
    url = 'https://myfin.by/crypto-rates'
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path=f'D:\pythonProject3\chromedriver.exe', options=options)
    try:
        driver.get(url=url)
        time.sleep(5)
        print('Зашёл на страницу')
        html_page = driver.page_source
        with open('htmlpage.html', 'w') as file:
            file.write(html_page)

    except Exception:
        print(Exception)

    finally:
        driver.close()
        driver.quit()


def write_json_donecurrency():
    currency = []
    with open('htmlpage.html', 'r') as file:
        htmlpg = file.read()

    soup = BeautifulSoup(htmlpg, 'lxml')
    all_currency = soup.find('tbody', class_='table-body')
    currency1 = soup.find_all('tr', class_='odd')
    for c1 in currency1:
        name = c1.find('a', class_='s-bold').text
        price = c1.find('div', class_='crypto_iname hidden-xs').find_next('td').text
        capitalistic = c1.find('td', class_='hidden-xs').text
        currency.append({
            'name': name,
            'price': price,
            'capital': capitalistic
        })

    with open('donecurrency.json', 'w', encoding='utf8') as file:
        json.dump(currency, file, indent=4, ensure_ascii=False)
