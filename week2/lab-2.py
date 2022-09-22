def main():
    print(cal_bmi(1.735, 62.2))

def cal_bmi(h, w):
    bmi = w / (h ** 2)
    return round(bmi, 4)

if __name__ == "__main__":
    main()