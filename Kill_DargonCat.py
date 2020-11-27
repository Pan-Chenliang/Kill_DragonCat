import os
import sys
import time
import math

#路线五 31.94105,118.78200
'''
路线五坐标点阵
31.94060,118.78171 西南角
31.94075,118.78251 东南角
31.94156,118.78228 东北角
31.94143,118.78147 西北角
'''

imei_num="000000000000000"#拨号盘输入*#06#
route_5=[31.94085,118.78249]#越小越向左下
route_5SW=[31.94064,118.78170]
route_5SE=[31.94085,118.78249]
route_5NE=[31.94151,118.78228]
route_5NW=[31.94130,118.78151]

def set_imei(imei):
    imei_str="adb shell setprop persist.nox.modem.imei "+imei
    os.system(imei_str)

def set_position(posi):
    latitude="adb shell setprop persist.nox.gps.latitude "+str(posi[0])
    longitude="adb shell setprop persist.nox.gps.longitude "+str(posi[1])
    os.system(latitude)
    os.system(longitude)

def line(posi1,posi2):
    result=[]
    delta=[(posi2[0]-posi1[0])/10,(posi2[1]-posi1[1])/10]
    for i in range(10):
        result.append([posi1[0]+i*delta[0],posi1[1]+i*delta[1]])
    return result

def circle(posi1,posi2,is_clockwise=False):
    result=[]
    center=[(posi1[0]+posi2[0])/2,(posi1[1]+posi2[1])/2]
    radius=math.sqrt((posi1[0]-posi2[0])**2+(posi1[1]-posi2[1])**2)/2
    angle_0=math.atan2(posi1[1]-center[1],posi1[0]-center[0])
    for i in range(15):
        if is_clockwise:
            angle=angle_0+math.pi*i/15
            result.append([center[0]+radius*math.cos(angle),center[1]+radius*math.sin(angle)])
        else:
            angle=angle_0-math.pi*i/15
            result.append([center[0]+radius*math.cos(angle),center[1]+radius*math.sin(angle)])
    return result

def main():
    #set_imei(imei_num)
    #set_position(route_5)
    a=circle(route_5NE,route_5NW,False)
    b=line(route_5NW,route_5SW)
    c=circle(route_5SW,route_5SE,False)
    d=line(route_5SE,route_5NE)
    for j in range(6):
        for i in range(15):
            set_position(a[i])
            time.sleep(2.5)
        for i in range(10):
            set_position(b[i])
            time.sleep(2.5)
        for i in range(15):
            set_position(c[i])
            time.sleep(2.5)
        for i in range(10):
            set_position(d[i])
            time.sleep(2.5)

if __name__=="__main__":
    main()