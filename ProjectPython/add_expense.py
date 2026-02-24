
def add_expense(transactions):
	print("\n=== Tambah Pengeluaran ===")

	# input deskripsi pengeluaran
	description = input("Deskripsi pengeluaran: ")

	# input jumlah pengeluaran
	try:
		amount = float(input("Jumlah pengeluaran: "))
	except ValueError:
		print("Jumlah harus berupa angka!")
		return

	# validasi angka tidak boleh negatif / nol
	if amount <= 0:
		print("Jumlah harus lebih dari 0")
		return

	# membuat data transaksi baru (dictionary)
	transaction = {
		"type": "expense",
		"amount": amount,
		"description": description
	}

	# menambahkan ke list transactions dari main.py
	transactions.append(transaction)

	print("Pengeluaran berhasil ditambahkan!")

