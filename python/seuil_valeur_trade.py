
from datetime import datetime
date = [datetime.datetime(2022, 7, 3, 22, 33),datetime.datetime(2022, 7, 3, 11, 22, 38),datetime.datetime(2022, 7, 3, 11, 22, 49)]
Token = ['GAga35-8','ASqf15-2','WGaf54-5']
entry = [round(random.randint(1, 1000) * random.random(), 2),round(random.randint(1, 1000) * random.random(), 2),round(random.randint(1, 1000) * random.random(), 2)]
for i in range(len(win)):
    if win[i]==0:
        win[i]="🟥🟥🟥"
    elif win[i]==1:
         win[i]="🟩🟥🟥"
    elif win[i]==2:
         win[i]="🟩🟩🟥"
    elif win[i]==3:
         win[i]="🟩🟩🟩"
TP1 = []
TP2 = []
TP3 = []
SL = []
code = ['','','']
for i in range(len(entry)):
    TP1.append(round(entry[i]*1.2,2))
    TP2.append(round(TP1[i]*1.2,2))
    TP3.append(round(TP2[i]*1.2,2))
    SL.append(round(TP1[i]*0.8,2))
    ti=Token[i]
    tr=trade[i]
    en=entry[i]
    code[i]=[Levier,tr,ti,en]
type = [random.randint(0, 1),random.randint(0, 1),random.randint(0, 1)]
for i in range(len(type)):
    if type[i]==0 :
        type[i] = "SHORT 📉"
    else :
        type[i] = "LONG 📈"
for i in range(len(trade)):
    print('************************************')
    print(trade_url[i])
    print(trade[i],"     ",type[i],"    ENTRY :")
    print(date[i],"         ",entry[i])
    print()
    print("Take Profit / Stop Loss")
    print("TP1:         TP2:")
    print(TP1[i],"     ",TP2[i])
    print("TP3:         SL:")
    print(TP3[i],"     ",SL[i])
    print()
    print("Complement :          ",win[i])
    print(Levier,"  ",Token[i])
    print(code[i])
    print("⚠️Trade with caution. You should never trade more than 10%-15% of your bag at a time. ")
    print("We are not financial advisors so trade at your own risks.")
