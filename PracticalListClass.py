def main ():
  name = []
  mark = []
  for counter in range (3) :
      val1 = input("Please Enter Student name :")
      val2 = int (input("Please Enter Student mark :"))
      name.append(val1)
      mark.append(val2)
  #name.remove(name[2])
  name.clear()
  print("names : " , name)
  print("_______________")
  print("marks : " , mark)

if __name__ == '__main__':
    main()