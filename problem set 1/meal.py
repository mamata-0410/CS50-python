def main():
    print("Please enter time in 24-hours format")
    time = input("What time is it? ")
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    
    hours = int(hours)
    minutes = int(minutes)

    t = hours + minutes / 60

    if 7 <= t < 8:
        print("breakfast time!!")

    elif 12 <= t < 13:
        print("lunch time!!")

    elif 18 <= t < 19:
        print("dinner time!!")

    else:
        print("not meal time!!")

main()