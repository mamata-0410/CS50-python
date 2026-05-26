def main ():
  file = input ("File name: ")
  check_file (file)

def check_file (file):
  if file.lower (). endswith (".gif"):
    print ("image / gif ")
  elif file.lower (). endswith (".jpg") or file.lower ().endswith(".jpeg"):
    print ("image / jpeg")
  elif file.lower (). endswith (".png"):
    print ("image / png")
  elif file.lower ().endswith (".pdf"):
    print ("application / pdf")
  elif file.lower ().endswith (".txt"):
    print ("text / plain")
  elif file.lower ().endswith (".zip"):
    print ("application / zip")
  else:
    print ("application / octet-stream")
  

main ()