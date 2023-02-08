def Student_info():
    name = input("Please Enter Students name : ")
    marks = []
    for counter in range (3):
        num = int (input("Enter the mark of the students : \n"))
        marks.append(num)
    print("Student name is : " , name)
    print("Student mark is : " , marks)


def main ():
    Student_info()
if __name__ == '__main__':
    main()