import cv2
execfile('preambel.py')


im1 = misc.imread('image1.png')
im2 = misc.imread('image2.png')
im3 = misc.imread('image3.png')
im4 = misc.imread('image4.png')
im5 = misc.imread('image5.png')
im6 = misc.imread('image6.png')

im1r = im1[:,:,0]
im1g = im1[:,:,1]
im1b = im1[:,:,2]
#plt.figure(1), plt.imshow(im1)
#plt.figure(2), plt.imshow(im1g,'gray')
#plt.figure(3), plt.imshow(im1b,'gray')
#plt.show()

### FRAGA 1
#SVAR
# Gul: lika blandning rott och gront
# Cyan: lika blatt ocht gront
# Magenta: lika blatt och rott
# White: lika max rgb
# SVart: 0 rgb

y, cb, cr = jl.rgb2ycbcr(im1)
y2, cb2, cr2 = jl.rgb2ycbcr(im2)
y3, cb3, cr3 = jl.rgb2ycbcr(im3)
y4, cb4, cr4 = jl.rgb2ycbcr(im4)
y5, cb5, cr5 = jl.rgb2ycbcr(im5)
y6, cb6, cr6 = jl.rgb2ycbcr(im6)

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
    halfgooddown = np.floor(misc.imresize(img, 0.5, interp='bicubic', mode='F'))
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
def frag6():
    y3 = np.floor(misc.imresize(y, 0.5, interp='bicubic', mode='F'))
    y4 = misc.imresize(y3, 2., interp='bicubic', mode='F')
    plt.figure(4), plt.imshow(y, 'gray')
    plt.figure(5), plt.imshow(y4, 'gray')
    plt.figure(6), plt.imshow(np.abs(y-y4), 'gray')
    plt.show()
#frag6()

### FRAGA 7

def frag7():
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
#frag7()

#SVAR
# Vi behover 17 bitar for att kunna representera informationspannet
# spann mellan -9437 och 58929, da behovs 17 bitar for att kunna representera det binart.


### FRAGA 8

def imgAssessmentDct(img):
    # good: psnr=39dB
    Y = cv2.dct(img)
    height = 512
    width = 768
    Yq = np.zeros((512,768))
    goodfactor = 9./16
    heightEnd = int(np.floor(height*goodfactor))
    widthEnd = int(np.floor(width*goodfactor))
    Yq[0:heightEnd,0:widthEnd] = np.round(Y[0:heightEnd,0:widthEnd])
    goodImg = cv2.idct(Yq)

    bits = np.ceil(np.log2(np.max(Yq)-np.min(Yq)))
    print(bits)
    image_part = 9./16
    bppg = bits*image_part

    print("psnr good: " + str(psnr(meanSquareError(goodImg, img))))
    print("bpp good: " + str(bppg))
    # half-good: psnr=35dB
    Y = cv2.dct(img)
    Yq = np.zeros((512,768))
    hgfactor = 1./5 #halfgoodfactor
    heightEnd = int(np.floor(height*hgfactor))
    widthEnd = int(np.floor(width*hgfactor))
    Yq[0:heightEnd,0:widthEnd] = np.round(Y[0:heightEnd,0:widthEnd])
    halfgoodImg = cv2.idct(Yq)

    bits = np.ceil(np.log2(np.max(Yq)-np.min(Yq)))
    print(bits)
    image_part = 1./5
    bpphg = bits*image_part

    print("psnr half-good: " + str(psnr(meanSquareError(halfgoodImg, img))))
    print("bpp half-good: " + str(bpphg))
    plt.figure(1)
    plt.subplot(131), plt.imshow(img, 'gray')
    plt.subplot(132), plt.imshow(goodImg, 'gray')
    plt.subplot(133), plt.imshow(halfgoodImg, 'gray')
    plt.show()
#imgAssessmentDct(y)

### FRAGA 9
#SVAR
# Likheten ar att de samlar de viktigaste vardena

### FRAGA 10
#SVAR
# Info samlades uppe i hornet och da kunde man bara ta ett avgransat
# omrade storlek beroende pa hur hog kvalite pa bilden man vill ha


### FRAGA11
def frag11():
    plt.figure(2), plt.imshow(y, 'gray', clim=(0, 255))
    Yb = jl.bdct(y, (8, 8))
    ulim = np.max(np.abs(Yb))/10
    plt.figure(3), plt.imshow(np.abs(Yb), 'gray', clim=(0, ulim))


    yn = jl.ibdct(Yb, (8, 8), (512, 768))
    plt.figure(4), plt.imshow(yn, 'gray', clim=(0, 255)), plt.show()
    print(np.max(np.abs(y-yn)))
    plt.show()


#SVAR
# 5.96855898038e-13 (typ ingen skillnad, for det borde i princip vara samma bild)
#frag11()

### FRAGA12
def frag12():
    Yb = jl.bdct(y, (8, 8))
    Ybq = np.zeros(Yb.shape)
    Ybq[(0, 1, 8, 9), :] = np.round(Yb[(0, 1, 8, 9), :])
    yq2 = jl.ibdct(Ybq, (8, 8), (512, 768))
    plt.figure(3), plt.imshow(yq2, 'gray', clim=(0, 255)), plt.show()
    print(np.max(Ybq))
    print(np.min(Ybq))


