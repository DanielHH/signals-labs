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
    print(psnr(meanSquareError(goodImg, img)))
    # half-good: psnr=35dB
    halfgoodImg = bppReduction(img, 3)
    print(psnr(meanSquareError(halfgoodImg, img)))
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
    print(psnr(meanSquareError(goodImg, img)))
    # half-good: psnr=35dB
    halfgooddown = np.floor(misc.imresize(img, 0.5, interp='bicubic', mode='F'))
    halfgoodImg = misc.imresize(halfgooddown, 2., interp='bicubic', mode='F')
    print(psnr(meanSquareError(halfgoodImg, img)))
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

### FRAGA7
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

### FRAGA8

def imgAssessmentDct(img):
    # good: psnr=39dB
    Y = cv2.dct(img)
    Yq = np.zeros((512,768))
    Yq[0:128,0:196] = np.round(Y[0:128,0:196])
    goodImg = cv2.idct(Yq)
    print(psnr(meanSquareError(goodImg, img)))
    # half-good: psnr=35dB
    Y = cv2.dct(img)
    Yq = np.zeros((512,768))
    Yq[0:128,0:196] = np.round(Y[0:128,0:196])
    halfgoodImg = cv2.idct(Yq)
    print(psnr(meanSquareError(halfgoodImg, img)))
    plt.figure(1)
    plt.subplot(131), plt.imshow(img, 'gray')
    plt.subplot(132), plt.imshow(goodImg, 'gray')
    plt.subplot(133), plt.imshow(halfgoodImg, 'gray')
    plt.show()
imgAssessmentDct(y)
