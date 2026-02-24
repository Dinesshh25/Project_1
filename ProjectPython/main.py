import json
import os
from add_income import add_income
from add_expense import add_expense
from show_transaction import show_transaction
from delete_transaction import delete_transaction
from calculate_total import calculate_total_expense

# Mendapatkan lokasi folder tempat file ini berada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'data.json')

# Pastikan load_data mengembalikan list [] bukan dict {}
def load_data():
    if not os.path.exists(FILE_PATH):
        return [] 
    with open(FILE_PATH, 'r') as file:
        try:
            data = json.load(file)
            # Jika data ternyata bukan list, paksa jadi list
            return data if isinstance(data, list) else []
        except:
            return []

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    transactions = load_data()

    while True:
        print("\n=== APLIKASI KEUANGAN KELOMPOK ===")
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Tampilkan Transaksi")
        print("4. Hapus Transaksi")
        print("5. Total Pengeluaran")
        print("6. Keluar")

        choice = input("Pilih menu (1-6): ")

        if choice == "1":
            add_income(transactions)
            save_data(transactions)
        elif choice == "2":
            add_expense(transactions)
            save_data(transactions)
        elif choice == "3":
            show_transaction(transactions)
        elif choice == "4":
            delete_transaction(transactions)
            save_data(transactions)
        elif choice == "5":
            total = calculate_total_expense(transactions)
            print(f"\nTotal Seluruh Pengeluaran: Rp{total}")
        elif choice == "6":
            print("Program dihentikan. Data tersimpan!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()