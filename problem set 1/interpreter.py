def main():
  exp = input ("Expression: ")
  examine (exp)

def examine (exp):
  x, y, z = exp.split ()
  x = int (x)
  z = int (z)
  match y:
    case "+":
      print (float(x+z))
    case "-":
      print (float(x-z))
    case "*":
      print(float(x*z))
    case "/":
      print (float(x/z))
    case _:
      print ("unknown operator")

main()
  
