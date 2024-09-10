def find_evklid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b

if __name__ == "__main__":
    print(find_evklid(256, 130))