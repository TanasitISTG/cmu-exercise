def main():
    print(convert_f2c(50))

def convert_f2c(f):
    c = (f - 32) * 5 / 9
    return c

if __name__ == "__main__":
    main()