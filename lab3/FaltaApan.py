exec(open('preambel.py').read())

Im = np.double(misc.imread('baboon.TIF'))
plt.subplot(121)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('apa')
plt.colorbar()
#plt.show()

#### Fråga 6

#SVAR
#


#### Fråga 7

b = np.array([0.5,0.5])
print(b)
print('\n')
b2 = np.convolve(b,b).reshape(1,-1)
print(b2)
print('\n')
aver = np.kron(b2,b2.T)
print(aver) # Kärnan

# Kärnan ser korrekt ut


Imaver = signal.convolve2d(Im,aver,'same')
plt.subplot(122)
plt.imshow(Imaver,'gray',clim=(0,255))
plt.title('apa')
plt.colorbar()
plt.show()

#SVAR
#Det blir suddigare