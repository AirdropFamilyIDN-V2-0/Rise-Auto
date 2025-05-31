import json
import time
import random
from web3 import Web3
from eth_account import Account
import requests
from rich.console import Console
from rich.panel import Panel
from termcolor import cprint


RPC_URL = "https://testnet.riselabs.xyz/"
CHAIN_ID = 11155931

WETH = Web3.to_checksum_address("0x4200000000000000000000000000000000000006")
USDC = Web3.to_checksum_address("0x8A93d247134d91e0de6f96547cB0204e5BE8e5D8")
RISE = Web3.to_checksum_address("0xd6e1afe5cA8D00A2EFC01B89997abE2De47fdfAf")
DODO_APPROVE_TO = Web3.to_checksum_address("0x5eC9BEaCe4a0f46F77945D54511e2b454cb8F38E")
SPENDER = Web3.to_checksum_address("0x6a9B38F1E20B7e048CE21b06f6e5eFe9d8f4e3e2")
ROUTER_ADDRESS = DODO_APPROVE_TO
RISE_TOKEN = Web3.to_checksum_address("0x6a9B38F1E20B7e048CE21b06f6e5eFe9d8f4e3e2")
USDC_TOKEN = Web3.to_checksum_address("0x3d53b844C62Ab07b16aa1584854acD16d2cD6a29")



tokens = [
    {"symbol": "WETH", "address": WETH},
    {"symbol": "USDC", "address": USDC},
    {"symbol": "RISE", "address": RISE}
]

WETH_ABI = [
    {"inputs": [], "name": "deposit", "outputs": [], "stateMutability": "payable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "", "type": "address"}],
     "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
     "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "spender", "type": "address"},
                 {"internalType": "uint256", "name": "amount", "type": "uint256"}],
     "name": "approve", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
     "stateMutability": "nonpayable", "type": "function"}
]

NFT_ABI = [
    {
        "inputs": [{"internalType": "string", "name": "name", "type": "string"},
                   {"internalType": "string", "name": "symbol", "type": "string"}],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {"inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}],
     "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}],
     "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "tokenId", "type": "uint256"}],
     "name": "mint", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
]

ERC20_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "_spender", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "approve",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function",
        "stateMutability": "nonpayable"
    }
]
ROUTER_ABI = [
    {
        "inputs": [
            {"internalType": "address","name": "tokenA","type": "address"},
            {"internalType": "address","name": "tokenB","type": "address"},
            {"internalType": "uint256","name": "amountADesired","type": "uint256"},
            {"internalType": "uint256","name": "amountBDesired","type": "uint256"},
            {"internalType": "uint256","name": "amountAMin","type": "uint256"},
            {"internalType": "uint256","name": "amountBMin","type": "uint256"},
            {"internalType": "address","name": "to","type": "address"},
            {"internalType": "uint256","name": "deadline","type": "uint256"}
        ],
        "name": "addLiquidity",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]


NFT_BYTECODE = "0x608060405234801561001057600080fd5b5060405161010c38038061010c83398101604081905261002f91610045565b600080546001600160a01b0319163317905561011f806100526000396000f3fe60806040526004361061001e5760003560e01c806318160ddd14610023578063d0def52114610048575b600080fd5b61002b610066565b60405161003891906100e9565b60405180910390f35b6100506100a4565b60405161005d91906100e9565b60405180910390f35b6000546001600160a01b0316331461007e57600080fd5b60015460405163a0712d6811600481906000908152602080840151908201529181015160609093015190928492509091908301828280156100d65780601f106100ab576101008083540402835291602001916100d6565b820191906000526020600020905b8154815290600101906020018083116100b957829003601f168201915b5050505050905090565b600080546001600160a01b03191690556000546001600160a01b031633146100fa57600080fd5b6001805460ff19169055565b600080fd5b6000819050919050565b61011c81610109565b811461012757600080fd5b5056fea2646970667358221220de798708fc9c0532db76d88a2fbd315c8c7ac775ce77c3a64e128a2d1be20f8164736f6c63430008130033"

console = Console()

def tampil_banner():
    banner = """[bold cyan]
████████╗███████╗███████╗████████╗███╗   ██╗███████╗████████╗
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝████╗  ██║██╔════╝╚══██╔══╝
   ██║   █████╗  ███████╗   ██║   ██╔██╗ ██║█████╗     ██║
   ██║   ██╔══╝  ╚════██║   ██║   ██║╚██╗██║██╔══╝     ██║
   ██║   ███████╗███████║   ██║   ██║ ╚████║███████╗   ██║
   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝
[/bold cyan]"""
    console.print(Panel.fit(banner, title="[bold yellow]Testnet Tools - RISE TESTNET[/bold yellow]", subtitle="BY ADFMIDN TEAM"))
def load_wallets():
    with open("pkevm.txt") as f:
        return [line.strip() for line in f if line.strip()]

def approve_pol(w3, wallet_pk, token_address, spender, amount):
    account = Account.from_key(wallet_pk)
    wallet_address = account.address
    token = w3.eth.contract(address=Web3.to_checksum_address(token_address), abi=ERC20_ABI)

    try:
        symbol = token.functions.symbol().call()
    except:
        symbol = "RISE & USDT"

    print(f"[APPROVE {symbol}] Wallet: {wallet_address} ke {spender}")

    try:
        tx = token.functions.approve(
            Web3.to_checksum_address(spender),
            amount
        ).build_transaction({
            'from': wallet_address,
            'nonce': w3.eth.get_transaction_count(wallet_address),
            'gas': 100000,
            'gasPrice': w3.eth.gas_price,
            'chainId': CHAIN_ID
        })

        signed_tx = w3.eth.account.sign_transaction(tx, wallet_pk)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"✅ Approve {symbol} sukses! Tx: https://explorer.testnet.riselabs.xyz/tx/{w3.to_hex(tx_hash)}")
    except Exception as e:
        print(f"❌ Gagal approve {symbol}: {e}")

