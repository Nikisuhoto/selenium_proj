from selenium import webdriver
import time as tm


n = int(input("Time to sleep?"))

driver = webdriver.Chrome()
driver.get("https://www.google.com")

tm.sleep(n)

# <button id="L2AGLb" class="tHlp8d" data-ved="0ahUKEwiohtOFm7eLAxU7VfEDHbmBHpQQiZAHCIAB">
# <div class="QS5gu sy4vM" role="none">Приемане на всички</div></button>

element = driver.find_element("id", "L2AGLb")
element.click()

tm.sleep(n)

# <textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus=""
# title="Търсене" value="" aria-label="Търс." placeholder="" aria-autocomplete="both"
# aria-expanded="true" aria-haspopup="false" autocapitalize="off" autocomplete="off"
# autocorrect="off" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false"
# jsaction="paste:puy29d" data-ved="0ahUKEwi-hfyEn7eLAxWiavEDHY6xGboQ39UDCAQ" aria-activedescendant=""
# style=""></textarea>

search = driver.find_element("id", "APjFqb")
search.send_keys("Николай Райков")
tm.sleep(n)

# <input class="gNO89b" value="Google Търсене" aria-label="Google Търсене" name="btnK" role="button" tabindex="0"
# type="submit" data-ved="0ahUKEwjnnuK3lbeLAxWzklYBHVHrFQcQ4dUDCB0">

element = driver.find_element("name", 'btnK')
element.click()

tm.sleep(n)


