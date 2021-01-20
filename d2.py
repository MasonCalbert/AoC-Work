
#  Part one

with open('d2.txt', 'r') as infiile:
    ans = 0
    for line in infiile:
        # The setup
        minnum, maxnum = line.split('-')
        maxnum = maxnum.split()
        let = maxnum[1]
        let = let[0]
        password = maxnum[2]
        maxnum = maxnum[0]

        # The work
        outcome = True
        count = password.count(let)
        if count < int(minnum) or count > int(maxnum):
            outcome = False
        if outcome == True:
            ans += 1
    #print(ans)




# Part two 

with open('d2.txt', 'r') as infiile:
    ans = 0
    for line in infiile:
        # The setup 
        posone, postwo = line.split('-')
        postwo = postwo.split()
        let = postwo[1]
        let = let[0]
        password = postwo[2]
        postwo = postwo[0]

        # The work
        outcome = True
        if password[int(posone)-1] == let and password[int(postwo)-1] == let:
            outcome = False
        if password[int(posone)-1] != let and password[int(postwo)-1] != let:
            outcome = False
        if outcome == True:
            ans += 1
    print(ans)