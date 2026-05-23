# calculating einstin's enery

def main():
  mass = float (input ("Enter the mass in kg:  "))
  print("The energy is: ", energy(mass), "joules")

def energy(mass):
  c= 3e8 # speed of light in m/s
  energy = mass * c**2
  return energy

main()
 