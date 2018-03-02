exec(open('preambel.py').read())
import cv2

im1 = misc.imread('image1.png')
im2 = misc.imread('image2.png')
im1r = im1[:,:,0]
im1g = im1[:,:,1]
im1b = im1[:,:,2]
#plt.figure(1), plt.imshow(im1)
#plt.figure(2), plt.imshow(im1g,'gray')
#plt.figure(3), plt.imshow(im1b,'gray')
#plt.show()

### FRAGA 1
#SVAR
# Gul: lika blandning rött och grönt
# Cyan: lika blått ocht grönt
# Magenta: lika blått och rött
# White: lika max rgb
# SVart: 0 rgb

y, cb, cr = jl.rgb2ycbcr(im1)

#lt.figure(2), plt.imshow(y, 'gray', clim=(0, 255))
#plt.figure(3), plt.imshow(cb, 'gray')
#plt.figure(4), plt.imshow(cr, 'gray')
#plt.show()

### FRAGA 2
#SVAR
# I luminens, figur 2 (y-kanal)

# Mean square error
def meanSquareError(imga, imgb):
    return np.square(np.subtract(imga, imgb)).mean()

# Peak signal to noise ratio
def psnr(mse):
    return 10*np.log10(255**2/mse)

def bppReduction(img, bits_to_reduce):
    X = 2**bits_to_reduce
    return X*np.floor_divide(img,X)

### FRAGA 3
#SVAR
# 2**3 = 8

### FRAGA 4

def imgAssessmentBppred(img):
    # good: psnr=39dB
    goodImg = bppReduction(img, 2)
    print("psnr good: " + str(psnr(meanSquareError(goodImg, img))))
    print("bpp good: " + str(int(np.ceil(np.log2(np.max(goodImg)-np.min(goodImg))))))
    # half-good: psnr=35dB
    halfgoodImg = bppReduction(img, 7)
    print(np.max(halfgoodImg))
    print(np.min(halfgoodImg))
    print("psnr half-good: " + str(psnr(meanSquareError(halfgoodImg, img))))
    print("bpp half-good: " + str(int(np.ceil(np.log2(np.max(halfgoodImg)-np.min(halfgoodImg))))))
    plt.figure(1)
    plt.subplot(131), plt.imshow(img)
    plt.subplot(132), plt.imshow(goodImg)
    plt.subplot(133), plt.imshow(halfgoodImg)
    plt.show()
#imgAssessmentBppred(im2)

### FRAGA 5

def imgAssessmentImresize(img):
    # good: psnr=39dB
    gooddown = np.floor(misc.imresize(img, 3/4, interp='bicubic', mode='F'))
    goodImg = misc.imresize(gooddown, 4/3, interp='bicubic', mode='F')
    print("psnr good: " + str(psnr(meanSquareError(goodImg, img))))
    print("bpp good: " + str(int(np.ceil(np.log2(np.max(goodImg)-np.min(goodImg))))))
    # half-good: psnr=35dB
    halfgooddown = np.floor(misc.imresize(img, 1/2, interp='bicubic', mode='F'))
    halfgoodImg = misc.imresize(halfgooddown, 2., interp='bicubic', mode='F')
    print("psnr half-good: " + str(psnr(meanSquareError(halfgoodImg, img))))
    print("bpp half-good: " + str(int(np.ceil(np.log2(np.max(halfgoodImg)-np.min(halfgoodImg))))))
    plt.figure(1)
    plt.subplot(131), plt.imshow(img, 'gray')
    plt.subplot(132), plt.imshow(goodImg, 'gray')
    plt.subplot(133), plt.imshow(halfgoodImg, 'gray')
    plt.show()
#imgAssessmentImresize(y)