#SVAR
# max = 1753, min = -470, Spann = 2223,
# 12 bitar.

#frag12()

### FRAGA13
def frag13():
    Y = cv2.dct(y)

    Yq = np.zeros((512, 768))
    Yq[0:128, 0:196] = np.round(Y[0:128, 0:196])
    yq = cv2.idct(Yq)

    bits = np.ceil(np.log2(np.max(Yq)-np.min(Yq)))
    image_part = 1./(512/128*768/196)
    bppyq = bits*image_part

    Yb = jl.bdct(y, (8, 8))
    Ybq = np.zeros(Yb.shape)
    Ybq[(0, 1, 8, 9), :] = np.round(Yb[(0, 1, 8, 9), :])
    yq2 = jl.ibdct(Ybq, (8, 8), (512, 768))

    bits = np.ceil(np.log2(np.max(Ybq)-np.min(Ybq)))
    image_part = 1./16
    bppyq2 = bits*image_part

    plt.figure(1)
    plt.subplot(131), plt.imshow(y, 'gray')
    plt.subplot(132), plt.imshow(yq, 'gray', clim=(0, 255))
    plt.subplot(133), plt.imshow(yq2, 'gray', clim=(0, 255))

# SVAR
    print("bpp for yq: " + str(bppyq) + ", psnr yq: " + str(psnr(meanSquareError(yq, y))))
    print("bpp for yq2: " + str(bppyq2) + ", psnr yq2: " + str(psnr(meanSquareError(yq2, y))))
    plt.show()
#frag13()

### FRAGA14
def frag14(img):

    Yb = jl.bdct(img, (8, 8))
    blocks = ()
    quality = 8
    block_size = 8
    set_good = False
    set_hg = False
    bppyg = None
    bppyhg = None
    yg = np.zeros(Yb.shape)
    yhg = np.zeros(Yb.shape)
    for q in range(quality, 0, -1):
        for col in range(0, q):
            for row in range(0, q):
                blocks = blocks + (row+col*block_size,)
        Y = np.zeros(Yb.shape)
        Y[blocks, :] = np.round(Yb[blocks, :])
        pos_y = jl.ibdct(Y, (8, 8), (512, 768))
        psnr_num = psnr(meanSquareError(pos_y, img))
        #print(psnr_num)
        if psnr_num < 41 and psnr_num >= 37 and not set_good:
            yg = pos_y
            set_good = True
            bits = np.ceil(np.log2(np.max(Y) - np.min(Y)))
            image_part = float(quality**2) / 64
            bppyg = bits * image_part
        elif psnr_num < 37 and psnr_num >= 33 and not set_hg:
            yhg = pos_y
            set_hg = True
            bits = np.ceil(np.log2(np.max(Y) - np.min(Y)))
            image_part = float(quality**2) / 64
            bppyhg = bits * image_part
        blocks = ()
    plt.figure(1)
    plt.subplot(131), plt.imshow(img, 'gray')
    plt.subplot(132), plt.imshow(yg, 'gray')
    plt.subplot(133), plt.imshow(yhg, 'gray')


# SVAR
    print("bpp for good: " + str(bppyg))
    print("psnr for good: " + str(psnr(meanSquareError(yg, img))))
    print("bpp for half good: " + str(bppyhg))
    print("psnr half good: " + str(psnr(meanSquareError(yhg, img))))
    plt.show()

#frag14(y)
#frag14(y2)
#frag14(y4)
#frag14(y6)


def frag15(img):
    Yb = jl.bdct(img, (8, 8))
    Q1 = 100
    good_Q1 = None
    hg_Q1 = None
    yg = None
    yhg = None
    set_good = False
    set_hg = False
    for q in range(1, Q1):
        Ybq = jl.bquant(Yb, q)
        Ybr = jl.brec(Ybq, q)
        yr = jl.ibdct(Ybr, (8, 8), (512, 768))
        psnr_num = psnr(meanSquareError(yr, img))
        if psnr_num < 40 and psnr_num > 38 and not set_good:
            set_good = True
            good_Q1 = q
            yg = yr
        elif psnr_num < 35 and psnr_num > 33 and not set_hg:
            set_hg = True
            hg_Q1 = q
            yhg = yr
        if set_good == True and set_hg == True:
            break

    plt.figure(1)
    plt.subplot(131), plt.imshow(img, 'gray', clim=(0, 255))
    plt.subplot(132), plt.imshow(yg, 'gray', clim=(0, 255))
    plt.subplot(133), plt.imshow(yhg, 'gray', clim=(0, 255))

    print("psnr for good: " + str(psnr(meanSquareError(yg, img))))
    print("Q1 for good: " + str(good_Q1))
    print("psnr for halfgood: " + str(psnr(meanSquareError(yhg, img))))
    print("Q1 for halfgood: " + str(hg_Q1))

    plt.show()

