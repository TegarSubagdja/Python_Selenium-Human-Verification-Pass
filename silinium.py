from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)
print("Berhasil connect ke Chrome")
driver.get("https://10fastfingers.com/typing-test/indonesian")
print("Facebook berhasil dibuka")
time.sleep(5)
print("Title:", driver.title)
try:
    button = driver.find_element(By.CLASS_NAME, "sc-29177491-0")
    button.click()
    time.sleep(2)
    print("Tombol ditemukan")
except:
    print("Tombol tidak ditemukan")
input("Tekan ENTER untuk selesai...")