

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
