exec(open('preambel.py').read())
Im = np.double(misc.imread('baboon.TIF'))
plt.subplot(121)
plt.imshow(Im,'gray',clim=(0,255))
plt.title('apa')
plt.colorbar()

def on_press(event):
    print(Im[int(round(event.ydata)), int(round(event.xdata))])

fig = plt.gcf()
fig.canvas.mpl_connect('button_press_event', on_press)
plt.show()


###### fraga 1
#print(np.min(Im)) # 2.0
#print(np.max(Im)) # 207.0

##### fraga 2
