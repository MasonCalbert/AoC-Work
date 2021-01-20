# Problem one

with open('d3.txt','r') as infile:
        pos = 0
        num = 0
        for line in infile:
            line = line.strip()  # Length is 31
            tree = False
            if line[pos] == "#":
                tree = True
            if tree == True:
                num += 1
            pos += 3
            if pos >= 31:
                pos %= 31
        print(num)













for i in [1,5,7]:
    with open('d3.txt','r') as infile:
        pos = 0
        num = 0
        for line in infile:
            line = line.strip()  # Length is 31
            tree = False
            if line[pos] == "#":
                tree = True
            if tree == True:
                num += 1
            pos += i
            if pos >= 31:
                pos %= 31
    print(num)





# Skip 2 lines
with open('d3.txt','r') as infile:
    pos = 0
    num = 0
    linenum = 0
    for line in infile:
        if linenum % 2 == 0:
            line = line.strip()  # Length is 31
            tree = False
            if line[pos] == "#":
                tree = True
            if tree == True:
                num += 1
            pos += 1
            if pos >= 31:
                pos %= 31
        linenum += 1
    print(num)
