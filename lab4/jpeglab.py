# JPEG lab module

import numpy as np

def rgb2ycbcr(r, g=0, b=0):
    if r.ndim == 3:
        g = r[:,:,1]
        b = r[:,:,2]
        r = r[:,:,0]
    y = (16. + 65.481*r + 128.553*g + 24.966*b)/255.
    cb = (128. - 37.797*r - 74.203*g + 112.*b)/255.
    cr = (128. + 112.*r - 93.786*g - 18.214*b)/255.
    return (y, cb, cr)

def ycbcr2rgb(y, cb, cr):
    r = 1.164*y + 1.596*cr - 0.874
    g = 1.164*y - 0.392*cb - 0.813*cr + 0.532
    b = 1.164*y + 2.017*cb - 1.086
    return (r, g, b)

def im2col_distinct(A, blocksize):
	nrows, ncols = blocksize
	nele = nrows*ncols
	nrowspad = A.shape[0]/nrows+(A.shape[0]%nrows>0)
	ncolspad = A.shape[1]/ncols+(A.shape[1]%ncols>0)	
	A1 = np.zeros((nrows*nrowspad, ncols*ncolspad))
	A1[:A.shape[0], :A.shape[1]] = A
	t = np.swapaxes(A1.reshape(nrowspad,nrows,ncolspad,ncols),0,3)
	out = t.reshape(nele,-1)
	return (out)	
	
def col2im_distinct(A, blocksize, shp):
	nrows, ncols = blocksize
	nele = nrows*ncols
	nrowspad = shp[0]/nrows+(shp[0]%nrows>0)
	ncolspad = shp[1]/ncols+(shp[1]%ncols>0)	
	t = np.swapaxes(A.reshape(ncols,nrows,ncolspad,nrowspad),0,3)
	out = t.reshape(nrows*nrowspad, ncols*ncolspad)[:shp[0],:shp[1]]
	return (out)
	
def dct2basemx(M):			#Make a 2D DCT transform matrix
	m, n = M
	dx = np.arange(m*n)
	u, v = np.meshgrid(dx % m, dx / m)
	u = u.T
	t = 2/np.sqrt(n*m) * np.sqrt(0.5)**(u==0) *	np.sqrt(0.5)**(v==0) * np.cos(np.pi*(u/(2.*m)) *	(2*u.T+1)) * np.cos(np.pi*(v/(2.*n)) * (2*v.T+1))
	return (t)
	
def bdct(im, M):				#bdct - block dct of image
	if isinstance(M,int):
		M =(M,M)
	t = np.dot(dct2basemx(M),im2col_distinct(im, M))
	return (t)

def ibdct(t, M, shp):				#bdct - block dct of image
	if isinstance(M,int):
		M =(M,M)
	if isinstance(shp,int):
		shp = (shp,shp)
	if M[0]*M[1] != t.shape[0]:
		sys.exit('The blocksize does not fit the transform image.')
	im = col2im_distinct(np.dot(dct2basemx(M).T,t), M, shp)
	return (im)

def bquant(t, qmtx):
	if isinstance(qmtx, int):
		tq = np.round(t/np.float(qmtx))# Only one quantization value
	else:
		qmtx = qmtx.reshape(-1,1)
		if t.shape[0] != qmtx.shape[0]:
			sys.exit('Wrong number of quantization values.')
		tq = np.round(t/np.kron(np.ones((1,t.shape[1])),qmtx.astype(float)))
	return (tq)
	
def brec(tq, qmtx):
	if isinstance(qmtx, int):
		t = tq*qmtx				# Only one quantization value
	else:
		qmtx = qmtx.reshape(-1,1)
		if tq.shape[0] != qmtx.shape[0]:
			sys.exit('Wrong number of quantization values.')
		t = tq*np.kron(np.ones((1,tq.shape[1])),qmtx.astype(float))
	return (t)
	
def jpgqmtx():
	Q=np.array([[ 16],
       [ 12],
       [ 14],
       [ 14],
       [ 18],
       [ 24],
       [ 49],
       [ 72],
       [ 11],
       [ 12],
       [ 13],
       [ 17],
       [ 22],
       [ 35],
       [ 64],
       [ 92],
       [ 10],
       [ 14],
       [ 16],
       [ 22],
       [ 37],
       [ 55],
       [ 78],
       [ 95],
       [ 16],
       [ 19],
       [ 24],
       [ 29],
       [ 56],
       [ 64],
       [ 87],
       [ 98],
       [ 24],
       [ 26],
       [ 40],
       [ 51],
       [ 68],
       [ 81],
       [103],
       [112],
       [ 40],
       [ 58],
       [ 57],
       [ 87],
       [109],
       [104],
       [121],
       [100],
       [ 51],
       [ 60],
       [ 69],
       [ 80],
       [103],
       [113],
       [120],
       [103],
       [ 61],
       [ 55],
       [ 56],
       [ 62],
       [ 77],
       [ 92],
       [101],
       [ 99]])
	return (Q)
