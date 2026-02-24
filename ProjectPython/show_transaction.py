import calculate_total
import add_income
import add_expense

# OPSI Ke-3
def show_transaction(transactions):
    print("\n=== Daftar Transaksi ===")
    for i, t in enumerate(transactions, start=1):
        print(f"{i}. Type: {t['type']} | Amount: {t['amount']} | Description: {t['description']}")

    
