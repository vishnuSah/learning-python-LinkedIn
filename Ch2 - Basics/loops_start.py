#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    # while (x < 5):
    #     x = x + 1
    #     print(x)

    # TODO: define a for loop
    # for x in range(5,10):
    #     if x == 8:
    #         continue
    #     print(x)

    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    # for day in days:
    #     print(day)


    # TODO: use the break and continue statements


    # TODO: using the enumerate() function to get index 
    for i,day in enumerate(days):
        print(i,day)
  
if __name__ == "__main__":
    main()
