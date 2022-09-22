def main():
    #x1 = 0, x2 = 10
    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    ans = create_list(x1,x2)
    print(ans)
    
def create_list(x1,x2):
    list_ans = []
    for x in range(x1,x2+1):
        y = -x**2+15*x+9
        list_ans.append(y)
    return list_ans
    
if __name__ == "__main__":
    main()
