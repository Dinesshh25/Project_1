def add_expense(transactions):
    print("\n=== Tambah Pengeluaran ===")
    
    # --- VALIDASI APAKAH TRANSACTIONS ITU LIST ---
    if not isinstance(transactions, list):
        print("Error: Database tidak berbentuk list. Periksa main.py!")
        return

    description = input("Deskripsi pengeluaran: ")

    try:
        amount = float(input("Jumlah pengeluaran: "))
    except ValueError:
        print("Jumlah harus berupa angka!")
        return

    if amount <= 0:
        print("Jumlah harus lebih dari 0")
        return

    transaction = {
        "type": "expense",
        "amount": amount,
        "description": description
    }

    # Sekarang aman karena sudah dipastikan transactions adalah list
    transactions.append(transaction)
    print("Berhasil menambah pengeluaran!")