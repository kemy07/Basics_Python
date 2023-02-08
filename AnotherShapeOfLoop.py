def main ():
    print("Please Enter 3 nunmbers")
    max = 0
    min = 100
    for counter in range(5):
        num = int (input())
        if num > max:
           max = num
        if num < min:
           min = num
    print("Max is :" , max , "Min is :" , min)

if __name__ == '__main__':
    main()