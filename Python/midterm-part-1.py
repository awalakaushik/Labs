def my_fun(x):
    z = 0
    for item in x:
        m = x.count(item)
        if m > z:
            z = m
    return z

y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
print (my_fun(y))















