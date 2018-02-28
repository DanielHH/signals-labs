exec(open('preambel.py').read())

Im = np.double(misc.imread('circle.TIF'))
plt.subplot(221)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('orginal image')
plt.colorbar()




b = np.array([0.5,0.5])
b2 = np.convolve(b,b).reshape(1,-1)
d = np.array([1, -1])
cd = np.convolve(b,d)
sobelx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
sobely = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
Imsobelx = signal.convolve2d(Im, sobelx,'same')
plt.subplot(223)
plt.imshow(Imsobelx, 'gray', clim=(-128,127))
plt.title('sobelx image')
plt.colorbar()


plt.subplot(224)
Imsobely = signal.convolve2d(Im, sobely,'same')
plt.imshow(Imsobely, 'gray', clim=(-128,127))
plt.title('sobely image')
plt.colorbar()

plt.show()

### Fraga 12
#SVAR
# Flr sobelx så blir de faltade värden på gråskalan
