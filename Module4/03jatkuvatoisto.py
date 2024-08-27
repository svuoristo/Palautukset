print("Press enter when you want to end the program.")
n = input("Enter a number: ")
biggest = n
smallest = n

while n != "":
    n = input("Enter another number: ")
    print("n: " + str(n))
    print("suurin " + str(biggest))
    print("pienin " + str(smallest))
    print()
    if n > biggest:
        biggest = n
    if n < smallest:
        smallest = n
    print("Muutoksen jälkeen:")
    print("n: " + str(n))
    print("suurin " + str(biggest))
    print("pienin " + str(smallest))
    print()

print("The biggest number is", biggest)
print("The smallest number is", smallest)
