import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 1000
def pi_este(n):
	inside_count = 0
	x_vals = np.random.uniform(-1,1,n)
	y_vals = np.random.uniform(-1,1,n)
	for i in range(n):
		if x_vals[i]**2 + y_vals[i]**2 <= 1:
			inside_count += 1
	pi_val = (4*inside_count)/n
	return inside_count, pi_val

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xs = []; ys = []
def animate(i):
    inside, y = pi_este(i)
    # if i>=100:
    # 	xs.pop(0)
    # 	ys.pop(0)
    ys.append(y)
    xs.append(i)
    ax1.clear()
    ax1.plot(xs, ys,color='mediumblue',label='Monte-Carlo estimate')
    plt.axhline(np.pi,color='Black',label='Exact $\\pi $ value')
    plt.grid(True)

    plt.xlabel('n values')
    plt.ylabel('$\\pi$ estimate')
    plt.legend(loc='lower right',prop={'size':10})
    plt.title('No. of points = %s, inside count = %s and $\\pi_{est}$ = %s'%(i,inside,round(y,5)))
    
ani = animation.FuncAnimation(fig, animate, frames=np.arange(20,n+1)) 
ani.save('Monte_Carlo_matplotlib.mp4',writer='ffmpeg',fps=30)
