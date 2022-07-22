def numpat(n):

   num = 1


   for i in range(1, n):

       #
       num = 2
       odd=i+1
       if(odd%2==0):
           num=1
       else:
           num=2

       for j in range(0, i,2):
           # printing number
           print(num, end=" ")


           num = num + 2


       # next row k liye
       print("")


# pahle input
n=int(input("Enter any no.:"))
numpat(n)
def numpat(n):

   num = 1


   for i in range(1, n):

       #
       num = 2
       odd=i+1
       if(odd%2==0):
           num=1
       else:
           num=2

       for j in range(0, i,2):
           # printing number
           print(num, end=" ")


           num = num + 2


       # next row k liye
       print("")


# pahle input
n=int(input("Enter any no.:"))
numpat(n)
