for i in range(1001,10000,2):
    k = i
    km = k//1000           #millier
    kc = (k//100)%10            #centaine
    kd = (k//10)%10        #dizaine
    ku = (k%100)%10        #unité
    if km<kc<kd<ku:
        if (km*kc*kd*ku)%2!=0:
            if (km+kc+kd+ku)%2==0:
                print(km,kc,kd,ku,(km+kc+kd+ku)%2)
                print(km+kc+kd+ku)

