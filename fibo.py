def list_fibo(n):
    fibo_list = [1, 1]
    if n <= 2:
        return fibo_list[:n]  # This is cool concept
    else:
        i = 3
        while i <= n:
            i += 1
            fibo_list.append(fibo_list[-1] + fibo_list[-2])
        return fibo_list


print(list_fibo(20))
