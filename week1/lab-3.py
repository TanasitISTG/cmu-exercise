def main():
    print(my_abs(-10))
    print(my_abs(10))

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

if __name__ == "__main__":
    main()