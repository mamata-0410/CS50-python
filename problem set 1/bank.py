def main ():
  greet = input ("Greeting: ")
  greeting (greet)

def greeting (greet):
  if greet.lower (). startswith ("hello"):
    print ("$ 0")
  elif greet.lower (). startswith ("h"):
    print ("$ 20")
  else:    
    print ("$ 100")
  

main ()