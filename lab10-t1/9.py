def c_sort():
    lis = []
    a = int(input("Enter a number: "))
    t_com = 0
    while a != 99999:
        comparisons = 0
        lis.append(a)
        i = len(lis) - 2
        while i >= 0:
            if lis[i] <= a:
                comparisons += 1
                lis1 = lis[:i+1]
                lis1.append(a)
                lis2 = lis[i+1:-1]
                lis = lis1 + lis2
                i = -1
            elif lis[i] > a and i > 0:
                i -= 1
                comparisons += 1
            elif lis[i] > a and i == 0:
                lis1 = []
                lis1.append(a)
                lis = lis1 + lis[:-1]
                i -= 1
                comparisons += 1
        t_com += comparisons
        if a != 99999:
            print("Comparisons: {}".format(comparisons))
        else:
            print("Total comparisons: {}".format(t_com))
        print(lis)
        a = int(input("Enter a number: "))
    print("Total comparisons: {}".format(t_com))
    print(lis)

c_sort()
