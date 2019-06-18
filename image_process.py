import cv2 as cv
import numpy as np
import os

def line_image(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #cv.imshow("gray",gray)
    edges = cv.Canny(gray, 100, 500, apertureSize=3)
    #cv.imshow("canny",edges)

    # contours,hierarchy=cv.findContours(edges,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
    # point_size=1
    # point_color=(0,0,255)
    # thickness=4
    # print("contours",np.array(contours).shape)
    # for i in range(np.array(contours).shape[0]):
    #     cv.circle(image,(contours[i][0][0][0],contours[i][0][0][1]),point_size,point_color,thickness)
    # cv.imshow("result",image)


    #cv.imshow("lunkuo",contours)
    #r,g,b=cv.split(image)
    # cv.connectedComponents(r)
    # cv.imshow("conn",cv.merge([r,r,r]))
    #print("dian:",hierarchy)
    #print("dian shape:",hierarchy.shape)
    lines = cv.HoughLines(edges, 1, np.pi / 2, 190)
    #print("lines:",lines.shape)
    #print(lines)
    col=[]
    row=[]
    #print(col)
    #print("----")
    for line in lines:
        rho, theta = line[0]
        if(theta<1):
            col.append(rho)
        else:
            row.append(rho)
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 2000 * (-b))
        y1 = int(y0 + 2000 * (a))
        x2 = int(x0 - 2000 * (-b))
        y2 = int(y0 - 2000 * (a))
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    #cv.imshow("hough", image)
    return col,row

def judge(image,p1,p2,p3,p4):
    count=0.0
    r,g,b=cv.split(image)
    #print(r.shape)#(1080,550)

    total=float((abs(p4[0]-p1[0]))*(abs(p4[1]-p1[1])))
    for i in range(int(abs(p4[0]-p1[0]))):
        for j in range(int(abs(p4[1]-p1[1]))):
            x=int(i+p1[0])
            y=int(j+p1[1])
            if(x>=r.shape[1]):
                x=r.shape[1]-1

            if(y>=r.shape[0]):
                y=r.shape[0]-1
            if(r[y][x]!=255):
                count=count+1
    if(count/total>0.8):
        #print("find one")
        return 1
    else:return 0


def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

def img_process(input):
    src = cv.imread(input)
    _x=src.shape[1]
    _y=src.shape[0]
    b,g,r=cv.split(src)
    for i in range(b.shape[0]):
        for j in range(b.shape[1]):
            if(b[i][j]!=255):
                b[i][j]=0
    src_merged=cv.merge([b,b,b])#src:原图,src_merged:二值化的图,需要对两张图都进行直线检测，结合两次直线检测结果。
    #cv.imshow("merged",src_merged)

    #line_image(src)#对原图进行直线检测
    col,row=line_image(src_merged)#对二值化图进行直线检测
    col.sort()
    row.sort()
    if(col[0]>0):
        col.append(0)
        col.sort()
    if(col[len(col)-1]<_x):
        col.append(_x)

    if(row[0]>0):
        row.append(0)
        row.sort()
    if(row[len(row)-1]<_y):
        row.append(_y)
    #print(row)
    #print(col)
    result=[]
    for i in range(len(col)-2):
        for j in range(len(row)-2):
            p1=[col[i],row[j]]
            p2=[col[i+1],row[j]]
            p3=[col[i],row[j+1]]
            p4=[col[i+1],row[j+1]]
            if(judge(src_merged,p1,p2,p3,p4)==1):
                result.append([p1,p2,p3,p4])
    #print("result",np.array(result).shape)
    #print(result)
    # for i in range(len(result)):
    #     print(tuple(result[i]))
    #     cv.rectangle(src_merged,tuple(result[i][0]),tuple(result[i][3]),(0,255,0),2)
    # cv.imshow("rec",src_merged)
    while(1):#判断区域之间是能够结合，若能结合则结合
        do_sth=0
        for i in range(len(result)):
            for j in range(len(result)-i-1):
                if((result[i][1]==result[j][0]) & (result[i][3]==result[j][2])):
                    result.append([result[i][0],result[j][1],result[i][2],result[j][3]])
                    result.remove(result[i])
                    result.remove(result[j-1])
                    do_sth=1
                    break
            if(do_sth==1):
                break
        if(do_sth==0):
            break
    #print(result)
    # for i in range(len(result)):
    #     print(tuple(result[i]))
    #     cv.rectangle(src_merged,tuple(result[i][0]),tuple(result[i][3]),(0,255,0),2)
    # cv.imshow("rec",src_merged)
    for i in range(len(result)):
        new_img=src[int(result[i][0][1]):int(result[i][2][1]),int(result[i][0][0]):int(result[i][1][0])]
        #cv.imshow("new%d"%(i),new_img)
        path=input.split(".")
        #mkdir("%s"%(path[0]))
        #os.chdir("%s"%(path[0]))

        filename="%snew%d.jpg"%(path[0],i)
        print(filename)
        cv.imwrite(filename,new_img)





os.chdir("image_example/1/")
print("out path:",os.getcwd())
files=os.listdir()
for file in files:
    img_process(file)
cv.waitKey(0)
cv.destroyAllWindows()
