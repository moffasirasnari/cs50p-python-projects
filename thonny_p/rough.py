def doOverlap(L1, R1, L2, R2):
        #code here
        x1 ,y1 =L1 
        x2, y2 =R1
    #right_top = x2, y1
    #left_bottom = x1,y2
        points_1 = [[x1,y1],[x2,y2],[x1,y2],[x2,y1]]
        
        p1 , q1 =L2
        p2 , q2 =R2
    #right_top = p2, q1
    #left_bottom = p1,q2
        points_2 = [[p1,q1],[p2,q2],[p1,q2],[p2,q1]]
        for x in points_1:
            for y in points_2:
                if ((x[0] >=y[0])and(x[1] >= y[1])) or ((x[0]<=y[0])and(x[1]<=y[1])):    
                    return print("y")
                else:continue
            continue
        return print("n")
    
doOverlap((-91,100),(-64,-39),(63,-71),(89,-74))
    
    