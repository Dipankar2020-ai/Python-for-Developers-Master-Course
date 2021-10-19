def Assign(i, f, s, b):
    # Write your code here
    w=i
    x=f
    S=s
    B=b
    print(w)
    print(x)
    print(S)
    print(B)
    print(['b', 'f', 'i', 's', 'w', 'x', 'y', 'z'])
    
if __name__ == '__main__':

    i = int(input().strip())

    f = float(input().strip())

    s = input()

    b = input().strip()
    
    Assign(i, f, s, b)
