import matplotlib.pyplot as plt
import numpy as np

# Vamos a desarrollar un programa de machine learning (básico)
# El siguiente es un paquete de datos a ser procesdos:
# La primera columna es: Número de horas
# La segunda columna es: Número de tareas ejecutadas
data = np.genfromtxt("web_traffic.tsv", delimiter="\t")
print(data[:10], '\n')
# Número de datos
print(data.shape)
# Se divide el array en dos vectores columnas: x, y

x = data[:,0]
y = data[:,1]
# Se muestran los valores en x, y
print(x, '\n')
print(y, '\n')

x = x[~np.isnan(y)]
y = y[~np.isnan(y)]


# Dibuja los puntos (x,y) con círculos de tamaño 10
plt.scatter(x, y, s=10)
# Títulos de la gráfica
plt.title("Tráfico Web en el último mes")
plt.xlabel("Tiempo")
plt.ylabel("Accesos/Hora")
plt.xticks([w*7*24 for w in range(10)],['semana %i' % w for w in range(10)])
plt.autoscale(tight=True)
# dibuja una cuadrícula punteada ligeramente opaca
plt.grid(True, linestyle='-', color='0.75')
# Muestra el gráfico
plt.show()