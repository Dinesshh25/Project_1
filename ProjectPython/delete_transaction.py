def delete_transaction(transactions):
    try:
        index = int(input("Masukkan nomor transaksi yang ingin dihapus: ")) - 1
        if 0 <= index < len(transactions):
            removed = transactions.pop(index)
            print(f"Transaksi '{removed['description']}' berhasil dihapus.")
        else:
            print("Nomor transaksi tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")