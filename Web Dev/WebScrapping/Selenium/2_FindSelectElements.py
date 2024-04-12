from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path="C:\Development\chromedriver.exe"

driver=webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.in/Arduino-UNO-board-DIP-ATmega328P/dp/B008GRTSV6/ref=sr_1_3?keywords=arduino+uno&qid=1684855453&sprefix=arduin%2Caps%2C345&sr=8-3")
driver.find_element(By.CLASS_NAME, "a-price-whole")






#driver.close()


# driver.quit()

