exec(open('preambel.py').read())

Im = np.load('pirat.npy')
plt.subplot(141)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('orginal image')
plt.colorbar()

d = np.array([1, -2, 1])
d2 = np.array([[1], [-2], [1]])
laplace = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

Imlaplace = signal.convolve2d(Im, laplace,'same')
plt.subplot(142)
plt.imshow(Imlaplace, 'gray', clim=(-100,100))
plt.title('laplace image')
plt.colorbar()

### Fraga 16
#SVAR
# Kontrasten blir högre

### Fraga 17
#svar
# Det är större filtersvar i regioner med snabba förändringar än det är i regioner med jämna ytor.
# Kanter blir utmärkande.

ImHP = -Imlaplace

Imsharp = Im + ImHP
plt.subplot(143)
plt.imshow(Imsharp,'gray',clim=(-100, 100))
plt.title('imsharp')
plt.colorbar()

Imsharp2 = Im + 2*ImHP
plt.subplot(144)
plt.imshow(Imsharp2,'gray',clim=(-100, 100))
plt.title('imsharp2')
plt.colorbar()

plt.show()

### Fraga 18
#svar
# För att färgerna är olika och tar ut varandra annars.
