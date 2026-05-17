# Selenium Attach Existing Chrome Session

Dokumentasi setup Selenium agar dapat:
- attach ke browser Chrome yang sudah terbuka
- mengurangi captcha / deteksi automation
- menggunakan session login asli
- menggunakan profile khusus automation

---

# Install

Install dependency Python:

```bash
pip install selenium
```

Optional (lebih stealth):

```bash
pip install undetected-chromedriver
```

---

# Kenapa Tidak Menggunakan Browser Selenium Default?

Jika langsung menggunakan:

```python
driver = webdriver.Chrome()
```

website sering mendeteksi automation karena:
- navigator.webdriver
- profile kosong
- tidak ada cookies/history
- fingerprint automation

Akibatnya:
- captcha sering muncul
- login dianggap mencurigakan
- automation lebih mudah diblokir

---

# Solusi

Menggunakan:
- Chrome asli
- remote debugging
- attach Selenium ke browser yang sudah berjalan

Dengan metode ini:
- browser lebih natural
- cookies tersimpan
- login tetap aktif
- captcha lebih sedikit

---

# Menjalankan Chrome Debugging

Tutup semua Chrome terlebih dahulu.

Jalankan CMD:

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium_profile"
```

Penjelasan:

| Parameter | Fungsi |
|---|---|
| --remote-debugging-port=9222 | Membuka API kontrol Chrome |
| --user-data-dir | Membuat profile Chrome khusus automation |

---

# Penjelasan Port 9222

Port:

```text
9222
```

digunakan Chrome untuk:
- remote debugging
- automation
- komunikasi Selenium ↔ Chrome

Secara konsep:

```text
Python/Selenium
       ↓
localhost:9222
       ↓
Chrome
```

---

# Cara Mengecek Port Masih Aktif atau Tidak

CMD:

```bash
netstat -ano | findstr :9222
```

Jika muncul:

```text
LISTENING
```

berarti port debugging masih aktif.

Contoh:

```text
TCP    127.0.0.1:9222    0.0.0.0:0    LISTENING    12345
```

Keterangan:
- 9222 = port debugging
- 12345 = PID process Chrome

---

# Penjelasan Status Socket

## LISTENING

Port masih aktif dan menerima koneksi.

## TIME_WAIT

Koneksi sudah ditutup tetapi Windows masih cleanup socket.

## CLOSE_WAIT

Koneksi sedang menunggu penutupan sempurna.

## FIN_WAIT_2

Tahap akhir penutupan koneksi TCP.

Status selain LISTENING biasanya aman dan akan hilang sendiri.

---

# Cara Menutup Port Debugging

## Cara normal

Tutup semua Chrome.

Atau di terminal tekan:

```text
CTRL + C
```

---

# Force Stop Chrome dan Selenium

CMD:

```bash
taskkill /F /IM chromedriver.exe
taskkill /F /IM chrome.exe
```

Keterangan:

| Command | Fungsi |
|---|---|
| taskkill /F | force close process |
| /IM | berdasarkan nama executable |

---

# Cara Mengetahui Chrome Masih Berjalan

CMD:

```bash
tasklist | findstr chrome
```

Jika masih muncul:
- chrome.exe
- chromedriver.exe

berarti process masih aktif.

---

# Cara Kill Berdasarkan PID

Cek PID:

```bash
netstat -ano | findstr :9222
```

Contoh hasil:

```text
TCP    127.0.0.1:9222    0.0.0.0:0    LISTENING    8064
```

Kill process:

```bash
taskkill /PID 8064 /F
```

---

# Jika Chrome Tidak Bisa Dibuka Setelah Debugging

Biasanya karena:
- chrome.exe masih berjalan
- profile terkunci
- chromedriver belum mati
- lock file tertinggal

---

# Cara Mengatasi Chrome Lock

Masuk ke folder:

```text
C:\selenium_profile
```

Hapus file berikut jika ada:

```text
SingletonLock
SingletonSocket
SingletonCookie
```

File tersebut digunakan Chrome untuk mencegah profile dipakai banyak process sekaligus.

---

# Jika Masih Bermasalah

Gunakan profile baru:

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium_profile2"
```

Chrome akan membuat profile baru otomatis.

---

# Connect Selenium ke Chrome Existing

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# connect ke chrome existing
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)

driver.get("https://www.facebook.com")

print(driver.title)

input("ENTER untuk selesai...")

driver.quit()
```

---

# Kenapa Menggunakan Profile Khusus?

Profile disimpan di:

```text
C:\selenium_profile
```

Tujuannya:
- menghindari corrupt profile utama
- memisahkan automation dan browser pribadi
- menyimpan cookies/login automation

---

# Best Practice

- gunakan profile khusus automation
- jangan gunakan profile utama pribadi
- gunakan attach existing browser
- selalu gunakan driver.quit()
- hindari headless jika ingin lebih natural
- jangan spam request terlalu cepat
- gunakan delay random
- login manual jika website sensitif

---

# Perbedaan close() vs quit()

```python
driver.close()
```

Hanya menutup tab aktif.

```python
driver.quit()
```

Menutup:
- browser
- chromedriver
- seluruh session Selenium

Disarankan selalu menggunakan:

```python
driver.quit()
```

---

# Kesimpulan

Metode attach existing Chrome session lebih stabil dibanding membuka browser Selenium baru karena:
- menggunakan browser asli
- fingerprint lebih natural
- cookies/history tersedia
- login tersimpan
- captcha lebih sedikit
- lebih cocok untuk automation modern