# Celcius
# Fahrenheit
# Kelvin
# Reamur
print("WELCOME TO TEMPERATURE CONVERT")
print("Pilih Jenis Konversi Awal")
print("1. Celcius")
print("2. Fahrenheit")
print("3. Kelvin")
print("4. Reamur")
print("5. Quit")

input_covert = input("Pilihan jenis konversi awal : ")

if input_covert == "1":
    celcius_input = int(input("Masukkan nilai konversi celsius : "))
    fahrenheit_convert = float(9/5) * celcius_input + 32
    kelvin_convert = celcius_input + 273.15
    reamur_convert = float(4/5) * celcius_input
    print(celcius_input,"C", "=", fahrenheit_convert,"F")
    print(celcius_input,"C", "=", kelvin_convert,"K")
    print(celcius_input,"C", "=", reamur_convert,"R")
elif input_covert == "2":
    fahrenheit_input =  int(input("Masukkan nilai konversi fahrenheit : "))
    celcius_convert = (fahrenheit_input - 32) * float(5/9)
    kelvin_convert = (fahrenheit_input + 459.67) * float(5/9)
    reamur_convert = float(4/9) * (fahrenheit_input - 32)
    print(fahrenheit_input,"F", "=", celcius_convert,"C")
    print(fahrenheit_input,"F", "=", kelvin_convert,"K")
    print(fahrenheit_input,"F", "=", reamur_convert, "R")
elif input_covert == "3":
    kelvin_input = int(input("Masukkan nilai konversi kelvin : "))
    celcius_convert = kelvin_input - 273.15
    fahrenheit_convert = float(kelvin_input * 9/5) - 459.67
    reamur_convert = float(4/5) * (kelvin_input - 273)
    print(kelvin_input,"K", "=", celcius_convert, "C")
    print(kelvin_input,"K", "=", fahrenheit_convert, "F")
    print(kelvin_input,"K", "=", reamur_convert, "R")
elif input_covert == "4":
    reamur_input = int(input("Masukkan nilai konversi reamur : "))
    celcius_convert = float(reamur_input/0.8)
    fahrenheit_convert = float(reamur_input * 2.25) + 32
    kelvin_convert = float(reamur_input / 0.8) + 273.15
    print(reamur_input,"R", "=", celcius_convert, "C")
    print(reamur_input,"R", "=", fahrenheit_convert,"R")
    print(reamur_input,"R", "=", kelvin_convert,"K")
elif input_covert == "5":
    print("Terimkasih sudah menggunakan konversi ini")
    quit()
else:
    print("Pilihan input salah, Silahkan masukkan yang benar!")