def main ():
    output = ""
    print("Please Enter 3 nunmbers")
    for counter in range(3):
        num = int (input())
        output = output + " num=" +  str(num) + ""
        print("Counter", counter)
    print("Output : " , output)

if __name__ == '__main__':
    main()