from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import time as tm

n = int(input("Time to sleep?"))

driver = webdriver.Chrome()
driver.get("https://old-microcredit.credihome.bg/")
tm.sleep(n)


# <input class="StandardInput StandardInput-is-block EmailInput" type="email" required="" placeholder="example@email.com"
# spellcheck="false" autocomplete="off" autocapitalize="none" autofocus="" name="email">

element = driver.find_element("name", "Email")
element.send_keys("niki@dron.bg")
tm.sleep(n)
element.send_keys()
element.send_keys(Keys.ENTER)


# <button type="submit" form="totp-form" class="Button Button-is-block Button-is-juicy Button-uses-org-theme-accent-color">


# <input class="StandardInput StandardInput-is-block StandardInput-is-code StandardInput-is-entry-code" type="text"
# required="" placeholder="000000" spellcheck="false" autocomplete="off" autocapitalize="none" autofocus=""
# name="code" inputmode="numeric" pattern="\d{6}">


# <input type="text" name="q" value="" id="search_q">
# <input data-val="true" data-val-maxlength="Имейлът ви не може да е по-дълъг от 50 символа" data-val-maxlength-max="50"
# data-val-regex="Моля въведете валиден имейл."
# data-val-regex-pattern="^(?:[A-z0-9!#$%&amp;'*+/=?^_`{|}~-]+(?:\.[A-z0-9!#$%&amp;'*+/=?^_`{|}~-]+)*@(?:[A-z0-9](?:[A-z0-9-]*[A-z0-9])?\.)+[A-z0-9](?:[A-z0-9-]*[A-z0-9])?)
# $" data-val-required="Полето за имейла ви е задължително." id="email_txt" name="Email" placeholder="Имейл" type="text" value="">

element = driver.find_element("name", "Email")
element.click()
tm.sleep(n)

# for i in range(10000000, 90000000, 100):
#     element.send_keys(i + Кeys.ENTER)  # TODO
#
#     tm.sleep(n)
#
#     element = driver.find_element("id", "search_q")
#     element.click()
#     tm.sleep(n)
