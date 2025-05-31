from web3 import Web3
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests, time


web3 = Web3(Web3.HTTPProvider("https://testnet.riselabs.xyz"))
chainId = web3.eth.chain_id


if not web3.is_connected():
    print("Gagal terhubung ke jaringan")
    exit()


def log(teks):
    with open('datariselabswallet.txt', "a") as f:
        f.write(teks + '\n')


def get_token(url, delay_seconds=7):
    try:
        driver = Driver(uc=True, headless=True)
        driver.uc_open_with_reconnect(url, reconnect_time=delay_seconds)
        time.sleep(delay_seconds)
        token_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "cf-turnstile-response"))
        )
        token = token_element.get_attribute("value")
        if not token or token == "None":
            print('Gagal ambil token CAPTCHA. Mencoba ulang...')
            return get_token(url, delay_seconds)
        print('>> Token CAPTCHA berhasil diambil')
        return token
    except Exception as e:
        print(f"Kesalahan CAPTCHA: {str(e)}")
        return None
    finally:
        try:
            driver.quit()
        except:
            pass

def req_faucet(token, alamat, proxy=None):
    try:
        url = "https://faucet-api.riselabs.xyz/faucet/multi-request"
        headers = {
            "content-type": "application/json",
            "origin": "https://faucet.testnet.riselabs.xyz",
            "referer": "https://faucet.testnet.riselabs.xyz/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        proxies = {
            "http": proxy,
            "https": proxy
        } if proxy else None

        data = {
            "address": alamat,
            "turnstileToken": token,
            "tokens": ["ETH"]
        }

        response = requests.post(url, headers=headers, json=data, proxies=proxies)
        return response.json()
    except Exception as e:
        print(f"Kesalahan faucet: {str(e)}")
        return None


with open("addressevm.txt", "r") as f:
    daftar_address = [line.strip() for line in f if line.strip()]

proxy = input('Masukkan proxy HTTP (contoh: http://user:pass@ip:port): ')
delays = int(input('Masukkan delay saat ambil token CAPTCHA (minimal 7 detik): '))


for addr in daftar_address:
    try:
        print(f'\nMemproses address: {addr}')
        print('Mengambil token CAPTCHA...')
        token = get_token("https://faucet.testnet.riselabs.xyz", delays)
        if not token:
            print("Gagal ambil CAPTCHA, lanjut ke alamat berikutnya.")
            continue

        hasil_faucet = req_faucet(token, addr, proxy)
        if not hasil_faucet:
            print("Gagal request faucet, lanjut ke alamat berikutnya.")
            continue

        txhash = hasil_faucet.get("results", [])[0].get("tx")
        if txhash:
            print(f'✅ Berhasil klaim faucet untuk: {addr}')
            print(f'   Hash transaksi: {txhash}')
            log(f'{addr}|{txhash}')
        else:
            print(f'❌ Gagal klaim faucet untuk: {addr}')
            print(hasil_faucet)
        time.sleep(5)
    except Exception as e:
        print(f"❌ Error: {e}")
