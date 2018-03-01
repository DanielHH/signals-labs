exec(open('preambel.py').read())

Im = np.double(misc.imread('circle.tif'))
plt.subplot(121)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('orginal image')
plt.colorbar()

d = np.array([1, -2, 1])
d2 = np.array([[1], [-2], [1]])
laplace = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

Imlaplace = signal.convolve2d(Im, laplace,'same')
plt.subplot(122)
plt.imshow(Imlaplace, 'gray', clim=(-200,200))
plt.title('laplace image')
plt.colorbar()

plt.show()

### Fraga 15
#SVAR
# Ja, cirkeln stömmer väl överens med orginalet.
