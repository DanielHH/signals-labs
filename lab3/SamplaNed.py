exec(open('preambel.py').read())

Im = np.load('pattern.npy')
plt.subplot(131)
plt.imshow(Im,'gray',clim=(-1,1))
plt.title('original pattern')

Im2 = Im[::2,::2]
plt.subplot(132)
plt.imshow(Im2,'gray',clim=(-1,1))
plt.title('downsampled pattern')


#### Fråga 19
# SVAR
# Man kastar bort varannan pixel (i x-led och y-led). Och varannan pixel blir 4 ggr så stor i den samplade bilden
# (dubbelt så stor både x- och y-led),
# och det är färre sampels vilket gör att mönstret förändras.


#### Fråga 20
# SVAR
# Bilden ska förbehandlas med bilinjär interpolation,
# alltså att bilden lågpassfiltreras och sen kastar man bort varannan pixel.


b = np.array([0.5,0.5])
b2 = np.convolve(b,b).reshape(1,-1)
aver = np.kron(b2,b2.T)

Imaver = signal.convolve2d(Im,aver,'same')
Imaver2 = signal.convolve2d(Imaver,aver,'same')
Imaver3 = signal.convolve2d(Imaver2,aver,'same')
Imaver4 = signal.convolve2d(Imaver3,aver,'same')
Imaver5 = signal.convolve2d(Imaver4,aver,'same')
Imaver6 = signal.convolve2d(Imaver5,aver,'same')
Imaver7 = signal.convolve2d(Imaver6,aver,'same')
Im3 = Imaver7[::2,::2]
plt.subplot(133)
plt.imshow(Im3,'gray',clim=(-1,1))
plt.title('pattern aver')

plt.show()

#### Fråga 21
# SVAR
# 5-7 upprepningar beroende på hur kinkig man är.
# Nackdelen är att bilden blir otydligare och otydligare (mörkare och kanter försvinner).