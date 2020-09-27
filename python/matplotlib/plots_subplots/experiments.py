import matplotlib.pyplot as plt
import numpy as np

f,ax = plt.subplots(3,3)
# Simple random plot
ax[0][0].plot(range(30),np.random.randint(0,100,30))
# Using map(lambda x:....) for sin(x)
ax[0][1].plot(np.arange(0.0,4*np.pi,0.01), list(map(lambda x: np.sin(x), np.arange(0.0,4*np.pi,0.01))))
# Same as before, converting map to np array using np.fromiter(...,dtype=float)
ax[0][2].plot(np.arange(0.0,4*np.pi,0.01), np.fromiter(map(lambda x: np.sin(x), np.arange(0.0,4*np.pi,0.01)),dtype=float))
# Same as before, using 'one line for' instead of arange()
ax[1][0].plot([x/1000 for x in range(0,4*3142)], list(map(lambda x: np.sin(x), [x/1000 for x in range(0,4*3142)])))
# Using the power of "np broadcast" to apply sin to all values of x
ax[1][1].plot(np.arange(0,4*np.pi,0.1),np.sin(np.arange(0,4*np.pi,0.1)))
plt.show()

xval=np.arange(0,4*np.pi,0.1)
plt.subplot(projection='polar')
plt.plot(xval,xval)
plt.plot(xval,xval+xval)

plt.show()

fig = plt.figure()
ax_cartesian = fig.add_axes([0.1,0.1,0.8,0.8])
ax_polar = fig.add_axes([0.1,0.1,0.8,0.8], polar=True, frameon=False)
ax_polar.plot(xval,xval)
ax_cartesian.plot(np.arange(0,4*np.pi,0.1),np.sin(np.arange(0,4*np.pi,0.1)))
plt.show()