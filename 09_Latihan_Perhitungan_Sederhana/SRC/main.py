# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input('Input Suhu (°C) : '))
print("Suhu adalah ",celcius, "°C")


# reamur
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah ",reamur, "R")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah ",fahrenheit, "F")


# kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah ",kelvin, "K")