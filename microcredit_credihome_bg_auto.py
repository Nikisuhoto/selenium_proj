from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time as tm

n = int(input("Time to sleep?"))

driver = webdriver.Chrome()
driver.get("https://old-microcredit.credihome.bg/")
tm.sleep(n)

# <input class="StandardInput StandardInput-is-block EmailInput" type="email"
# name="email">

element = driver.find_element("name", "email")
element.send_keys("niki@dron.bg")
tm.sleep(n)
element.send_keys(Keys.ENTER)

tm.sleep(30)
# number_code = int(input("Number code:"))

try:
    element = driver.find_element("name", "code")

    tm.sleep(n)
    element.send_keys(Keys.ENTER)

except:
    pass

### id="AmountIndex" max="43" min="0" name="AmountIndex" step="1"
# data-val-required="The MonthsIndex field is required." id="MonthIndex" max="11" min="0" name="MonthsIndex"

slider = driver.find_element("id", "MonthIndex")
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(10, 0).release().perform()
# [3,4,5,6,7,8,9,10,11,12,15,18]
tm.sleep(n)

# id="email_txt" name="Email" placeholder="Имейл"

element = driver.find_element("id", "email_txt")
element.send_keys("niki@dron.bg")
tm.sleep(n)

# id="phone_txt" name="Phone" placeholder="Телефон"

element = driver.find_element("id", "phone_txt")
element.send_keys("0878734442")
tm.sleep(n)

# <button data-action="save" type="submit" id="fix-form-btn">Вземи сега</button>

element = driver.find_element("id", "fix-form-btn")
element.click()
tm.sleep(n*5)
