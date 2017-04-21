from subprocess import call

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

write = open("phase6.txt", 'w')

for g in range(6):
    a += 1
    for h in range(6):
        b += 1
        for i in range(6):
            c += 1
            for j in range(6):
                d += 1
                for k in range(6):
                    e += 1
                    for l in range(6):
                        f += 1
                        if a==b or a==c or a==d or a==e or a==f or b==c or b==d or b==e or b==f or c==d or c==e or c==f or d==e or d==f or e==f:
                            continue
                        write.write(str(a) + " " + str(b) + " " + str(c) + " "  + str(d) + " " + str(e) + " "  + str(f))
                    f = 0
                e = 0
            d = 0
        c = 0
    b = 0
