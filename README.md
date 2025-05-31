# 🚀 Rise Auto -  Rise Testnet
![image](https://github.com/user-attachments/assets/350f732f-3140-4f54-95c2-a0a6ef4ce124)

| **Deskripsi** | **Fitur Utama** | **Persyaratan Sistem** |
|---------------|-----------------|-----------------------|
| **Rise Auto** adalah alat otomatisasi untuk menjalankan transaksi di jaringan **Rise Testnet**. Dengan tool ini, kamu bisa: <br>- 🔄 Mengubah ETH menjadi WETH (wrap ETH) <br>- 🔁 Menukar (swap) token seperti WETH, USDC, dan RISE <br>- ✅ Memberikan izin (approve) token ke kontrak pintar <br>- 💧 Menambah likuiditas (add liquidity) ke pool DEX menggunakan router DODO <br>- 🎨 Melakukan deploy NFT di jaringan testnet <br>- 🤖 Menjalankan proses ini untuk banyak wallet sekaligus dari daftar private key | - Berbasis `Web3.py` untuk interaksi dengan blockchain Ethereum compatible (Rise Testnet) <br>- Pengelolaan transaksi termasuk nonce dan gas secara otomatis <br>- Output terminal berwarna dan interaktif menggunakan `rich` dan `termcolor` <br>- Delay acak untuk menghindari aktivitas bot yang terlalu kaku | - **Python versi 3.10** (direkomendasikan untuk kompatibilitas terbaik) <br>- **Web3.py versi 6.2.0** (untuk memastikan fitur terbaru dan stabilitas) <br>- Koneksi internet stabil untuk akses RPC Rise Testnet |

---

## 🚀 Instalasi dan Cara Menjalankan

| Langkah | Perintah / Penjelasan |
|---------|----------------------|
| **1. Clone repository** | ```git clone https://github.com/AirdropFamilyIDN-V2-0/Rise-Auto.git``` Mengunduh kode ke folder``` cd Rise-Auto``` |
| **2. Install Python 3.10** | Jika belum punya, download dan install dari:<br>[https://www.python.org/downloads/release/python-3100/](https://www.python.org/downloads/release/python-3100/) |
| **3. Cek versi Python** | Pastikan versi Python minimal 3.10 dengan:<br>```bashpython3 --version```<br>Output contoh: `Python 3.10.x` |
| **4. Buat Virtual Environment (Opsional)** | Untuk isolasi paket, buat dan aktifkan venv:<br>Linux/macOS:<br>```bashpython3 -m venv venv<br>source venv/bin/activate```<br>Windows:<br>```bashpython3 -m venv venv venv\Scripts\activate``` |
| **5. Install dependencies** | Install paket yang diperlukan:<br>```pip install web3==6.2.0 eth-account requests rich termcolor``` |
| **6. Siapkan file private key** | Buat file `pkevm.txt` di folder project. Isi dengan private key wallet, satu per baris:```0x123abc456def7890abcdef1234567890abcdef1234567890abcdef1234567890<br>0xabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcd```<br>**Jangan bagikan file ini ke siapapun!** |
| **7. Jalankan skrip utama** | Jalankan otomatisasi dengan:<br>```bashpython3 main.py``` |
| **8. Pantau output** | Terminal akan menampilkan proses dan status transaksi secara real-time dengan warna dan info lengkap. |

---
## Instalasi & Cara Menjalankan di Windows (RDP User)

| Langkah                     | Perintah / Penjelasan                                                                                           |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| 1. Buka Command Prompt      | Tekan `Win + R`, ketik `cmd`, lalu tekan Enter                                                                 |
| 2. Clone repository         | `git clone https://github.com/AirdropFamilyIDN-V2-0/Rise-Auto.git`  Mengunduh kode ke folder `Rise-Auto`    |
| 3. Masuk ke folder project  | `cd Rise-Auto`                                                                                                  |
| 4. (Opsional) Buat virtual environment | `python -m venv venv` <br> Aktifkan dengan `venv\Scripts\activate`                                           |
| 5. Install dependencies     | `pip install web3==6.2.0 eth-account requests rich termcolor`                                                  |
| 6. Siapkan file private key | Buat file `pkevm.txt` di folder `Rise-Auto` <br> Isi dengan private key wallet per baris, contoh: <br> `0xabcdef123...` |
| 7. Jalankan script utama    | `python main.py`                                                                                                |
| 8. Selesai / keluar venv    | Ketik `deactivate` jika pakai virtual environment                                                              |

---
## Instalasi & Cara Menjalankan di VPS Linux (Ubuntu/Debian)

| Langkah                     | Perintah / Penjelasan                                                                                           |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| 1. Login ke VPS             | Gunakan SSH: `ssh user@alamat_ip_vps`                                                                          |
| 2. Update sistem            | `sudo apt update && sudo apt upgrade -y`                                                                       |
| 3. Install Python 3.10      | ```sudo apt install software-properties-common -y<br>sudo add-apt-repository ppa:deadsnakes/ppa -y sudo apt update sudo apt install python3.10 python3.10-venv python3.10-dev -y``` |
| 4. Periksa versi Python     | `python3.10 --version`                                                                                           |
| 5. Clone repository         | `git clone https://github.com/AirdropFamilyIDN-V2-0/Rise-Auto.git` <br> Mengunduh kode ke folder `Rise-Auto`    |
| 6. Masuk ke folder project  | `cd Rise-Auto`                                                                                                  |
| 7. Buat virtual environment | `python3.10 -m venv venv` <br> Aktifkan dengan `source venv/bin/activate`                                       |
| 8. Install dependencies     | `pip install --upgrade pip`  `pip install web3==6.2.0 eth-account requests rich termcolor`                   |
| 9. Siapkan file private key | Buat file `pkevm.txt` di folder `Rise-Auto`  Isi dengan private key wallet per baris, contoh:  `0xabcdef123...` |
| 10. Jalankan script utama   | `python main.py`                                                                                                |
| 11. Selesai                 | Ketik `deactivate` untuk keluar virtual environment jika perlu                                                  |

---

### Instalasi menggunakan poetry

| Langkah | Perintah / Penjelasan |
|---------|----------------------|
| **1. Clone repository** | ```git clone https://github.com/AirdropFamilyIDN-V2-0/Rise-Auto.git``` Mengunduh kode ke folder``` cd Rise-Auto``` |
| **2. Install Python 3.10** | Jika belum punya, download dan install dari:<br>[https://www.python.org/downloads/release/python-3100/](https://www.python.org/downloads/release/python-3100/) |
| **3. Cek versi Python** | Pastikan versi Python minimal 3.10 dengan:<br>```python3 --version```<br>Output contoh: `Python 3.10.x` |
| **4. Install Poetry** | Jika belum punya, install ```pip install poetry``` atau ```curl -sSL https://install.python-poetry.org | python3 -```, setelah itu set PATH sesuai instruksi. Jika belum pernah memakai poetry maka config venv ```poetry config virtualenvs.create true``` dan ```poetry config virtualenvs.in-project true``` |
| **5. Install dependencies** | Jalankan ```poetry install``` |
| **6. Siapkan file private key** | Buat file `pkevm.txt` di folder project. Isi dengan private key wallet, satu per baris:```0x123abc456def7890abcdef1234567890abcdef1234567890abcdef1234567890<br>0xabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcd```<br>**Jangan bagikan file ini ke siapapun!** |
| **7. Jalankan skrip utama** | Jalankan otomatisasi dengan:<br>```poetry run python main.py``` |
| **8. Pantau output** | Terminal akan menampilkan proses dan status transaksi secara real-time dengan warna dan info lengkap. |


---
## ⚠️ Tips dan Catatan

| Poin Penting |
|--------------|
| - Pastikan saldo ETH wallet cukup untuk membayar biaya gas. |
| - Gunakan RPC Rise Testnet yang stabil (default sudah diatur di skrip). |
| - Jika ada error, cek kembali versi Python dan Web3.py. |
| - Gunakan virtual environment supaya paket tidak bercampur dengan sistem. |
| - Delay acak di script untuk menghindari deteksi bot. |

---

## 📁 Struktur Folder

```text
Rise-Auto/
│
├── main.py          # Skrip utama otomatisasi transaksi
├── pkevm.txt        # File daftar private key wallet (jangan dibagikan)
└──  README.md        # Dokumentasi ini
```


## 🌐 Join Komunitas

📢 Gabung ke komunitas kami untuk update terbaru, diskusi, dan support:
👉 [https://t.me/AirdropFamilyIDN](https://t.me/AirdropFamilyIDN)

Jika kamu ingin akses ke lebih banyak tools eksklusif, silakan join **membership ADFMIDN** 💎
👉 Dapatkan fitur premium dan alat otomatisasi terbaru hanya untuk member!



## 📄 Lisensi

Repositori ini bersifat open-source dan bebas digunakan.
Gunakan dengan bijak untuk eksplorasi dan pembelajaran.