#frag15(y)
#frag15(y2)
#frag15(y3)
#frag15(y4)
#frag15(y5)
#frag15(y6)

### FRAGA16
# SVAR
def frag16():
    Qm = jl.jpgqmtx()
    print(Qm.reshape(8, 8))
#frag16()


###FRAGA17
# SVAR
# Low frequency components are quantized to longer steps since DCT
# gathers the high frequency components in the top left corner.
# And as the JPEG standard is based on DCT it values the high frequency components higher
# than the low frequency components which can be seen in the matrix from question 16
# (short quantization steps are in the top left corner).


###FRAGA18
def frag18():
    Qm = jl.jpgqmtx()
    JPEGMEAN = np.mean(Qm)
    print(JPEGMEAN)
#frag18()

#SVAR
# 57.625

def frag19(img):

    Yb = jl.bdct(img, (8, 8))
    Q2 = 100
    good_Q2 = None
    hg_Q2 = None
    yg = None
    yhg = None
    set_good = False
    set_hg = False
    for q in range(1, Q2):
        q = float(q)/10
        Ybq = jl.bquant(Yb, jl.jpgqmtx() * q)
        Ybr = jl.brec(Ybq, jl.jpgqmtx() * q)
        yr = jl.ibdct(Ybr, (8, 8), (512, 768))
        psnr_num = psnr(meanSquareError(yr, img))
        #print(psnr_num)
        if psnr_num < 40 and psnr_num > 38 and not set_good:
            set_good = True
            good_Q2 = q
            yg = yr
        elif psnr_num < 35 and psnr_num > 33 and not set_hg:
            set_hg = True
            hg_Q2 = q
            yhg = yr
        if set_good == True and set_hg == True or psnr_num < 33:
            break

    plt.figure(1)
    plt.subplot(131), plt.imshow(img, 'gray', clim=(0, 255))
    plt.subplot(132), plt.imshow(yg, 'gray', clim=(0, 255))
    plt.subplot(133), plt.imshow(yhg, 'gray', clim=(0, 255))

    print("psnr for good: " + str(psnr(meanSquareError(yg, img))))
    print("JPEGMEAN*Q2 for good: " + str(np.mean(jl.jpgqmtx())*good_Q2))
    print("psnr for halfgood: " + str(psnr(meanSquareError(yhg, img))))
    print("JPEGMEAN*Q2 for halfgood: " + str(np.mean(jl.jpgqmtx())*hg_Q2))

    plt.show()

#frag19(y)
#frag19(y2)
#frag19(y3)
#frag19(y4)
#frag19(y5)
#frag19(y6)

def frag20(img):

    Yb = jl.bdct(img, (8, 8))
    Q1 = 100
    good_Q1 = None
    ygq1 = None
    set_good = False
    for q in range(1, Q1):
        Ybq = jl.bquant(Yb, q)
        Ybr = jl.brec(Ybq, q)
        yr = jl.ibdct(Ybr, (8, 8), (512, 768))
        psnr_num = psnr(meanSquareError(yr, img))
        if psnr_num < 40 and psnr_num > 38 and not set_good:
            set_good = True
            good_Q1 = q
            ygq1 = yr
            break

    Yb = jl.bdct(img, (8, 8))
    Q2 = 100
    good_Q2 = None
    ygq2 = None
    set_good = False
    for q in range(1, Q2):
        q = float(q)/10
        Ybq = jl.bquant(Yb, jl.jpgqmtx() * q)
        Ybr = jl.brec(Ybq, jl.jpgqmtx() * q)
        yr = jl.ibdct(Ybr, (8, 8), (512, 768))
        psnr_num = psnr(meanSquareError(yr, img))
        #print(psnr_num)
        if psnr_num < 40 and psnr_num > 38 and not set_good:
            set_good = True
            good_Q2 = q
            ygq2 = yr
            break

    plt.figure(1)
    plt.subplot(131), plt.imshow(img, 'gray', clim=(0, 255))
    plt.subplot(132), plt.imshow(ygq2, 'gray', clim=(0, 255))
    plt.subplot(133), plt.imshow(ygq1, 'gray', clim=(0, 255))

    print("Q2 psnr for good: " + str(psnr(meanSquareError(ygq2, img))))
    print("JPEGMEAN*Q2 for good: " + str(np.mean(jl.jpgqmtx())*good_Q2))

    print("Q1 psnr for good: " + str(psnr(meanSquareError(ygq1, img))))
    print("Q1 for good: " + str(good_Q1))
    print("Factor: " + str(np.mean(jl.jpgqmtx()) * good_Q2 / good_Q1))


    plt.show()

#frag20(y)
#frag20(y2)
#frag20(y3)
#frag20(y4)
#frag20(y5)
#frag20(y6)

#FRAGA20
#SVAR
# How much more you can quantize with Q2 and JPEG matrix than Q1 depends on the image.
# Q1 (uniform quantization) regards all components equally while JPEG takes into consideration
# which frequency the components have in the image. Images with a lot of
# high frequency components will se a much larger difference
# between the Q1 and Q2 quantization steps than images that are more uniform in this regard.

