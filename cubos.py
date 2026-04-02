import matplotlib.pyplot as plt
''' criando um grafico com potencias de 3'''

eixo_x = range(1, 5001)
eixo_y = [ eixo_y**3 for eixo_y in eixo_x]
cmap = plt.colormaps['flag']

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(eixo_x, eixo_y, c= eixo_y, cmap=plt.colormaps['flag'],s=10)
ax.set_title("Números ao cubo", fontsize=24)
ax.set_xlabel("Números elevados ao cubo", fontsize=12)
ax.set_ylabel("Resultado", fontsize=12)
ax.axis([0, 100, 0, 1000000])
ax.ticklabel_format(style='plain')
ax.tick_params(labelsize=6)

plt.show()
