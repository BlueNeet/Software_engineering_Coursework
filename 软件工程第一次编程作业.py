def chtoint(y):
    global temp
    if y=='零':
        return 0
    elif y=='一':
        return 1
    elif y=='二':
        return 2
    elif y=='三':
        return 3
    elif y=='四':
        return 4
    elif y=='五':
        return 5
    elif y=='六':
        return 6
    elif y=='七':
        return 7
    elif y=='八':
        return 8
    elif y=='九':
        return 9
    elif y=='十':
        return 10
    else:
        print("数字有问题")
        return "errorx"

def inttoch(z):
    if z==1:
         return '一'
    elif z==2:
        return '二'
    elif z==3:
        return '三'
    elif z==4:
        return '四'
    elif z==5:
        return '五'
    elif z==6:
        return '六'
    elif z==7:
        return '七'
    elif z==8:
        return '八'
    elif z==9:
        return '九'
    elif z==10:
        return '十'
    else:
        print("数字有问题")
def printo(charr):
    try:
        print(inttoch(strings[charr[1]]))
    except KeyError:
        if charr[1][0]=="“":
            tekst=charr[1]
            tekst=tekst.strip('“')
            tekst=tekst.strip('”')
            print(tekst)
        else:
            print("未初始化该量")
    except IndexError:
        print("无此命令!!!")

def firstrslt(ze):
    if ze[1]=="看看":
        ze[0]=ze[1]
        ze[1]=ze[2]
        printo(ze)
    elif ze[1]=="无":
        return 0
    elif ze[2]=="增加":
        change=chtoint(ze[3])
        if change!="errorx":
            strings[ze[1]]=strings[ze[1]]+change
    elif ze[2]=="减少":
        change=chtoint(ze[3])
        if change!="errorx":
            strings[ze[1]]=strings[ze[1]]-change
    elif ze[2]=="乘以" or ze[2]=="除以":
        change=chtoint(ze[3])
        if ze[2]=="乘以":
            if change!="errorx":
                strings[ze[1]]=strings[ze[1]]*change
        else:
            if change==0:
                print("分母不可为零")
            else:
                if change!="errorx":
                    strings[ze[1]]=strings[ze[1]]/change
    else:
        print("则里的动作错误")

def secrslt(fouze):
    if fouze[1]=="看看":
        fouze[0]=fouze[1]
        fouze[1]=fouze[2]
        printo(fouze)
    elif fouze[1]=="无":
        return 
    elif fouze[2]=="增加":
        change=chtoint(fouze[3])
        if change!="errorx":
            strings[fouze[1]]=strings[fouze[1]]+change
    elif fouze[2]=="减少":
        change=chtoint(fouze[3])
        if change!="errorx":
            strings[fouze[1]]=strings[fouze[1]]-change
    elif fouze[2]=="乘以" or fouze[2]=="除以":
        change=chtoint(fouze[3])
        if fouze[2]=="乘以":
            if change!="errorx":
                strings[fouze[1]]=strings[fouze[1]]*change
        else:
            if change==0:
                print("分母不可为零")
            else:
                if change!="errorx":
                    strings[fouze[1]]=strings[fouze[1]]/change
    else:
        print("否则里的动作错误")

def ChParser():
    text=input()
    result = ' '.join(text.split())
    charr=result.split(" ")
    if text=="":
        return
    elif len(charr)<3 and charr[0]!="看看":
        print("无此命令!!!")
    elif charr[0]=="整数" and charr[2]=="等于":
        strings[charr[1] ]=chtoint(charr[3])
    elif charr[0]=="看看":
        printo(charr)
    elif charr[1]=="增加" or charr[1]=="减少":
        change=chtoint(charr[2])
        if charr[1]=="增加" and change!="errorx":   
            strings[charr[0]]=strings[charr[0]]+change
        elif charr[1]=="减少" and change!="errorx":
            strings[charr[0]]=strings[charr[0]]-change

    elif charr[1]=="乘以" or charr[1]=="除以":
        change=chtoint(charr[2])
        if charr[1]=="乘以":
            strings[charr[0]]=strings[charr[0]]*change
        else:
            if change==0:
                print("分母不可为零")
            else:
                strings[charr[0]]=strings[charr[0]]/change

    elif charr[0]=="如果" and charr[2]=="大于":
        kuchi=text.split("则",1)
        sentence=kuchi[1].split("否则")
        ze=sentence[0].split(" ")
        fouze=sentence[1].split(" ")
        if strings[charr[1]]>chtoint(charr[3]):
            firstrslt(ze)
        else:
            secrslt(fouze)        
            
    elif charr[0]=="如果" and charr[2]=="小于":
        kuchi=text.split("则",1)
        sentence=kuchi[1].split("否则")
        ze=sentence[0].split(" ")
        fouze=sentence[1].split(" ")    
        if strings[charr[1]]<chtoint(charr[3]):
            firstrslt(ze)
        else:
            secrslt(fouze)

    elif charr[0]=="如果" and charr[2]=="等于":
        kuchi=text.split("则",1)
        sentence=kuchi[1].split("否则")
        ze=sentence[0].split(" ")
        fouze=sentence[1].split(" ")
        if strings[charr[1]]==chtoint(charr[3]):
            firstrslt(ze)
        else:
            secrslt(fouze)

    elif charr[0]=="如果" and charr[2]=="不等于":
        kuchi=text.split("则",1)
        sentence=kuchi[1].split("否则")
        ze=sentence[0].split(" ")
        fouze=sentence[1].split(" ")
        if strings[charr[1]]!=chtoint(charr[3]):
            firstrslt(ze)
        else:
            secrslt(fouze)
    else:
        print("无此命令!!!")

   
        
if __name__=="__main__":
    strings={}
    while True:
        ChParser()
