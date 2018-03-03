exec(open('preambel.py').read())

Im = np.double(misc.imread('baboon.TIF'))
plt.subplot(131)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('apa')
plt.colorbar()
#plt.show()


#### Fråga 6

#SVAR
# Resultatet av filtret ska bli 1.
# Filtret får ett högre värde (man släpper igenom högre frekvenser), vilket resulterar i en ljusare bild.


#### Fråga 7
b = np.array([0.5,0.5])
d = np.array([1, -1])
print(b)
print('\n')
b2 = np.convolve(b,b).reshape(1,-1)
print(b2)
print('\n')
aver = np.kron(b2,b2.T)
print(aver) # Kärnan

# Kärnan ser korrekt ut

Imaver = signal.convolve2d(Im,aver,'same')
plt.subplot(132)
plt.imshow(Imaver,'gray',clim=(0,255))
plt.title('faltad apa')
plt.colorbar()
#plt.show()

#SVAR
#Det blir suddigare


### Fråga 8

#SVAR
#Same gör att Imaver har samma storlek som Im.
#help(signal.convolve2d)


### Fråga 9
Imaver2 = signal.convolve2d(Imaver,aver,'same')
Imaver3 = signal.convolve2d(Imaver2,aver,'same')
plt.subplot(133)
plt.imshow(Imaver3,'gray',clim=(0,255))
plt.title('trippelfaltad apa')
plt.colorbar()
plt.show()

#SVAR
#Bilder blir mjukare, men färre och färre detaljer syns

### Fraga 10
cd = np.convolve(b,d)

### Fraga 11
"""
[-1, -2, -1,
0, 0, 0
1, 2, 1]
"""

#
