# Constants
G = 6.674e-11  # Gravitational constant (Nm^2/kg^2)
mass_earth = 5.972e24      # Mass of Earth in kg
mass_moon = 7.34767309e22  # Mass of Moon in kg
mass_sun = 1.989e30        # Mass of Sun in kg

distance_earth_sun = 1.496e11   # Distance Earth-Sun (m)
distance_moon_earth = 3.844e8   # Distance Moon-Earth (m)

# Gravitational force between Earth and Sun
F_earth_sun = G * (mass_earth * mass_sun) / (distance_earth_sun ** 2)

# Gravitational force between Moon and Earth
F_moon_earth = G * (mass_moon * mass_earth) / (distance_moon_earth ** 2)

# Results
print(f"Gravitational Force between Earth and Sun: {F_earth_sun:.2e} N")
print(f"Gravitational Force between Moon and Earth: {F_moon_earth:.2e} N")

# Comparison
if F_earth_sun > F_moon_earth:
    print("\n🌍 The Earth is more strongly attracted to the Sun than to the Moon.")
else:
    print("\n🌙 The Moon is more strongly attracted to the Earth than the Earth is to the Sun.")



# Sample Output:
#Gravitational Force between Earth and Sun: 3.54e+22 N
#Gravitational Force between Moon and Earth: 1.98e+20 N
#🌍 The Earth is more strongly attracted to the Sun than to the Moon.