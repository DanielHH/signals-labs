exec(open('preambel.py').read())
Im = np.double(misc.imread('baboon.TIF'))

plt.subplot(231)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('apa')
plt.colorbar()

plt.subplot(232)
plt.imshow(Im,'gray',clim=(50,200)) #fråga2
plt.title('högkontrast-apa')
plt.colorbar()


##### fraga 1
#print(np.min(Im)) # 2.0
#print(np.max(Im)) # 207.0

##### fraga 2
"""
 LÄGRE KONTRAST
 värde: 64
 x-koord: 62.6613
 y-koord: 15.1237
 
 HÖGRE KONTRAST
 värde: 64
 x-koord: 62.7473
 y-koord: 15.1237
"""

##### fraga 3
graycmap = plt.get_cmap('gray', 256)
gray_vals = graycmap(np.arange(256))
#print(gray_vals)

#SVAR:
#Skillnaden är att istället för att anta 256 olika värden mellan 0 och 255 (steglängd: 1),
# så antar den här tabellen 256 olika värden mellan 0 och 1 (steglängd: 1/255).


##### fraga 4
gray_vals[200:] = [1, 0, 0, 1]
plt.register_cmap('ngray', graycmap.from_list('ngray', gray_vals))

plt.subplot(234)
plt.imshow(Im,'ngray',clim=(0,255))
plt.title('apa med ngray - red')
plt.colorbar()
#SVAR
#Alla pixlar på bilden som har ett gråskalevärde som är högre än 200 blir rödfärgade [1, 0, 0, 1].


##### fraga 5

gray_vals[200:] = [0, 0, 1, 1] #blue
gray_vals[:50] = [0, 1, 0, 1] #green
plt.register_cmap('ngray', graycmap.from_list('ngray', gray_vals))

plt.subplot(235)
plt.imshow(Im,'ngray',clim=(0,255))
plt.title('apa med ngray - blue/green')
plt.colorbar()

plt.subplot(236)
plt.imshow(Im,'jet',clim=(0,255))
plt.title('apa med jet')
plt.colorbar()

#SVAR
# Apans nos blir ljusblå.



### 4.1 Förberedelseuppgift: Viktat medelvärdesbildande filter (lågpassfilter)



def on_press(event):
    print(Im[int(round(event.ydata)), int(round(event.xdata))])

fig = plt.gcf()
fig.canvas.mpl_connect('button_press_event', on_press)
plt.show()