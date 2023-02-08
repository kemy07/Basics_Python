def Average () :
    x = int (input("Enter the Range That you want : "))
    sum = 0
    for counter in range (x):

        num = int (input("Enter The numbers : \n "))
        sum = sum + num
        res = sum / x
    print("the Average Is " , res)


def main ():
    Average()
if __name__ == '__main__':
    main()