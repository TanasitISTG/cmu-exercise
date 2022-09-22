def main():
    print(reverse_digits(1234))

def reverse_digits(x):
    x = str(x)
    x = list(x)
    x.reverse()
    x = ''.join(x)
    x = int(x)
    #return int(str(x)[::-1])
    return x

if __name__ == "__main__":
    main()