def auto_add_liquidity(w3, wallet_pk, token_a, token_b, amount_a, amount_b, router_address, abi):
    account = Account.from_key(wallet_pk)
    wallet_address = account.address
    contract = w3.eth.contract(address=Web3.to_checksum_address(router_address), abi=abi)

    print(f"[ADD LIQUIDITY] Wallet: {wallet_address}")
    try:
        tx = contract.functions.addLiquidity(
            Web3.to_checksum_address(token_a),
            Web3.to_checksum_address(token_b),
            amount_a,
            amount_b,
            0,
            0,
            wallet_address,
            int(time.time()) + 1000
        ).build_transaction({
            'from': wallet_address,
            'nonce': w3.eth.get_transaction_count(wallet_address),
            'gas': 300000,
            'gasPrice': w3.eth.gas_price,
            'chainId': CHAIN_ID
        })

        signed_tx = w3.eth.account.sign_transaction(tx, wallet_pk)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"✅ Add liquidity sukses! Tx: https://explorer.testnet.riselabs.xyz/tx/{w3.to_hex(tx_hash)}")
    except Exception as e:
        print(f"❌ Gagal add liquidity: {e}")



def process_wallet(wallet_pk):
    from web3.middleware import geth_poa_middleware

    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    acct = Account.from_key(wallet_pk)
    address = acct.address

    print("\n--------------------------------------------------")
    print(f"🔁 Memproses wallet: {address}")
    print("--------------------------------------------------")

    try:
        eth_balance = w3.eth.get_balance(address)
        print(f"💰 Saldo ETH: {w3.from_wei(eth_balance, 'ether')} ETH")

        token_balances = get_all_token_balances(w3, address)
        for sym, val in token_balances.items():
            print(f"   - {sym}: {val}")

        random_delay("\n⏳ Wrapping")
        wrap_eth_to_weth(w3, wallet_pk, Web3.to_wei(0.00001, 'ether'))

        random_delay("\n⏳(WETH Ke USDC)")
        auto_swap(w3, wallet_pk, Web3.to_wei(0.00001, 'ether'))

        random_delay("\n⏳ (RISE ke USDC)")
        swap_rise_to_usdc(w3, wallet_pk, Web3.to_wei(0.0001, 'ether'))

        random_delay("\n⏳ Approve RISE")
        approve_pol(w3, wallet_pk, RISE_TOKEN, SPENDER, Web3.to_wei(1, 'ether'))

        random_delay("\n⏳ Approve USDC")
        approve_pol(w3, wallet_pk, USDC_TOKEN, SPENDER, Web3.to_wei(1, 'ether'))

        random_delay("\n⏳ add liquidity")
        auto_add_liquidity(
            w3=w3,
            wallet_pk=wallet_pk,
            token_a=RISE_TOKEN,
            token_b=USDC_TOKEN,
            amount_a=w3.to_wei(1, 'ether'),
            amount_b=w3.to_wei(1, 'ether'),
            router_address=ROUTER_ADDRESS,
            abi=ROUTER_ABI
        )

        random_delay("\n⏳ deploy NFT")
        deploy_nft(w3, wallet_pk)

        cprint(f"\n✅ Selesai untuk wallet {address}\n", "green")
        print("--------------------------------------------------")

    except Exception as e:
        cprint(f"⚠️ Error saat memproses wallet: {e}", "red")
        print("--------------------------------------------------")



