def lane_number(CW_width):
    if 13.1<CW_width<16.6:
        return 4
    elif 9.6<CW_width<13.1:
        return 3
    elif 5.3<CW_width<9.6:
        return 2
    elif 4.25<CW_width<5.3:
        return 1
    else:
        return 0

def ll_combinations(lane_no):
    # return combination based on lane_no
    pcomb = []
    comb = []
    for i in range((lane_no)+1):
        k=2
        while k>=1:
            ele=[0,0,0]
            ele[0]=i
            ele[k]=(lane_no-i)/2
            if ele[k].is_integer():
                pcomb.append(ele)
                k-=1
            else:
                break
    for elem in pcomb:
        if elem not in comb:
            comb.append(elem)
    return comb
while True:
    cw_width = float(input("Enter the Carriageway width: "))
    if cw_width>=4.25:
        break
print("No of lanes = ", lane_number(cw_width))
print("Live load sombinations in the form (Class A, 70R(RW), 70(RT))")
if len(ll_combinations(lane_number(cw_width))) == 1: 
    print(ll_combinations(lane_number(cw_width))," and a 500kg/m^3 UDL on remaining length.")
else:
    print(ll_combinations(lane_number(cw_width)))