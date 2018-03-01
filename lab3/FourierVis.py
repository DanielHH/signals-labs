exec(open('preambel.py').read())


#### Fråga 22
"""
testarr = ([1,2,3,4,5,6,7])

rad1 = np.fft.ifftshift(testarr)
print(rad1)

rad2 = np.fft.fft(rad1)
print(rad2)

###

rad3 = np.fft.fftshift(rad2)
print(rad3)

###

rad2igen = np.fft.ifftshift(rad3)
print(rad2igen)

rad1igen = np.fft.ifft(rad2igen)
print(rad1igen)

original = np.fft.fftshift(rad1igen)
print(original)

"""

Im = np.load('pirat2.npy')

IM = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(Im)))
plt.subplot(221), plt.imshow(np.log(np.abs(IM)+1),'gray'), plt.colorbar()
plt.subplot(222), plt.imshow(np.angle(IM)>np.mean(np.angle(IM)),'gray'), plt.colorbar()
plt.subplot(223), plt.imshow(np.real(IM),'gray', clim=(-1000, 1000)), plt.colorbar()
plt.subplot(224), plt.imshow(np.imag(IM),'gray'), plt.colorbar()

plt.show()



#### Fråga 23
#SVAR
# När man shiftar så hamnar alla höga frekvenser ut med hörnen, och de lägra hamnar i mitten av bilden.
# Då när man fourier transformar så kommer alltså utslagen att ges vid hörnen och kanterna.
# Vid nästa shift så samlas de högsta frekvenserna i mitten av billden, alltså blir det en vit prick i mitten.


#Utan ifftshift()

IM = np.fft.fftshift(np.fft.fft2(Im))
plt.subplot(221), plt.imshow(np.log(np.abs(IM)+1),'gray'), plt.colorbar()
plt.subplot(222), plt.imshow(np.angle(IM)>np.mean(np.angle(IM)),'gray'), plt.colorbar()
plt.subplot(223), plt.imshow(np.real(IM),'gray', clim=(-1000, 1000)), plt.colorbar()
plt.subplot(224), plt.imshow(np.imag(IM),'gray'), plt.colorbar()

plt.show()

#### Fråga 24

#SVAR
# Första bilden är världigt lik i båda versionerna,
# vilket vi tror beror på att efter fouriertransformen
# så samlas alla höga frekvenser i mitten vid skiftningen hursom.
# Andra bilden blir kornigare, vilket kan bero på att eftersom man inte skiftade innan fouriertransformen
# så var det mycket spritt var de olika frekvenserna befann sig i bilden och därför blir det kornigare.