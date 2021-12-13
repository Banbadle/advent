def count(offset=1):
    
    with open("input.txt", "r+") as f:
        with open("input.txt", "r+") as g:  
            count = 0
            for i in range(0,offset):
                next(f)
                
            for next_num in f:
                last_num = next(g)

                if int(next_num) > int(last_num):
                    count += 1
                
            print(count)

count(1)
count(3)