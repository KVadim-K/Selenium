from selenium import webdriver
import time
#С помощью time мы можем делать задержки в программе

#Если мы работаем с Chrome. Создаём объект браузера, через который мы будем действовать.
browser = webdriver.Chrome()

# Настраиваем возможность зайти на сайт.
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")#В кавычках указываем URL сайта, на который нам нужно зайти
browser.save_screenshot("dom.png")
time.sleep(5)
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")
time.sleep(3)
browser.refresh()
time.sleep(3)
# browser.quit() #Закрываем браузер
