'''
Esteban Camarillo
ID#:1636095
'''

import pandas as pd


pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

#Asking for user to input file name
manufac_list=input("Manufacturer list CSV file name")
manufac_heading=['id', 'man', 'type', 'stat']
manufac_df=pd.read_csv(manufac_list + '.csv', header=None, skiprows=0, names=manufac_heading)



#Asking for user to input file name
service_date_list=input("Service Dates List CSV file name")
service_heading=['id', 'date']
service_df=pd.read_csv(service_date_list + '.csv', header=None, skiprows=0, names=service_heading)


#Asking for user to input file name
price_list=input("Price List CSV file name")
price_heading=['id', 'price']
price_df=pd.read_csv(price_list + '.csv', header=None, skiprows=0, names=price_heading)
total= manufac_df, service_df, price_df



#Merging files by their id's
fullinvent=df= pd.merge(pd.merge(manufac_df, service_df, on='id', how='left'), price_df, on='id', how='left')
fullinvent_a=fullinvent[['id', 'man', 'type', 'price', 'date', 'stat']]
fullinvent_b = fullinvent_a.sort_values('man')


#Merging files by their id's
fullinvent_b.to_csv('Fullinventoy.csv', header=False, index=False)
damage_a=fullinvent_b.query("stat == 'damaged'")
damage_b= damage_a.drop('stat', 1)

damage_b.to_csv('DamagedInventory.csv', header=False, index=False)


# import date filter date for past due, drop columns and export csv
import datetime
today=datetime.date.today()
ft=datetime.date.strftime(today,"%m/%d/%Y")
fullinvent_b['date'] =pd.to_datetime(fullinvent_b['date'], format='%m/%d/%Y')
k=fullinvent_b[fullinvent_b['date'].between('1700-01-01', '2020-11-09')]
kt=k.sort_values('date')

kt.to_csv('PastServiceDateInventory.csv',header=False, index=False)



filter_laptop=fullinvent_b.query("type == 'laptop'")
sort_laptop=filter_laptop.sort_values('id')
drop_laptop= sort_laptop.drop('type',1)

drop_laptop.to_csv('LaptopInventory.csv',header=False, index=False)

filter_phone=fullinvent_b.query("type == 'phone'")
sort_phone=filter_phone.sort_values('id')
drop_phone= sort_phone.drop('type',1)

drop_phone.to_csv('PhoneInventory.csv',header=False, index=False)

filter_tower=fullinvent_b.query("type == 'tower'")
sort_tower=filter_tower.sort_values('id')
drop_tower= sort_tower.drop('type',1)

drop_tower.to_csv('TowerInventory.csv',header=False, index=False)



q=fullinvent_b[fullinvent_b['date'] > '2020-11-09']
q_drop= q.drop('date',1)
filter_q=q_drop[q_drop['stat'].isnull()]
drop_filter_q=filter_q.drop('stat',1)

dic=drop_filter_q.to_dict('list')

dic
while True:
    query = input("Type a query or q to quit: ")
    if(query == "q"):
        break
    item = ""
    pos = ""
    for r in dic["man"]:
        if r in query:
            item = r
    for r in dic["type"]:
        if r in query:
            pos = r
    if(item == "" or pos == ""):
        print("No such item in invetory")
    else:
        h = ["", "", "", 0]
        for r in range(len(dic["id"])):
            if(dic["man"][r] == item and dic["type"][r] == pos):
                if(h[3] < dic["price"][r]):
                    h[0] = dic["id"][r]
                    h[1] = dic["man"][r]
                    h[2] = dic["type"][r]
                    h[3] = dic["price"][r]
    print("Your item is " + str(h[0]) + " " + str(h[1]) + " " + str(h[2]) + " " + str(h[3]))
    extra = []
    for i in range(len(dic["id"])):
        if(dic["type"][r] == pos and dic["man"][r] != item):
            extra.append([dic["id"][r], dic["man"][r], dic["type"][r], dic["price"][r]])
        if(len(extra) != 0):
            print("You may also like ")
            for r in range(len(extra)):
                print(str(extra[r][0]) + " " + extra[r][1] + " " + extra[r][2] + " " + str(extra[r][3]))
