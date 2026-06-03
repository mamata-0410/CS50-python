# ommit vowels from string

def main():
  s= input("Input: ")
  out= ommit_vowels(s)
  print("Output: ", out)

def ommit_vowels(s):
  output = ""
  for c in s:
    if c.lower() in ["a","e","i","o","u"]:
      continue
    else:
      output += c
  return output


main()