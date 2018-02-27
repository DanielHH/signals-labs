exec(open('preambel.py').read())
Im = np.double(misc.imread('baboon.TIF'))

plt.subplot(121)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('lågkontrast-apa')
plt.colorbar()

plt.subplot(122)
plt.imshow(Im,'gray',clim=(50,200)) # fråga2
plt.title('högkontrast-apa')
plt.colorbar()

def on_press(event):
    print(Im[int(round(event.ydata)), int(round(event.xdata))])

fig = plt.gcf()
fig.canvas.mpl_connect('button_press_event', on_press)
plt.show()

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
print(gray_vals)
#Skillnaden är att istället för att anta 256 olika värden mellan 0 och 255 (steglängd: 1),
# så antar den här tabellen 256 olika värden mellan 0 och 1 (steglängd: 1/255).


##### fraga 4



### 4.1 Förberedelseuppgift: Viktat medelvärdesbildande filter (lågpassfilter)



