# -*- coding: utf-8 -*-
"""train.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15HA7XAeipd519Kx5tOnI-0emSEGXc2Mz
"""

from PIL import Image
import os,glob
import numpy as np
from sklearn.model_selection import train_test_split

def training():
  classify_dir="./datasets/train"
  categories=["bear","bird","butterfly","car","cat","deer","dog","horse","sheep","tiger"]
  nb_classes=len(categories)

  image_w=64
  image_h=64
  pixels=image_w*image_h*3

  X=[]
  Y=[]
  for idx,cate in enumerate(categories):
    label=[0 for i in range(nb_classes)]
    label[idx]=1

    image_dir=classify_dir+"/"+cate
    files=glob.glob(image_dir+"/*.jpg")

    for i,f in enumerate(files):
      img=Image.open(f)
      img=img.convert("RGB")

      img=img.resize((image_w,image_h))
      data=np.asarray(img)#numpy 배열로 변환
      X.append(data)
      Y.append(label)

      if i%10==0:
        print(i,"\n",data)
  X=np.array(X)
  Y=np.array(Y)
  #학습 전용 데이터와 테스트 전용 데이터 구분
  X_train, X_test, y_train, y_test=\
      train_test_split(X,Y)
  xy=(X_train, X_test, y_train, y_test)


  np.save("./datasets.npy",xy)
  print("ok",len(Y))