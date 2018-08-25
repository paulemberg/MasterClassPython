__author__ = 'dev'

age = 24

print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5},{6} and {7} ".format(31,"January", "March", "May",
                                                                          "July","August","October", "December"))
print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))



print("My age is %d years" % age)

age = 24
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

print("Pi is approximately %12f" % (22 / 7))

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))


    quantity = 10
price = 5.0
total = quantity * price
tax = total / 5

Total = total + tax

print(total)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])


data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[1:5])

a = 45
b = 15
c = 3

print(a - b / c)