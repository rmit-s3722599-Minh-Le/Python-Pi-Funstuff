def binaryGap(N):
    # write your code in Python 3.6
    bin_N = bin(N).strip('0b')
    # print(bin_N)
    sol = 0
    count = 0
    for c in bin_N:
        if c == '1':
            if count > sol:
                sol = count
            count = 0
        elif c == '0':
            count+= 1
    return sol

def main():
    print("Enter digit here")
    num = int(input())
    print(binaryGap(num))

if __name__ == "__main__":
    main()