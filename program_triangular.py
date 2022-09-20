def triangular(i):
    if i < 2:
        return 1
    else:
        return i + triangular(i-1)
        
i = int(input("Masukkan bilangan : "))
print(f"{i}t=", triangular(i))
