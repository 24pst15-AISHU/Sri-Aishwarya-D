# Beam Deflection Calculator

P = float(input("Load (kN): "))
L = float(input("Beam length (m): "))
E = float(input("Modulus of Elasticity (MPa): "))
I = float(input("Moment of Inertia (m4): "))

deflection = (P * (L**3)) / (48 * E * I)

print("Maximum Deflection =", deflection, "meters")
