#right angled triangle
n = int(input("Enter number of rows : "))
for i in range(1, n + 1):
    print('*' * i)

    
    
############################################



#centered pyramid
n = int(input("Enter number of rows: "))
for i in range(1, n+1):
    print(' ' * (n - i)+ '*' * (2 * i-1))




############################################



#diamond
n = int(input("Enter diamond helf-height (rows above middle)"))
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

    print('*' * (2* n +  1))

    for i in range(n, 0, -1):
        print(' ' * (n -i) + '*' *(2 * i -1))