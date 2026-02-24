def show_transaction(transactions):

    print("\n=== DAFTAR TRANSAKSI ===")
    
    if not transactions:
        print("Belum ada data transaksi.")
        return

    # Gunakan enumerate untuk memberikan nomor urut
    for i, t in enumerate(transactions, 1):
        tipe = t.get('type', 'N/A').upper()
        ket = t.get('description', 'Tanpa keterangan')
        jumlah = t.get('amount', 0)
        
        print(f"{i}. [{tipe}] {ket}: Rp{jumlah}")