def main():
  get_item()


def get_item():
  items={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
        }
  total = 0.00
  try:
    while True:
      item = input("Item: ")
      if item.title() in items:
        total += items[item.title()]
        print(f"Total: ${total:.2f}")
  except EOFError:
    print(f"Total: ${total:.2f}")


main ()