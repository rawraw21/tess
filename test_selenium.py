from selenium import webdriver

# Tentukan lokasi ChromeDriver
driver = webdriver.Chrome()

# Buka Google
driver.get("https://www.google.com")

# Cetak judul halaman
print("Judul halaman:", driver.title)

# Tutup browser setelah 5 detik
import time
time.sleep(5)
driver.quit()
