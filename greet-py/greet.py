import argparse

def main():
    # Create the parser object
    parser = argparse.ArgumentParser(description="Simple CLI app example")

    # Define a positional argument (required)
    parser.add_argument('name', help='Your name')

    # Define an optional flag
    parser.add_argument('--shout', action='store_true', help='Print name in uppercase')

    # Parse the args
    args = parser.parse_args()

    # Use the arguments in your program logic
    if args.shout:
        print(f"HELLO, {args.name.upper()}!")
    else:
        print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()

