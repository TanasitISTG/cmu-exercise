def main():
    print(max_mid_min(300, 25, -2))

def max_mid_min(a, b, c):
    if a > b:
        if a > c:
            if b > c:
                return a, b, c
            else:
                return a, c, b
        else:
            return c, a, b
    else:
        if b > c:
            if a > c:
                return b, a, c
            else:
                return b, c, a
        else:
            return c, b, a

if __name__ == "__main__":
    main()