### FRAGA 6
"""
y3 = np.floor(misc.imresize(y, 0.5, interp='bicubic', mode='F'))
y4 = misc.imresize(y3, 2., interp='bicubic', mode='F')
plt.figure(4), plt.imshow(y, 'gray')
plt.figure(5), plt.imshow(y4, 'gray')
plt.figure(6), plt.imshow(np.abs(y-y4), 'gray')
plt.show()
"""

### FRAGA 7
#SVAR
# Vi behöver 17 bitar för att kunna representera informationspannet
# spann mellan -9437 och 58929, då behövs 17 bitar för att kunna representera det binärt.
"""
Y = cv2.dct(y)
plt.figure(3)
plt.subplot(221), plt.imshow(y, 'gray')
plt.subplot(222), plt.imshow(np.log(np.abs(Y)+1),'gray')

Yq = np.zeros((512,768))
Yq[0:128,0:196] = np.round(Y[0:128,0:196])
print(np.max(Yq))
print(np.min(Yq))
plt.subplot(223), plt.imshow(np.log(np.abs(Yq)+1),'gray')
yq = cv2.idct(Yq)
plt.subplot(224), plt.imshow(yq,'gray',clim=(0,255))
plt.show()
"""

### FRAGA 8

def imgAssessmentDct(img):
    # good: psnr=39dB
    Y = cv2.dct(img)
    height = 512
    width = 768
    Yq = np.zeros((512,768))
    goodfactor = 9/16
    heightEnd = int(np.floor(height*goodfactor))
    widthEnd = int(np.floor(width*goodfactor))
    Yq[0:heightEnd,0:widthEnd] = np.round(Y[0:heightEnd,0:widthEnd])
    goodImg = cv2.idct(Yq)
    print("psnr good: " + str(psnr(meanSquareError(goodImg, img))))
    print("bpp good: " + str(int(np.ceil(np.log2(np.max(goodImg)-np.min(goodImg))))))
    # half-good: psnr=35dB
    Y = cv2.dct(img)
    Yq = np.zeros((512,768))
    hgfactor = 1/5 #halfgoodfactor
    heightEnd = int(np.floor(height*hgfactor))
    widthEnd = int(np.floor(width*hgfactor))
    Yq[0:heightEnd,0:widthEnd] = np.round(Y[0:heightEnd,0:widthEnd])
    halfgoodImg = cv2.idct(Yq)
    print("psnr half-good: " + str(psnr(meanSquareError(halfgoodImg, img))))
    print("bpp half-good: " + str(int(np.ceil(np.log2(np.max(halfgoodImg)-np.min(halfgoodImg))))))
    plt.figure(1)
    plt.subplot(131), plt.imshow(img, 'gray')
    plt.subplot(132), plt.imshow(goodImg, 'gray')
    plt.subplot(133), plt.imshow(halfgoodImg, 'gray')
    plt.show()
#imgAssessmentDct(y)

### FRAGA 9
#SVAR
# Likheten är att de samlar de viktigaste värdena

### FRAGA 10
#SVAR
# Info samlades uppe i hörnet och då kunde man bara ta ett avgränsat
# område, storlek beroende på hur hög kvalite på bilden man vill ha.

### FRAGA 11
# SVAR
#

Y = cv2.dct(y)
Yq = np.zeros((512,768))
a = 4
b = 1.8
Yq[0:int(512/a ),0:int(768/a )] = np.round(Y[0:int(512/a ),0:int(768/a )])
yq = cv2.idct(Yq)

Yb = jl.bdct(y, (8, 8))
Ybq = np.zeros(Yb.shape)
Ybq[(0, 1, 8, 9), :]  = np.round(Yb[(0, 1, 8, 9), :])
yq2 = jl.ibdct(Ybq, (8, 8), (512, 768))

plt.figure(2)
plt.subplot(121)
plt.imshow(yq, 'gray', clim=(0, 255)),plt.title('yq')
plt.subplot(122)
plt.imshow(yq2, 'gray', clim=(0, 255)),plt.title('yq2')
plt.show()
