import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(-np.pi/2, np.pi/2, 1000)
y = (0.64*np.sqrt(np.abs(x))-0.8+1.2**np.abs(x)*np.cos(200*x))*np.sqrt(np.cos(x))

fig, ax = plt.subplots()
line, = ax.plot(x, y, color='red')

text = ax.text(0, 0, "I love you", fontsize=50, ha='center', va='center', color='white', zorder=10)

def animate(i):
    line.set_ydata((0.64*np.sqrt(np.abs(x))-0.8+1.2**np.abs(x)*np.cos(200*(x+i/15)))*np.sqrt(np.cos(x)))
    text.set_position((0, 1.2*np.sqrt(np.cos(x.max())))) # update the text position
    return line, text

ani = animation.FuncAnimation(fig, animate, frames=1000, interval=20, blit=True)

plt.title("kreggscode")
plt.show()