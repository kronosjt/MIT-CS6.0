# Problem Set 2 (Part I)
# Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55 McNuggets
# , by finding solutions to the Diophantine equation. To determine if it is
# possible to buy exactly n McNuggets, one has to solve a Diophantine equation:
# find non-negative integer values of a, b, and c, such that
# 6a + 9b + 20c = n.

McNuggets = (50, 51, 52, 53, 54, 55)
tupcounter = 0
while(tupcounter<6):
    print 'To buy ', McNuggets[tupcounter]
    for i in range(0, 50):
        for j in range(0, 50):
            for k in range(0, 50):
                if((i*6 + j*9 + k*20) == McNuggets[tupcounter]):
                    print i, '*6 + ', j, '*9 + ', k, '*20 =', McNuggets[tupcounter]
    tupcounter+=1

