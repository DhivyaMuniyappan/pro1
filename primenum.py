n = int(input("Enter any number: "))
if (n > 1):
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "NO - Not prime num")
            break
    else:
        print(n, "YES - prime number")

else:
    print(n, "NO - Not prime number")

 
 
