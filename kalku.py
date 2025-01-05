def main():
  """Program kalkulator sederhana."""
  while True:
    print("Pilih Operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("0. Keluar")

    choice = input("Pilih operasi (1/2/3/4/0): ")

    if choice == '0':
      break

    try:
      num1 = float(input("Masukkan bilangan pertama: "))
      num2 = float(input("Masukkan bilangan kedua: "))

      if choice == '1':
        result = num1 + num2
        print("Hasil:", num1, "+", num2, "=", result)
      elif choice == '2':
        result = num1 - num2
        print("Hasil:", num1, "-", num2, "=", result)
      elif choice == '3':
        result = num1 * num2
        print("Hasil:", num1, "*", num2, "=", result)
      elif choice == '4':
        if num2 == 0:
          print("Pembagian dengan nol tidak diperbolehkan.")
        else:
          result = num1 / num2
          print("Hasil:", num1, "/", num2, "=", result)
      else:
        print("Pilihan tidak valid.")
    except ValueError:
      print("Masukkan angka yang valid.")

if name == "main":
  main()