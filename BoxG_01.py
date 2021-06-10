
Veh1=[[27,0.0],[27,1.10],[114,4.30],[114,5.50],
      [68,9.8],[68,12.8],[68,15.8],[68,18.8]]
    # Vehicle data of ClassA in List Type
Veh2=[[80,0],[120,3.96],[120,5.48],[170,7.61],
      [170,8.98],[170,12.03],[170,13.4],[0,13.4]]

Veh3=[[50,0],[100,0.653],[100,1.306],[100,1.959],
      [100,2.611],[100,3.264],[100,3.917],[50,4.57]]

Veh=[Veh1, Veh2,Veh3]#[0,1,2]

span=50

def FindBM(BL, Uat, BMat):
    if Uat<=0 or Uat>=BL:
        BM=0
    elif Uat>0 and Uat<=BMat:
        BM=Uat/BL*(BL-BMat)
    else :
        BM=(BL-Uat)/BL*BMat
    return BM


def FindSF (BL, Uat, BMat):
    if Uat<0 or Uat>BL:
        SF=0
    elif Uat>=0 and Uat<=BMat:
        SF=-Uat/BL
    elif Uat<=BL:
        SF=(BL-Uat)/BL
    return SF


def MoveVeh():
    for v in range(len(Veh)):
        lp=0
        bmx=0
        while lp+Veh[v][7][1]<span:
            tbm=0
            for w in range( len(Veh[v])):
                load=Veh[v][w][0]
                location=lp-Veh[v][w][1]
                tbm=tbm+FindBM(span,location,span/2)*load   
            if tbm>bmx:
                bmx=tbm
            lp=lp+0.1
        print(bmx)

MoveVeh()
        




        
    






