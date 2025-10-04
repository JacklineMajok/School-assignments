#problem1.py
#Name: Jackline Yom Ajoh Majok
#Date: 23/09/025
#Description: A program that takes in an amount in cedis and returns the breakdown of ghanaian currency denominations

def breakdown(amount):
    amount = round(amount*10)/10
    pesewas = int(round(amount*100))
    denominations = [20000,10000,5000,2000,1000,500,200,100,50,20,10]
    result = []
    for denom in denominations:
        count = pesewas//denom
        pesewas = pesewas%denom
        result.append(count)
    return tuple(result)

def main():
    amount = float(input("enter the amount in cedis:"))
    breakdown_tuple = breakdown(amount)
    print("Denominations breakdown:",breakdown_tuple)
if __name__ == "__main__":
    main()



                