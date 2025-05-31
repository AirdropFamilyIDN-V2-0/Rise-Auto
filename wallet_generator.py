import json
import csv
from eth_account import Account
from datetime import datetime

def generate_wallets_batch(count):
    print(f"🔐 Generating {count} Ethereum wallets...")

    wallets = []

    for i in range(count):
        account = Account.create()

        wallet = {
            'index': i + 1,
            'address': account.address,
            'private_key': account.key.hex(),
            'public_key': account._key_obj.public_key.to_hex()
        }

        wallets.append(wallet)

        if (i + 1) % 100 == 0:
            print(f"Generated {i + 1}/{count} wallets...")

    print(f"✅ Successfully generated {count} wallets!")
    return wallets

def auto_save_files(wallets):
    with open("pkevm.txt", 'w', encoding='utf-8') as txtfile:
        for wallet in wallets:
            txtfile.write(f"{wallet['private_key']}\n")

    print("✅ Private keys saved to: pkevm.txt")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_filename = f"wallets_batch_complete_{timestamp}.json"

    complete_data = {
        'metadata': {
            'generated_at': datetime.now().isoformat(),
            'total_wallets': len(wallets),
            'generator_type': 'batch_random',
            'description': 'Batch generated random Ethereum wallets'
        },
        'files': {
            'private_keys_file': 'pkevm.txt',
            'complete_data_file': json_filename
        },
        'wallets': wallets
    }

    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(complete_data, jsonfile, indent=2, ensure_ascii=False)

    print(f"✅ Complete data saved to: {json_filename}")

    return {
        'private_keys_file': 'pkevm.txt',
        'complete_file': json_filename
    }

def print_sample_wallets(wallets, count=5):
    print(f"\n📋 Sample wallets (showing first {count}):")
    print("-" * 80)

    for wallet in wallets[:count]:
        print(f"Wallet #{wallet['index']}:")
        print(f"  Address:     {wallet['address']}")
        print(f"  Private Key: {wallet['private_key']}")
        print()

if __name__ == "__main__":
    try:
        wallet_count = int(input("Enter number of wallets to generate (default: 100): ") or "100")

        if wallet_count > 10000:
            confirm = input(f"⚠️  You're about to generate {wallet_count} wallets. Continue? (y/n): ")
            if confirm.lower() != 'y':
                print("❌ Operation cancelled")
                exit()

        wallets = generate_wallets_batch(wallet_count)

        print("\n💾 Auto-saving files...")
        saved_files = auto_save_files(wallets)

        print_sample_wallets(wallets, 3)

        print(f"\n🎉 COMPLETE!")
        print(f"📁 Files created:")
        print(f"  🔑 Private keys: {saved_files['private_keys_file']}")
        print(f"  📋 Complete data: {saved_files['complete_file']}")
        print(f"🔢 Total wallets generated: {len(wallets)}")

    except ValueError:
        print("❌ Invalid number input!")
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
