def distinctList(myList):
    uniqueElements = []
    for item in myList:
        if item not in uniqueElements:
            uniqueElements.append(item)
    return uniqueElements

def calculatePercen(i,n): 
    i = float(i)
    n = float(n)  
    return ((i/n) * 100) > 5

def mostActive(customers):
    output = []
    counter = 0
    disCst = distinctList(customers)
    for dcst in disCst:
        for cst in customers:
            if(dcst == cst):
                counter = counter + 1
        if(calculatePercen(counter , len(customers))):
            output.append(dcst)
            counter = 0
        else:
            counter = 0
    return output

customers = []
n = int(input("Enter the number of customer: "))
for i in range(n):
    cust = input("Enter the customer name: ")
    customers.append(cust)

print(mostActive(customers))