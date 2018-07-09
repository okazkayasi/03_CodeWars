def pisagor_three(n = 1000):
    # brute-force ancak her sayiyi denemek zorundad degiliz.
    # c'yi pisagor formulunden buluyoruz. a iki sayidan da kucuk olacak
    # b, a'dan buyuk c'den kucuk olacak.
    # a < b < c
    # a + b + c = n (1000)
    # a,  n/3'ten (333) kucuk olmak zorunda
    # b, a'dan buyuk ancak kalanin yarisindan kucuk olmak zorunda -> (1000 - a)/2
    a_end = n/3
    for a in range(a_end):
        b_start = a+1
        b_end = (1000-a)/2
        for b in range(b_start, b_end):
            # c'yi pisagor formulu ile buluyoruz
            c = (a**2 + b**2)**0.5
            # 3 sayinin toplai n (1000) ettiyse tamam.
            if a + b + c == n:
                print "a: {}, b: {}, c: {}".format(a,b,c)
                return a*b*c
    return "kriteri saglayan 3 tamsayi bulunmamaktadir"

print pisagor_three()

