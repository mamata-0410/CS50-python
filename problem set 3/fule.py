def main():
  percentage = convert()
  if percentage <= 1:
    print("E")
  elif percentage >= 99:
    print("F")
  else:
    print(f"{percentage}%")
    
def convert():
  while True:
    fraction = input("Fraction: ")
    try:
      x, y = fraction.split("/")
      x= int(x)
      y= int(y)
      if y == 0:
        raise ZeroDivisionError
      return round(x/y*100)
    
    except (ValueError, ZeroDivisionError):
      pass

main()

