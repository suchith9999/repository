from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument("--headless")  # Enable only if needed
# chrome_options.add_argument("--headless=new")  # Modern headless mode
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# Launch browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# Open NSE stock page (example symbol)
url = "https://www.nseindia.com/get-quotes/equity?symbol=ATHERENERG"
driver.get(url)

# Wait until price loads
wait = WebDriverWait(driver, 15)
price_element = wait.until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='midBody']/div[2]/div[2]/div/div[1]/div/div[1]"))
)

# Extract price
price = price_element.text
print("Current Price:", price)

driver.quit()
