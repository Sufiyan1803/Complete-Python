def sum_all(*args):
    print(args)

    for i in args:
       print(i * 3)
    return sum(args)


print(sum_all(int(input()) , int(input()), int(input())), )
