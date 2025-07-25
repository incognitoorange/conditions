costprice =int(input("enter cp :"))
sellingprice =int(input( "enter the sp:"))

if(sellingprice >costprice):
    print("profit")
    pt=sellingprice-costprice
    print(pt)
else:
    print("you made a loss of")
    ls=costprice-sellingprice
    print(ls)