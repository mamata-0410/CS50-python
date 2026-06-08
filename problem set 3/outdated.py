def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            # Format: M/D/YYYY
            if "/" in date:
                month, day, year = date.split("/")

                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

            # Format: Month D, YYYY
            elif "," in date:
                month, day, year = date.split()

                month = month.capitalize()

                if month not in months:
                    continue

                day = day.rstrip(",")

                if not day.isdigit():
                    continue

                month = months.index(month) + 1
                day = int(day)
                year = int(year)

                if 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

        except (ValueError, IndexError):
            pass


main()
