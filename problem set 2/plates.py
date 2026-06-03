def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isdigit() or s[1].isdigit():
        return False
    number_started = False
    for c in s:
        if c in [" ", ".", ","  ]:
            return False
        if c.isdigit():
            if not number_started:
                if c == "0":
                    return False
                number_started = True
        elif number_started:
            return False
    return True

main()