def random_delay(reason=None):
    delay = round(random.uniform(2, 6), 2)
    if reason:
        cprint(f"{reason}: Dilay {delay} detik...", "blue")
    time.sleep(delay)

def get_all_token_balances(w3, address):
    balances = {}
    for token in tokens:
        try:
            contract = w3.eth.contract(address=token["address"], abi=WETH_ABI)
            raw = contract.functions.balanceOf(address).call()
            balances[token["symbol"]] = Web3.from_wei(raw, 'ether')
        except Exception as e:
            balances[token["symbol"]] = f"error: {e}"
    return balances

def wrap_eth_to_weth(w3, wallet_pk, amount):
    acct = Account.from_key(wallet_pk)
    address = acct.address
    print(f"[WRAP ETH → WETH] Wallet: {address}")
    weth = w3.eth.contract(address=WETH, abi=WETH_ABI)
    tx = weth.functions.deposit().build_transaction({
        'from': address, 'value': amount,
        'nonce': w3.eth.get_transaction_count(address),
        'gas': 100000, 'gasPrice': w3.eth.gas_price,
        'chainId': CHAIN_ID
    })
    signed = w3.eth.account.sign_transaction(tx, wallet_pk)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    print(f"✅ Wrap sukses! Tx: https://explorer.testnet.riselabs.xyz/tx/{w3.to_hex(tx_hash)}")

def approve_token(w3, wallet_pk, token_address, amount):
    acct = Account.from_key(wallet_pk)
    address = acct.address
    token = w3.eth.contract(address=token_address, abi=WETH_ABI)
    tx = token.functions.approve(DODO_APPROVE_TO, amount).build_transaction({
        'from': address,
        'nonce': w3.eth.get_transaction_count(address),
        'gas': 100000,
        'gasPrice': w3.eth.gas_price,
        'chainId': CHAIN_ID
    })
    signed = w3.eth.account.sign_transaction(tx, wallet_pk)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    print(f"✅ Approve sukses! Tx: https://explorer.testnet.riselabs.xyz/tx/{w3.to_hex(tx_hash)}")

def auto_swap(w3, wallet_pk, amount):
    acct = Account.from_key(wallet_pk)
    address = acct.address
    print(f"[SWAP WETH → USDC] Wallet: {address}")
    approve_token(w3, wallet_pk, WETH, Web3.to_wei(10, 'ether'))

    params = {
        "fromTokenAddress": WETH,
        "toTokenAddress": USDC,
        "fromAmount": str(amount),
        "userAddr": address,
        "chainId": CHAIN_ID
    }
    r = requests.get("https://api.dodoex.io/api/v1/route/quote", params=params)
    swap_data = r.json() if r.status_code == 200 else None
    if not swap_data or "data" not in swap_data or "tx" not in swap_data["data"]:
        return
    tx_data = swap_data["data"]["tx"]
    tx = {
        "to": tx_data["to"],
        "value": int(tx_data["value"]),
        "gas": int(tx_data["gas"]),
        "gasPrice": int(tx_data["gasPrice"]),
        "nonce": w3.eth.get_transaction_count(address),
        "data": tx_data["data"],
        "chainId": CHAIN_ID
    }
    signed = w3.eth.account.sign_transaction(tx, wallet_pk)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    print(f"✅ Swap sukses! Tx: https://explorer.testnet.riselabs.xyz/tx/{w3.to_hex(tx_hash)}")

