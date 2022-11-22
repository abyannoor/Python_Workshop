#  Kelvin to Fahrenheit
print("\nPROGRAM KONVERSI TEMPERATUR\n")
kelvin = float(input('Input Suhu (°K) : '))
print("Suhu adalah ",kelvin, "°F")

# kelvin to fahrenheit
# F = 1,8 x (K - 273) + 32.
fahrenheit = (1.8 * (kelvin - 273)) + 32
print("Suhu dalam Fahrenheit adalah ",fahrenheit, "F")