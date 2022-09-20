def beta1_value():
    if fc <= 28:
        beta1 = 0.85
    else:
        beta1 = max(0.85 - (0.05 * ((fc - 28)/7)), 0.65)
    return beta1

def steel_areas():
    import math
    As = (math.pi * dbar ** 2)/4 * n
    Asprime = (math.pi) * (dbarprime **2/4) * nprime
    return As, Asprime

def effective_depth():
    number_of_layer = next(layer for layer in range(1, 6) if (b - 2 * cc -2 * ties - (n/layer) * dbar)/((n/layer) - 1) > dbar)
    multi_layer = number_of_layer - 0.5
    deff = h - cc - ties - dbar * multi_layer
    return deff

def topbar_depth():
    number_of_layer = next(layer for layer in range(1, 6) if (b - 2 * cc -2 * ties - (nprime/layer) * dbarprime)/((nprime/layer) - 1) > dbarprime)
    multi_layer = number_of_layer - 0.5
    deff = h - cc - ties - dbar * multi_layer
    return deff

def stress_strain():
    # T = C + Cprime
    # As *fy = 0.85 * fc * a * b + Asprime * fsprime
    # As * fy = 0.85 * fc * beta1 * c * b + Asprime * ec * Es * ((c - dprime)/c)
    # 0.85 * fc * b * beta1 * c**2 + (Asprime * ec * Es - As * fy) * c - Asprime * ec * Es * dprime = 0
    # Quadratic equation: Ax **2 + Bx + c = 0
    # Discriminant: D = (B**2) - (4 * A * C)
    # x1 = (- B + math.sqrt(D)/2 * A) 
    # x2 = (- B - math.sqrt(D)/2 * A)
    import math
    A = 0.85 * fc * b * beta1
    B = Asprime * ec * Es - As * fy
    C = - Asprime * ec * Es * dprime
    D = (B**2) - (4 * A * C)
    c = (- B + math.sqrt(D)/2 * A)
    a = beta1 * c
    es = ec * (deff - c)/c
    fs = es * Es
    esprime = ec * ((c - dprime)/c)
    fsprime = esprime * Es
    return fs, fsprime, es, a, c

def strength_factor_classification():
    phi = 0.65 + (0.25 * (es - ey)/(0.005 - ey))
    if phi > 0.90:
        phi, classify = 0.90, 'Tension-controlled'
    elif phi < 0.65:
        phi, classify = 0.65, 'compression-controlled'
    else:
        phi, classify = phi, 'Transition'
    return phi, classify

def forces_capacity():
    C = (0.85  * fc * a * b)/1000
    Cprime = (Asprime * (min(fy, fsprime)))/1000
    T = (As * (min(fy, fs)))/1000
    Mn = (C * (deff - (a/2))) + (Cprime * (deff - dprime))
    Mu = (phi * Mn)/1000
    return Mu, T, C, Cprime
    
def steel_ratio_check():
    rho = (As - Asprime)/(b * deff)
    rho_max = (3/7) * ((0.85 * fc * beta1)/fy)
    rho_min1 = 1.4/fy
    rho_min2 = (fc ** (1/2))/(4 * fy)
    if rho <= rho_max and rho >= min(rho_min1, rho_min2):
        return 'steel ratio is with limits: ''\u03C1 = {:.4f}'.format(rho)
    else: 
        return 'steel ratio exceeds the maximum limit, overly reinforced: ', '\u03A1'+'max = {:.4f}'.format(rho)
                           
def rebar_suggestion():
    dbar_sizes = [16, 20, 25]
    n_list = []
    number_of_layer_list = []
    
    dbarprime_sizes = []
    nprime_list =[]
    for dbar in dbar_sizes:
        import math
        Abar = (math.pi * dbar**2)/4 
        rho_max = (3/7) * (0.85 * fc * beta1)/fy
        deff_initial = h - cc -ties - dbar * 0.5
        As_max = rho_max * b * deff_initial
        n = math.ceil(As_max/Abar)
        n_list.append(n)
        number_of_layer = next(layer for layer in range(1, 6) if (b - 2 * cc - 2 * ties - (n/layer)*dbar)/((n/layer)-1) > dbar)
        number_of_layer_list.append(number_of_layer)
        dbarprime = dbar
        dbarprime_sizes.append(dbarprime)
        if number_of_layer > 1 and n/number_of_layer > 2:
            nprime = 3
        else:
            nprime = 2
        nprime_list.append(nprime)
    dict = {'Bottom Bars': dbar_sizes, 'Qty(bottom)': n_list, 'layer': number_of_layer_list, 'Top Bars': dbarprime_sizes, 'Qty (Top)': nprime_list}
    import pandas as pd
    df = pd.DataFrame(dict)
    return df
print('\n...........................................................................')
print('Beam design check-rectangular beam')
print('..............................................................................')
while True:
    try:
        print('Please enter material and section properties.')
        fc = float(input('concerete strength, fc (kN)= '))
        fy = float(input('Steel strength, fy(N/mm2)= '))
        b = float(input('Beam width, b(mm)= '))
        h = float(input('Beam total depth, h(mm)= '))
    except ValueError:
        print('Data input error! Try again ')
    else:
        Es = 200000
        ec = 0.003
        ey = fy/Es
        cc = 25
        ties = 10
        beta1 = beta1_value()
        df = rebar_suggestion()
        capacity = []
        classify_member = []
        steel_ratio = []
        for i in range(0, len(df.index)):
            dbar, n, number_of_layer = effective_depth()
            dprime = topbar_depth()
            fs, fsprime, es, a, c = stress_strain()
            phi, classify = strength_factor_classification()
            Mu, T, C, Cprime = forces_capacity()
            capacity.append(round(Mu)) 
            classify_member.append(steel_ratio_check())
            df['capacity, Mu(kNm)'] = capacity
            df['classification'] = classify_member
            df['stee; ratio'] = steel_ratio
            print('\n.............................................................')
            print('suggested reinforcement')
            print('................................................................')
            import time
            time.sleep(1)
            print(df)
            answer = input('would you like to provide reinforcement to check? (y/n) ')
            while answer.lower().startswith('y'):
                try:
                    dbar = int(input('Bottom rebar dia (mm)= '))
                    n = int(input('Bottom Rebar total qty(no.)= '))
                    dbarprime = int(input('Top Rebar dia (mm)= '))
                    nprime = int(input('Top Rebar total qty(no.)= '))
                except ValueError:
                    print('Data input error! Try again')
                if dbar < 10 or n < 2 or dbarprime < 10 or nprime < 2:
                    print('Data input error! minimum 2 no and minimum 10 mm dia')
                else:
                    As, Asprime = steel_areas()
                    deff, number_of_layer = effective_depth()
                    dprime = topbar_depth()
                    fs, fsprime, es, a, c, = stress_strain()
                    phi, classify = strength_factor_classification()
                    Mu, T, C, Cprime = forces_capacity()
                    print(f'\nBeam capacity : Mu= {round(Mu)}Kn-m, \nBeam is under{classify}, \n{steel_ratio_check()}')
                    print('\nHave a good day!\n')
                    exit()
            else:
                print('\nHave a good day!\n')
                exit()



                                                                                                                                                               
    
                           
                           