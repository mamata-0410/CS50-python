# convert camelCase to snake_case

def main ():
  camelCase = input ("enter camelcase:")
  snake_case = convert(camelCase)
  print ("snake_case: ", snake_case)


def convert (camelCase):
  s=""
  for c in camelCase:
    if c.isupper():
      s += "_" + c.lower()
    else:
      s += c
  return s

main()