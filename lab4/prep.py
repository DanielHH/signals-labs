exec(open('preambel.py').read())

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

def imgAssesmentBppred(img):
    # good: psnr=39dB
    goodImg = bppReduction(img, 2)
    print(psnr(meanSquareError(goodImg, img)))
    # half-good: psnr=35dB
    halfgoodImg = bppReduction(img, 3)
    print(psnr(meanSquareError(halfgoodImg, img)))
    plt.figure(1), plt.imshow(img)
    plt.figure(2), plt.imshow(goodImg)
    plt.figure(3), plt.imshow(halfgoodImg)
    plt.show()
#imgAssesmentBppred(im2)

### FRAGA 5

def imgAssesmentImresize(img):
    # good: psnr=39dB
    gooddown = np.floor(misc.imresize(img, 3/4, interp='bicubic', mode='F'))
    goodImg = misc.imresize(gooddown, 4/3, interp='bicubic', mode='F')
    print(psnr(meanSquareError(goodImg, img)))
    # half-good: psnr=35dB
    halfgooddown = np.floor(misc.imresize(img, 0.5, interp='bicubic', mode='F'))
    halfgoodImg = misc.imresize(halfgooddown, 2., interp='bicubic', mode='F')
    print(psnr(meanSquareError(halfgoodImg, img)))
    plt.figure(1), plt.imshow(img, 'gray')
    plt.figure(2), plt.imshow(goodImg, 'gray')
    plt.figure(3), plt.imshow(halfgoodImg, 'gray')
    plt.show()
#imgAssesmentImresize(y)

### FRAGA 6

y3 = np.floor(misc.imresize(y, 0.5, interp='bicubic', mode='F'))
y4 = misc.imresize(y3, 2., interp='bicubic', mode='F')
plt.figure(4), plt.imshow(y, 'gray')
plt.figure(5), plt.imshow(y4, 'gray')
plt.figure(6), plt.imshow(np.abs(y-y4), 'gray')
plt.show()
