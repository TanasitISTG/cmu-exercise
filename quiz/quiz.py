def main():
    h_list  = [1.5617, 1.5252, 1.5778]
    w_list = [66.8450,74.4070, 87.2640]

    bmi_output = cal_bmi_list(h_list, w_list)
    print(bmi_output)
    
def cal_bmi_list(h,w):
        ans = cal_bmi(h,w)
        ans_list = []
        for i in range (len(ans)):
            ans_list.append([h[i],w[i],ans[i]])
        return ans_list

def cal_bmi(h,w):
    bmi = [] 
    for i in range(len(h)):
        bmi.append(w[i]/(h[i]**2))
    return bmi

if __name__ == "__main__":
    main()