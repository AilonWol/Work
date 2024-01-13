from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

o = Options()
o.add_experimental_option("detach", True)

# Инициализация драйвера Chrome
driver=webdriver.Chrome(options=o)

# Переходим на веб-сайт
driver.get("https://guru.qahacking.ru/")
driver.set_window_size(1500,900)

driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[3]/a").click()
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[3]/a").click()
driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div[3]/div/div[1]/div[1]/div/div/div[3]/div[7]/a[1]").click()
driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/form/div[2]/div/div[2]/a").click()

driver.find_element(By.ID,"f_name").send_keys("Zubenko")
driver.find_element(By.ID,"l_name").send_keys("Mikhail")
driver.find_element(By.ID,"email").send_keys("Zb_mik@gmail.com")
driver.find_element(By.ID,"street").send_keys("Shumilovsky_town")
driver.find_element(By.NAME,"zip").send_keys("100001")
driver.find_element(By.NAME,"city").send_keys("Tashkent")
driver.find_element(By.NAME,"state").send_keys("Tashkent region")
# Селектор
country_dropdown = driver.find_element(By.ID, "country")
select = Select(country_dropdown)
select.select_by_value("226")

driver.find_element(By.ID,"phone").send_keys("+7(843)2310505")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div/form/div[4]/div/input").click()
#Способ оплаты
driver.find_element(By.ID, "payment_method_2").click()
driver.find_element(By.ID, "payment_submit").click()
#Способ доставки
driver.find_element(By.ID, "shipping_method_2")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div/form/input").click()
#Запуск "ПРАВИЛА"
driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div[2]/form/div/div[3]/a[1]").click()
time.sleep(2)
#Запуск "ПРАВО ВОЗВРАТА"
driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div[2]/form/div/div[3]/a[2]").click()
time.sleep(2)

window_handles = driver.window_handles
main_window_handle = driver.current_window_handle
second_window_handle = [handle for handle in window_handles if handle != main_window_handle][0]
driver.switch_to.window(second_window_handle)
driver.switch_to.window(main_window_handle)

#Подтверждение заказа
driver.find_element(By.ID, "agb").click()
driver.find_element(By.NAME, "finish_registration").click()
time.sleep(2)
#Допы:
driver.save_screenshot("mk_ord_1auto-test_(sbs).png")
print("\033[1;30;42m ----Успешно---- \033[0m")

driver.quit()

