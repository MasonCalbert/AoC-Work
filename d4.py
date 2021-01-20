# Problem 1

with open("d4.txt",'r') as inFile:
    doc = []
    total = 0
    for line in inFile:
        if line == "\n":
            # gets data for passport
            numcat = 0
            cid = False
            for slist in doc:
                for item in slist:
                    if "cid" in item:
                        cid = True
                    numcat += 1
            
            # checks and adds to total
            valid = False
            if numcat == 8:
                valid = True
            elif numcat == 7 and cid == False:
                valid = True
            
            # updates total
            if valid == True:
                total += 1
            
            # resets
            doc = []
        
        # Makes passport 1 variable
        else:
            doc.append(line.split())


##print(total)



# Problem 2 

