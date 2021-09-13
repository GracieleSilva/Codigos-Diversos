i, im, f, fm = list(map(int, input().split()))

if f>i and fm>=im: 
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif f>i and im>fm:
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif i>f and fm>=im:
    
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif i>f and im>fm:
   
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
elif f==i and fm>im:
   
    print("O JOGO DUROU 0 HORA(S) E %i MINUTO(S)" %(h,m))
elif i==f and im==fm:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")