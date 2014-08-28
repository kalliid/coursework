import scitools.sound
from math import *
from numpy import *

def DWTHaarImpl(x,m):
    N = len(x)
    for mres in range(m,0,-1): 
        lenx=N/2**(m-mres)
        x[0:(lenx/2)], x[(lenx/2):lenx] = x[0:lenx:2] + x[1:lenx:2], x[0:lenx:2] - x[1:lenx:2]
        x[0:lenx]=x[0:lenx]/sqrt(2)
  
def IDWTHaarImpl(x,m):
    N = len(x)
    for mres in range(1,m+1): 
        lenx=N/2**(m-mres)
        x[0:lenx:2], x[1:lenx:2] = x[0:(lenx/2)]+x[(lenx/2):lenx], x[0:(lenx/2)]-x[(lenx/2):lenx]
        x[0:lenx]=x[0:lenx]/sqrt(2)

def DWTImpl(h0,h1,x,m):
    N = len(x)
    N1, N2 = len(h0), len(h1)
    topad1, topad2 = (N1-1)/2, (N2-1)/2
  
    Ncurr=N
    for mres in range(m):
        xnew=hstack((x[topad1:0:(-1)], x[0:Ncurr]))
        xnew=hstack((xnew,x[(Ncurr-2):(Ncurr-topad1-2):(-1)])) 
        x1=convolve(h0,xnew)
        x1=x1[(N1-1):(len(x1)-(N1-1))]
  
        xnew=hstack((x[topad2:0:(-1)], x[0:Ncurr]))
        xnew=hstack((xnew,x[(Ncurr-2):(Ncurr-topad2-2):(-1)]))
        x2=convolve(h1,xnew)
        x2=x2[(N2-1):(len(x2)-(N2-1))]

        # Reorganize the coefficients
        x[0:(Ncurr/2)], x[(Ncurr/2):Ncurr] = x1[0:Ncurr:2], x2[1:Ncurr:2]
        
        Ncurr=ceil(Ncurr/2)
  
def IDWTImpl(g0,g1,xnew,m):
    # function changecolumnrows begin
    # Keep track of the indices of the biggest even and odd index.
    g0=g0[len(g0)/2:len(g0)]
    g1=g1[len(g1)/2:len(g1)]
    maxeveng0, maxoddg0 = len(g0), len(g0)
    if mod(maxeveng0,2)==0:
        maxeveng0=maxeveng0-1
    else:
        maxoddg0=maxoddg0-1
  
    maxeveng1, maxoddg1 = len(g1), len(g1)
    if mod(maxeveng1,2)==0:
        maxeveng1=maxeveng1-1
    else:
        maxoddg1=maxoddg1-1
  
    a0length=max(maxeveng0,maxoddg1)
    a1length=max(maxeveng1,maxoddg0)
  
    a0=zeros(a0length)
    a0[0:maxeveng0:2]=g0[0:maxeveng0:2]
    a0[1:maxoddg1:2]=g1[1:maxoddg1:2]
  
    a1=zeros(a1length)
    a1[0:maxeveng1:2]=g1[0:maxeveng1:2]
    a1[1:maxoddg0:2]=g0[1:maxoddg0:2]
  
    a0=hstack(( a0[(len(a0)-1):0:(-1)], a0))
    a1=hstack(( a1[(len(a1)-1):0:(-1)], a1))
    # function changecolumnrows end
  
    N1, N2 = len(a0), len(a1)
    topad1, topad2 = (N1-1)/2, (N2-1)/2
  
    lenall=zeros(m+1)
    lenall[0]=len(xnew)
    for mres in range(1,m+1):
        lenall[mres]=ceil(lenall[mres-1]/2.0)
    # lenall is now the lengths of the (lowpass,highpass) sections of xnew
  
    for mres in range(m,0,-1):
        # Reorganize the coefficients first  
        intmid = hstack((xnew[0:lenall[mres]], xnew[lenall[mres]:lenall[mres-1]]))
        xnew[0:lenall[mres-1]:2] = intmid[0:lenall[mres]]
        xnew[1:lenall[mres-1]:2] = intmid[lenall[mres]:lenall[mres-1]]
        
        x=hstack(( xnew[topad1:0:(-1)], xnew[0:lenall[mres-1]] ))
        x=hstack(( x, xnew[(lenall[mres-1]-2):(lenall[mres-1]-topad1-2):(-1)] ))
        x1=convolve(a0,x)
        x1=x1[(N1-1):(len(x1)-(N1-1))]
  
        x=hstack(( xnew[topad2:0:(-1)], xnew[0:lenall[mres-1]] ))
        x=hstack(( x, xnew[(lenall[mres-1]-2):(lenall[mres-1]-topad2-2):(-1)] ))
        x2=convolve(a1,x)
        x2=x2[(N2-1):(len(x2)-(N2-1))]
    
        xnew[0:len(x1):2]=x1[0:len(x1):2]
        xnew[1:len(x2):2]=x2[1:len(x2):2]


def playDWTlower(m):
    x=scitools.sound.read('../castanets.wav')
    #x=array(x)
    x=x[0:2*2**17:2]
    DWTHaarImpl(x,m)
    lenx=len(x)
    x[(lenx/2**m):lenx]=zeros(lenx-lenx/2**m)
    IDWTHaarImpl(x,m)
    scitools.sound.write(x,'newsong.wav')
    scitools.sound.play('newsong.wav')

