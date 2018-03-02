exec(open('preambel.py').read())

im1 = misc.imread('image1.png')
im1r = im1[:,:,0]
im1g = im1[:,:,1]
im1b = im1[:,:,2]
plt.figure(1), plt.imshow(im1)
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
    return 10*np.log(255**2/mse)

print(psnr(meanSquareError(im1g, im1r)))

def bppReduction(img, bits_to_reduce):
    X = 2**bits_to_reduce
    return X*np.floor_divide(img,X)

plt.figure(2), plt.imshow(bppReduction(im1, 4))
plt.show()
