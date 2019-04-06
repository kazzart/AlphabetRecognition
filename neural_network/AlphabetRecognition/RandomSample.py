import random as r
import os
from PIL import Image
class Rand:
    #инициализация, quantity - количество примеров
    def __init__(self,quantity, folder = "learn"):
        dirName = os.path.join(os.path.realpath(r"..\..\ "),"samples",folder)
        names = os.listdir(dirName)
        self.objects = []
        self.used = []
        for name in names:
            fullname = os.path.join(dirName, name)
            if not os.path.isfile(fullname):
                self.objects.append(name)

        r.seed(version =2)
        self.Path = folder
        for i in range(len(self.objects)):
            li = []
            for i in range(quantity):
                li.append(i+1)
            self.used.append(li)
    #проверка, не осталось ли неиспользованных примеров
    def getObjs(self):
        return self.objects
    def notEmpty(self):
        for line in self.used:
            if len(line) > 0:
                return True
        return False
    
    #выдаёт следующее рандомное изображение
    def next(self):
        li = self.used
        #print(len(self.used))
        a = r.randint(0,len(li)-1)
        while len(li[a]) == 0:
            a = r.randint(0,len(li)-1)
        li2 = li[a]
        im = Image.open( os.path.join(os.path.realpath(r"..\..\ "),"samples",self.Path,str(self.objects[a]),"{}_{}{}.jpg".format(self.Path,self.objects[a], li2[0]) ) )
        li2.remove(li2[0])
        return im,a

def take_a_pic(im, rnd,n_ans):
    import numpy as np
    img_temp = np.asarray(im)
    size = img_temp.shape[0]*img_temp.shape[1]
    img = np.zeros((size))
    #print (img_temp, rnd)
    count = 0
    for i in img_temp:
        for j in i:
            img[count] = j
            count += 1

    answer = np.zeros((n_ans))
    answer[rnd] = 1
    return img, answer
def imgToArray(path):
    import numpy as np
    im = Image.open(path)
    img_temp = np.asarray(im)
    size = img_temp.shape[0]*img_temp.shape[1]
    img = np.zeros((size))
    count = 0
    for i in img_temp:
        for j in i:
            img[count] = j
            count += 1
    X_train = np.array([img]).T
    return X_train/255
'''
s = Rand(10,"learn")
while(s.notEmpty()):
    image,num = s.next()
    image.show()
'''
