# pip install webdriver-manager

import asyncio
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


# Normal (blocking) Selenium function
def open_website(url):
    options = Options()
    # options.add_argument("--headless=new")
    # chrome_options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)
    wait = WebDriverWait(driver, 15)
    price_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='midBody']/div[2]/div[2]/div/div[1]/div/div[1]"))
    )
    # Extract price
    price = price_element.text
    print("Current Price:", price)
    from sound import playsound
    # driver.quit()
    # setprice = float(716.00)
    # if setprice >= float(price):
    #     sound.runner()
    # else:
    #     print('price is greater then set price')


# Async wrapper
async def run_task(url, executor):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(executor, open_website, url)
    print(f"{url} → {result}")


async def main():
    urls = [
        "https://www.nseindia.com/get-quote/equity/ATHERENERG/Ather-Energy-Limited",
        "https://www.nseindia.com/get-quote/equity/KAYNES/Kaynes-Technology-India-Limited"
    ]

    with ThreadPoolExecutor(max_workers=2) as executor:
        tasks = [run_task(url, executor) for url in urls]
        await asyncio.gather(*tasks)

while True:
    asyncio.run(main())
