from add_income import add_income , save_transactions
from delete_transaction import delete_transaction 

transactions = [
    {"type": "income", "amount": 5000, "description": "Gaji"},
    {"type": "expense", "amount": 1500, "description": "Belanja bulanan"},  
    {"type": "expense", "amount": 200, "description": "Makan di luar"},
    {"type": "income", "amount": 2000, "description": "Freelance"},
    {"type": "expense", "amount": 300, "description": "Transportasi"},
]

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Tampilkan Transaksi")
        print("4. Hapus Transaksi")
        print("5. Total Pengeluaran")
        print("6. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            add_income(transactions)
            save_transactions(transactions)
            print(transactions) 
        elif choice == "2":
            add_expense(transactions)
        elif choice == "3":
            show_transactions(transactions)
        elif choice == "4":
            delete_transaction(transactions)
        elif choice == "5":
            total = calculate_total_expense(transactions)
            print("Total Pengeluaran:", total)
        elif choice == "6":
            break
        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
