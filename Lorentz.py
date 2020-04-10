# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:19:55 2020

@author: snice
"""
RGB=[(255,0,0),(255,99,71),(255,127,80),(205,92,92),(240,128,128),
     (233,150,122),(250,128,114),(255,160,122),(255,69,0),
     (255,140,0),(255,165,0),(255,215,0),(184,134,11),
     (218,165,32),(238,232,170),(189,183,107),(240,230,140),
     (128,128,0),(255,255,0),(154,205,50),(85,107,47),
     (107,142,35),(124,252,0),(127,255,0),(173,255,47),
     (0,100,0),(0,128,0),(34,139,34),(0,255,0),(50,205,50),
     (144,238,144),(152,251,152),(143,188,143),(0,250,154),
     (0,255,127),(46,139,87),(102,205,170),(60,179,113),
     (32,178,170),(47,79,79),(0,128,128),(0,139,139),
     (0,255,255),(0,255,255),(224,255,255),(0,206,209),
     (64,224,208),(72,209,204),(175,238,238),(127,255,212),
     (176,224,230),(95,158,160),(70,130,180),(100,149,237),
     (0,191,255),(30,144,255),(173,216,230),(135,206,235),
     (135,206,250),(25,25,112),(0,0,128),(0,0,139),
     (0,0,205),(0,0,255),(65,105,225),(138,43,226),
     (75,0,130),(72,61,139),(106,90,205),(123,104,238),
     (147,112,219),(139,0,139),(148,0,211),(153,50,204),
     (186,85,211),(128,0,128),(216,191,216),(221,160,221),
     (238,130,238),(255,0,255),(218,112,214),(199,21,133),
     (219,112,147),(255,20,147)] 


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio
import os
import shutil
from math import floor, log
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')


def nextpos(x,y,z,a,b,c,dt):
    x+=a*(y-x)*dt
    y+=(b*x-y-x*z)*dt
    z+=(x*y-c*z)*dt
    return(x,y,z)
    
def setfig():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor") 
    return (ax)

def makeGif():
    filenames = sorted(fn for fn in os.listdir(r'C:\Users\snice\OneDrive\Bureau\Computer Stuff\Python Projects\Lorentz') if fn.endswith('.png'))
    images = []
    #print(filenames)
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(r'C:\Users\snice\OneDrive\Bureau\Computer Stuff\Python Projects\Lorentz\Gif.gif', images, duration=0.1)
    #shutil.rmtree(r'C:\Users\snice\OneDrive\Bureau\Computer Stuff\Python Projects\Lorentz\Images')
    
def drawfig(n,b,x0,y0,z0,dt,tot):
    """On prend b>24,3 et deltaT en secondes"""
    ax=setfig()
    X=[x0]
    Y=[y0]
    Z=[z0]
    a=10
    c=8/3
    k=0
    while k<n:
        #ax.scatter(X[-1],Y[-1],Z[-1])
        #plt.pause(0.1)
        (x,y,z)=nextpos(X[-1],Y[-1],Z[-1],a,b,c,dt)
        X.append(x)
        Y.append(y)
        Z.append(z)
        k+=1
    #print(X,Y,Z)
    #deltaZ=max(Z)-min(Z)
    #ls=len(RGB)
    ax.plot(X,Y,Z,c='red')
    p=floor(log(tot,10))
    q=floor(log(n,10))
    zero='0'*(p-q)
    print(p,q)
    plt.savefig(r'C:\Users\snice\OneDrive\Bureau\Computer Stuff\Python Projects\Lorentz\Frame_'+str(zero)+(str(n))+'_'+str(tot)+'_.png',dpi=300)
    plt.show()
    
def animation(tot,b,x0,y0,z0,dt):
    #os.mkdir(r'C:\Users\snice\OneDrive\Bureau\Computer Stuff\Python Projects\Lorentz\Images')
    for n in range(1,tot+1):
        print(n)
        drawfig(n,b,x0,y0,z0,dt,tot)
    print("All images have been made")
    print("Generating Gif")    
    makeGif()
    print("Done")
        
        
    
    

    