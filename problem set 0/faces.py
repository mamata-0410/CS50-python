# passing string to place emoticons 



def main():
  string = input("Enter the string with emoticons: \n")
  print("The string with emoticons is: \n", convert(string))


def convert(str):
  str = str.replace(":)", "🙂")
  str = str.replace(":(", "🙁")
  return str

main()