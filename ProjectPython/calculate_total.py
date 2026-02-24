
def calculate_total_expense(transactions):
	"""Hitung total pengeluaran dari list transaksi.

	transactions: list of dict dengan keys 'type' dan 'amount'
	returns: float total pengeluaran
	"""
	total = 0.0
	for t in transactions:
		if t.get("type") == "expense":
			try:
				total += float(t.get("amount", 0))
			except (TypeError, ValueError):
				continue
	return total

