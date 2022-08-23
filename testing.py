def silly():
    res = []
    done = False
    while not done:
        elem = input()
        if elem == '':
            done = True
        else:
            res.append(elem)
    print(f"res: {res}")
    tmp = res
    tmp2 = res[:]
    tmp.reverse()
    isPal = (res == tmp)
    print(f"tmp: {tmp}, res: {res}, tmp2: {tmp2}")
    if isPal:
        print("its palindrome")
    else:
        print("its not palindrome")

if __name__ == "__main__":
    silly()