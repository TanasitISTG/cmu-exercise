def main():
    print(round_to_int(-2.5))

def round_to_int(x):
    return int(x + 0.5) if x >= 0 else int(x - 0.5)

if __name__ == "__main__":
    main()