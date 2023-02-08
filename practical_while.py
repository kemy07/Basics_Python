def main () :
    counter = 0
    sum = 0
    print("Please Enter Ten numbers : ")
    output = ""
    while counter < 10 :
        num = int (input(""))
        sum = sum + num
        counter = counter + 1
        average = sum / 10
    print("output " , average)
if __name__ == '__main__':
    main()