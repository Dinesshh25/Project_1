import json

def add_income(transactions):
    print("\n=== Tambah Pemasukan ===")

    # input deskripsi pemasukan
    description = input("Sumber pemasukan: ")

    # input jumlah pemasukan
    try:
        amount = float(input("Jumlah pemasukan: "))
    except ValueError:
        print("Jumlah harus berupa angka!")
        return

    # validasi angka tidak boleh negatif / nol
    if amount <= 0:
        print("Jumlah harus lebih dari 0")
        return

    # membuat data transaksi baru (dictionary)
    transaction = {
        "type": "income",
        "amount": amount,
        "description": description
    }

    # menambahkan ke list transactions dari main.py
    transactions.append(transaction)

    print("Pemasukan berhasil ditambahkan!")

def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)