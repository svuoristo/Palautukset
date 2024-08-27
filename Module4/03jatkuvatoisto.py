print("Press enter when you want to end the program.")
n_str = input("Enter a number: ")
if n_str == "":
    print("Ei annettuja lukuja.")

else:
    biggest = float(n_str)
    smallest = float(n_str)

    while n_str != "":
        n = float(n_str)
        if n > biggest:
            biggest = n
        if n < smallest:
            smallest = n
        n_str = input("Enter another number: ")

    print("The biggest number is", str(biggest))
    print("The smallest number is", str(smallest))