def swap_rise_to_usdc(w3, wallet_pk, amount):
    acct = Account.from_key(wallet_pk)
    address = acct.address
    print(f"[SWAP RISE → USDC] Wallet: {address}")
    approve_token(w3, wallet_pk, RISE, Web3.to_wei(10, 'ether'))

    params = {
        "fromTokenAddress": RISE,
        "toTokenAddress": USDC,
        "fromAmount": str(amount),
        "userAddr": address,
        "chainId": CHAIN_ID
    }
    r = requests.get("https://api.dodoex.io/api/v1/route/quote", params=params)
    swap_data = r.json() if r.status_code == 200 else None
    if not swap_data or "data" not in swap_data or "tx" not in swap_data["data"]:
        return
    tx_data = swap_data["data"]["tx"]
    tx = {
        "to": tx_data["to"],
        "value": int(tx_data["value"]),
        "gas": int(tx_data["gas"]),
        "gasPrice": int(tx_data["gasPrice"]),
        "nonce": w3.eth.get_transaction_count(address),
        "data": tx_data["data"],
        "chainId": CHAIN_ID
    }
    signed = w3.eth.account.sign_transaction(tx, wallet_pk)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    print(f"✅ Swap sukses! Tx: https://explorer.testnet.riselabs.xyz/tx/{w3.to_hex(tx_hash)}")


def deploy_nft(w3, wallet_pk, abi=NFT_ABI, bytecode=NFT_BYTECODE):
    account = Account.from_key(wallet_pk)
    address = account.address

    suffix = str(random.randint(1000, 9999))
    name = f"CoolNFT{suffix}"
    symbol = f"CNFT{suffix}"

    print(f"🚀 Deploying NFT untuk wallet {address}...")

    try:
        contract = w3.eth.contract(abi=abi, bytecode=bytecode)
        build_txn = contract.constructor(name, symbol).build_transaction({
            'from': address,
            'nonce': w3.eth.get_transaction_count(address),
            'gas': 2000000,
            'gasPrice': w3.eth.gas_price,
            'chainId': CHAIN_ID
        })
        signed = w3.eth.account.sign_transaction(build_txn, wallet_pk)
        tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
        print(f"⏳ Menunggu konfirmasi deploy...")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        contract_address = receipt.contractAddress
        print(f"✅ Kontrak NFT berhasil dideploy di {contract_address}")
        print(f"🔗 Explorer: https://explorer.testnet.riselabs.xyz/address/{contract_address}")
    except Exception as e:
        print(f"❌ Gagal deploy NFT: {e}")
        return

    try:
        print("🖼️ Minting NFT ke wallet sendiri...")
        contract_instance = w3.eth.contract(address=contract_address, abi=abi)
        mint_tx = contract_instance.functions.mint(address, 1).build_transaction({
            'from': address,
            'nonce': w3.eth.get_transaction_count(address, 'pending'),
            'gas': 150000,
            'gasPrice': w3.eth.gas_price,
            'chainId': CHAIN_ID
        })
        signed = w3.eth.account.sign_transaction(mint_tx, wallet_pk)
        tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
        print(f"✅ Mint sukses! Tx: https://explorer.testnet.riselabs.xyz/tx/{w3.to_hex(tx_hash)}")
    except Exception as e:
        print(f"❌ Gagal mint NFT: {e}")


def main():
    tampil_banner()
    wallets = load_wallets()

    if not wallets:
        print("❌ Wallet tidak ditemukan di pkevm.txt")
        return

    while True:
        print("🚀 Mulai proses semua wallet")
        for wallet_pk in wallets:
            try:
                process_wallet(wallet_pk)
            except Exception as e:
                print(f"⚠️ Error saat memproses wallet: {e}")

        print("⏸️ Semua wallet telah diproses Dilay 24 Abad Sampai Tea Listing ")
        time.sleep(86400)

if __name__ == "__main__":
    main()
