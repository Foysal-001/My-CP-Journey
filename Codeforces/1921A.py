for i in range(int(input())):
     x1, y1 = map(int, input().split())
     x2, y2 = map(int, input().split())
     x3, y3 = map(int, input().split())
     x4, y4 = map(int, input().split())
     
     if x1 == x3:
     

        side = ((x1 - x3)**2 + (y1 - y3)**2)**(1/2)

        area = int(side ** 2)

        print(area)
     
     elif x2 == x4:
        side = ((x2 - x4)**2 + (y2 - y4)**2)**(1/2)

        area = int(side ** 2)

        print(area)


     elif x1 == x2:
        side = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

        area = int(side ** 2)

        print(area)

     elif x1 == x4:
        side = ((x1 - x4)**2 + (y1 - y4)**2)**(1/2)

        area = int(side ** 2)

        print(area)


     elif x3 == x4:
        side = ((x3 - x4)**2 + (y3 - y4)**2)**(1/2)

        area = int(side ** 2)

        print(area)



     else:
        side = ((x2 - x3)**2 + (y2 - y3)**2)**(1/2)

        area = int(side ** 2)

        print(area)