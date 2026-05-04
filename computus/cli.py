import argparse
from .chronology import indiction
from .roman import arabic_to_roman

def main():
    parser = argparse.ArgumentParser(description="Calculate indiction")
    parser.add_argument("year", type=int)
    parser.add_argument("--calendar", default="AD")
    args = parser.parse_args()

    i = indiction(args.year, args.calendar)
    print(f"Indiction: {i} ({arabic_to_roman(i)})")

if __name__ == "__main__":
    main()