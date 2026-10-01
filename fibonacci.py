
def list_fibo(n):
    if n == 1:
        global fibo_list
        fibo_list = [1]
        return fibo_list
    elif n == 2:
        fibo_list = [1, 1]
        return fibo_list
    else:
        fibo_list = [1, 1]
        i = 3
        while i <= n:
            i += 1
            fibo_list.append(fibo_list[-1] + fibo_list[-2])
        return fibo_list


print(list_fibo(10))
