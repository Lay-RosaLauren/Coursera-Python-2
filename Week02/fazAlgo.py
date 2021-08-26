def fazAlgo(string):
    pos = len(string)-1
    string = string.upper()
    while pos >= 0:
        print(string[pos],end = "")
        pos = pos - 1

fazAlgo("paralelepipedo")
