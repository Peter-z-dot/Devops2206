from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver1 = webdriver.Chrome()
driver1.get("c:/users/a9438/downloads/tip_calc/tip_calc/index.html")
billamt = driver1.find_element('id', 'billamt')
billamt.send_keys('100')
driver1.find_element('xpath', '//*[@id="serviceQual"]/option[3]').click()
driver1.find_element('xpath', '//*[@id="soundQual"]/option[3]').click()
driver1.find_element('id', 'peopleamt').send_keys('4')
driver1.find_element('id', 'calculate').click()
actual = driver1.find_element('id', 'tip').text
expected = '6.00'
print(actual)
assert expected == actual
sleep(10)