def playDWTlowerdifference(m):
    x=scitools.sound.read('../castanets.wav')
    x=x[0:2*2**17:2]
    DWTHaarImpl(x,m)
    lenx=len(x)
    x[0:(lenx/2**m)]=zeros(lenx/2**m)
    IDWTHaarImpl(x,m)
    scitools.sound.write(x,'newsong.wav')
    scitools.sound.play('newsong.wav')
  
def playDWTfilterslower(m,h0,h1,g0,g1):
    x=scitools.sound.read('../castanets.wav')
    x=x[0:2*2**17:2]
    DWTImpl(h0,h1,x,m)
    lenx=len(x)
    x[(lenx/2**m):lenx]=zeros(lenx-lenx/2**m)
    IDWTImpl(g0,g1,x,m)
    scitools.sound.write(x,'newsong.wav')
    scitools.sound.play('newsong.wav')
  
def playDWTfilterslowerdifference(m,h0,h1,g0,g1):
    x=scitools.sound.read('../castanets.wav')
    x=x[0:2*2**17:2]
    DWTImpl(h0,h1,x,m)
    lenx=len(x)
    x[0:(lenx/2**m)]=zeros(lenx/2**m)
    IDWTImpl(g0,g1,x,m)
    scitools.sound.write(x,'newsong.wav')
    scitools.sound.play('newsong.wav')
  
def playDWTall(m):  
    print('Haar wavelet')
    playDWTlower(m)
    print('Wavelet for piecewise linear functions')
    playDWTfilterslower(m,sqrt(2)*[1],sqrt(2)*[-1/2.0,1,-1/2.0],[1/2.0,1,1/2.0]/sqrt(2),[1]/sqrt(2))
    print('Wavelet for piecewise linear functions, alternative  version')
    playDWTfilterslower(m,sqrt(2)*[-1/8.0,1/4.0,3/4.0,1/4,-1/8],sqrt(2)*[-1/2.0,1,-1/2.0],[1/2.0,1,1/2.0]/sqrt(2),[-1/8.0,-1/4.0,3/4.0,-1/4.0,-1/8.0]/sqrt(2))
   
def playDWTalldifference(m):
    print('Haar wavelet')
    playDWTlowerdifference(m)
    print('Wavelet for piecewise linear functions')
    playDWTfilterslowerdifference(m,sqrt(2)*[1],sqrt(2)*[-1/2.0,1,-1/2.0],[1/2.0,1,1/2.0]/sqrt(2),[1]/sqrt(2))
    print('Wavelet for piecewise linear functions, alternative  version')
    playDWTfilterslowerdifference(m,sqrt(2)*[-1/8.0,1/4.0,3/4.0,1/4,-1/8],sqrt(2)*[-1/2.0,1,-1/2.0],[1/2.0,1,1/2.0]/sqrt(2),[-1/8.0,-1/4.0,3/4.0,-1/4.0,-1/8.0]/sqrt(2))



g0 = (1./16)*array([1,4,6,4,1])
g1 = (1./128)*array([5,20,1,-96,-70,280,-70,-96,1,20,5])
h0 = (1./128)*array([-5,20,-1,-96,70,280,70,-96,-1,20,-5])
h1 = (1./16)*array([1,-4,6,-4,1])

for m in range(8, 9):
    print "Haar wavelet, m=%i, compressed sound" % m
    playDWTlower(m)
    print "Our mother wavelet, m=%i, compressed sound" % m
    playDWTfilterslower(m,h0,h1,g0,g1)
    print "Haar wavelet, m=%i, detail information" % m
    playDWTlowerdifference(m)
    print "Our mother wavelet, m=%i, detail information" % m
    playDWTfilterslowerdifference(m,h0,h1,g0,g1)


# diverse testkode
#playDWTall(m)
#playDWTlower(4)
#playDWTfilterslower(4,sqrt(2)*[1],sqrt(2)*[-1/2.0,1,-1/2.0],[1/2.0,1,1/2.0]/sqrt(2),[1]/sqrt(2))
#playDWTfilterslower(4,sqrt(2)*[-1/8.0,1/4.0,3/4.0,1/4,-1/8],sqrt(2)*[-1/2.0,1,-1/2.0],[1/2.0,1,1/2.0]/sqrt(2),[-1/8.0,-1/4.0,3/4.0,-1/4.0,-1/8.0]/sqrt(2))
#playDWTlowerdifference(4)
#playDWTfilterslowerdifference(4,sqrt(2)*[1],sqrt(2)*[-1/2.0,1,-1/2.0],[1/2.0,1,1/2.0]/sqrt(2),[1]/sqrt(2))
#playDWTfilterslowerdifference(4,sqrt(2)*[-1/8.0,1/4.0,3/4.0,1/4,-1/8],sqrt(2)*[-1/2.0,1,-1/2.0],[1/2.0,1,1/2.0]/sqrt(2),[-1/8.0,-1/4.0,3/4.0,-1/4.0,-1/8.0]/sqrt(2))
#x=array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).astype(float)
#DWTImpl([sqrt(2)],[-sqrt(2)/2,sqrt(2),-sqrt(2)/2],x,3)
#print x
#IDWTImpl([1/(2*sqrt(2)),1/sqrt(2),1/(2*sqrt(2))],[1/sqrt(2)],x,3)
#print x # should recover the original x
#x=array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).astype(float)
#DWTHaarImpl(x,3)
#print x
#IDWTHaarImpl(x,3) 
#print x # should recover the original x