import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader as web

# plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')
# plt.style.use('bmh')
# plt.style.use('seaborn-white')
plt.style.use('seaborn-deep')

x = np.linspace(0, 2*np.pi, 10)
y1 = np.sin(x)
y2 = np.cos(x)

font1 = {'family' : 'serif', 'color':'blue', 'size':20}
font2 = {'family' : 'serif', 'color':'darkred', 'size':15}
plt.figure(figsize=(12,8))
# mec = markeredgecolor/mfc = markerfacecolor/ ms = markersize/lw line width
plt.plot(x,y1, linewidth=4, label='sin(x)',color='r', marker = 'H', ms = 20, mec = 'g', mfc = 'r', linestyle=':')
plt.plot(x,y2, linewidth=4, label='cos(x)',color='c', marker = 'D', ms = 20, mec = 'y', mfc = 'b')
plt.legend(fontsize = 20, loc='center right')
plt.title("Sine of x", fontdict=font2, loc = 'left')
# axis means show only x axis
# plt.grid(axis= 'x')
plt.grid(axis= 'y')
plt.xlabel("Samples", fontdict=font1)
plt.ylabel("Mag", fontsize = 20, fontdict=font1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()

# plot style
# classic
# • fivethirtyeight
# • ggplot
# • bmh
# • grayscale
# • seaborn-dark
# • seaborn-
# darkgrid
# • seaborn-deep
# • seaborn-
# whitegrid

# Line color
# 1. ”b” = blue
# 2. ”g” = green
# 3. ”r” = red
# 4. ”c” = cyan
# 5. ”m” = magenta
# 6. ”y” = yellow
# 7. ”k” = black
# 8. ”w” = white

# Line Styles
# 1. ”-” = ’solid’ (default)
# 2. ”:” = ’dotted’
# 3. ”–” = ’dashed’
# 4. ”-.” = ’dashdot’
# 5. ” ” = ’None’

# Marker & Marker size & Marker color
# 1. ”o” = circle
# 2. ”*” = star
# 3. ”.” = point
# 4. ”,” = pixel
# 5. ”s” = square
# 6. ”D” = diamond
# 7. ”p” = pentagon
# 8. ”H” = hexagon
# 9. ”v” = triangle
# down
# 10. ”ˆ” = triangle up
# 11. ”1” = tri down
# 12. ”2” = tri up
# 13. ”3” = tri left
# 14. ”4” = tri right
# 15. ”|” = vline
# 16. ” ” = hline

# plt.legend
# upper right
# • upper left
# • upper center
# • lower right
# • lower left
# • lower center
# • center left
# • center right

x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
x2 = np.array([0,1,2,3])
y2 = np.array([6,2,7,11])
plt.plot(x1,y1,x2,y2)
plt.show()



