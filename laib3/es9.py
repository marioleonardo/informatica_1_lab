spesa = float(input("Quanto ha speso il cliente? "))

if spesa >= 210:
    buono = 0.14 * spesa
elif spesa >= 150:
    buono = 0.12 * spesa
elif spesa >= 60:
    buono = 0.10 * spesa
elif spesa >= 10:
    buono = 0.08 * spesa
else:
    exit(0)

print("il buono vale:", "%.2f" % (buono))
