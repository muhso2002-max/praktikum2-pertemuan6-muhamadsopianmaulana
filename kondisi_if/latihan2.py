print("=== Program Mengurutkan Data ===")
jumlah_data = int(input("Masukkan jumlah data (minimal 3): "))

if jumlah_data < 3:
    print("Jumlah data harus minimal 3!")
else:
    data = []
    for i in range(jumlah_data):
        nilai = int(input(f"Masukkan data ke-{i+1}: "))
        data.append(nilai)

    data.sort()

    print("\nUrutan bilangan:")
    for d in data:
        print(d, end=" ")  # tampil menyamping
    print()  # biar barisnya rapi setelah selesai
