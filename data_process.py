"""
MADE BY RDUAN, FOR RESEARCH ONLY

This programe is for displace all the 

WARNING:
1. THIS PROGRAME CAN BE USED IN GET HORTZONTAL PROJECTILE MOTION ONLY
2. PLEASE PLACE YOUR ORIGINAL DATA FILE ON ./csv_data FOLDER
3. THE OUTPUT DATA WILL BE PLACED IN ./csv_displacement
"""

import csv
import os

# VARIABLE DEFINE AREA

csv_dir='./csv_data' # ORIGINAL CSV DATA PATH
output_csv_dir='./csv_displacement' # OUTPUT CSV DATA PATH
ratio_csv_dir='./csv_data/ratio.csv' # ratio_csv_data
object_height=60 #object height #物件高度(cm)
ratio_switch=True
# 設定True會轉換為公分，False不會



def read_csv_to_array(file_path):
    data_array = []

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            try:
                row_int = [int(element) for element in row]
                data_array.append(row_int)
            except ValueError:
                continue

    return data_array

def write_array_to_csv(data_array, file_path):
    file_path = os.path.join(output_csv_dir, file_path)
    title = [['frame', 'x', 'y']] + [row for row in data_array]
    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(title)


ratio_data=read_csv_to_array(ratio_csv_dir)
r_b = ratio_data[0][2] #bottom
r_h= ratio_data[1][2] #height
ratio=(abs(r_h-r_b)/object_height)


csv_datas=[] # DO NOT CHANGE THIS VARIABLE
print(csv_datas)
for root,dir,files in os.walk(csv_dir):
    for file in files:
        print(type(file))
        if os.path.basename(file) == "ratio.csv":
            continue
        else:
            csv_datas.append(os.path.join(root,file))
print(csv_datas)

for csv_name in csv_datas:
    data = read_csv_to_array(csv_name)
    try:
        x_f = data[0][1]
        y_f = data[0][2]
        print("FILE {} BEFORE DISPLACEMENT".format(csv_name))
        print(data)
        
        for i in range(len(data)):
            data[i][1] -= x_f
            data[i][2] -= y_f
            if ratio_switch==True:
                data[i][1] /= ratio
                data[i][2] /= ratio
        
        print("FILE {} AFTER DISPLACEMENT".format(csv_name))
        # 使用 os.path.basename() 取得檔案名稱
        filename = os.path.basename(csv_name)

        # 使用 os.path.splitext() 分割檔案名稱和副檔名
        write_array_to_csv(data,filename)

    
    except IndexError:
        print("FILE {} Index out of range error occurred.".format(csv_name))
