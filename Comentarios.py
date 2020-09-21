#-----------------------------INICIO---------------------------------------#

#Se inicializa un for en la que se  utiliza la funcion ZIP la cual toma como
#Argumentos (models, linestyles, colors) los cuales son objetos iterables y 
#La funcion ZIP retorna un nuevo iterable cuyos elementos son tuplas que 
#Contienen un elemento de cada uno de los 
#Iteradores originales los cuales son: (model, style, color)
        for model, style, color in zip(models, linestyles, colors):
            #Genera, mas no muestra, diferentes graficas por cada iterador
            #Devuelto por ZIP, generando graficas con diferentes estilos
            #de lina, color, y tamaño
            plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)
        #Para cada modelo genera una legend la cual contiene informacion
        #de cada grafico, esta leyenda esta ubicada en la esquina superior
        #izquierda
        plt.legend(["d=%i" % m.order for m in models], loc="upper left")
    #Ajuste de escala automatico 
    plt.autoscale(tight=True)
    #Minimo en y es cero
    plt.ylim(ymin=0)
    #Definicion de maximos en Y y minimos en X
    if ymax:
        plt.ylim(ymax=ymax)
        
    if xmin:
        plt.xlim(xmin=xmin)
    #Crea las cuadriculas en la grafica
    plt.grid(True, linestyle='-', color='0.75')
    #Se guarda el grafico en un archivo
    plt.savefig(fname)
# Primera mirada a los datos
# -----------------------------------------------------------------
#Se hace el llamado a la funcion la cual grafica los datos
#y los guarda en una imagen
plot_models(x, y, None, os.path.join(CHART_DIR, "1400_01_01.png"))


# Con la funcion polyfit elegimos el grado polinomial(1)
#con el cual queremos ver los datos (tercer parametro)
fp1, res1, rank1, sv1, rcond1 = np.polyfit(x, y, 1, full=True)
print("Parámetros del modelo fp1: %s" % fp1)
print("Error del modelo fp1:", res1)
f1 = sp.poly1d(fp1)

#Lo mismo hecho anteriormento pero de grado 2
fp2, res2, rank2, sv2, rcond2 = np.polyfit(x, y, 2, full=True)
print("Parámetros del modelo fp2: %s" % fp2)
print("Error del modelo fp2:", res2)
f2 = sp.poly1d(fp2)

#Genera diferentes ecuaciones polinomiales
#para saber cual de ellas se ajusta con exactitud
#a la grafica generada 
f3 = sp.poly1d(np.polyfit(x, y, 3))
f10 = sp.poly1d(np.polyfit(x, y, 10))
f100 = sp.poly1d(np.polyfit(x, y, 100))

# Se grafican los modelos
# -----------------------------------------------------------------
plot_models(x, y, [f1], os.path.join(CHART_DIR, "1400_01_02.png"))
plot_models(x, y, [f1, f2], os.path.join(CHART_DIR, "1400_01_03.png"))
plot_models(
        x, y, [f1, f2, f3, f10, f100], os.path.join(CHART_DIR,
                                                    "1400_01_04.png"))

# Ajusta y dibuja un modelo utilizando el conocimiento del punto
# de inflexión
# -----------------------------------------------------------------
#En la semana 3.5 se presenta un punto de quierbre en el cual
#a partir de el se toman los puntos finales e iniciales
#para asi generar una recta con estos 

inflexion = 3.5 * 7 * 24
xa = x[:int(inflexion)]
ya = y[:int(inflexion)]
xb = x[int(inflexion):]
yb = y[int(inflexion):]

# Se grafican dos líneas rectas
# -----------------------------------------------------------------
#Se generan las rectar a partir de la semana 3.5
#con los puntos tomados anteriormente
fa = sp.poly1d(np.polyfit(xa, ya, 1))
fb = sp.poly1d(np.polyfit(xb, yb, 1))

# Se presenta el modelo basado en el punto de inflexión
# -----------------------------------------------------------------
plot_models(x, y, [fa, fb], os.path.join(CHART_DIR, "1400_01_05.png"))

# Función que calcula el nivel de error presentado en la prediccion
# -----------------------------------------------------------------
def error(f, x, y):
    return np.sum((f(x) - y) ** 2)

# Se imprimen los errores
# -----------------------------------------------------------------
print("Errores para el conjunto completo de datos:")
for f in [f1, f2, f3, f10, f100]:
    print("Error d=%i: %f" % (f.order, error(f, x, y)))
    
print("Errores solamente después del punto de inflexión")
for f in [f1, f2, f3, f10, f100]:
    print("Error d=%i: %f" % (f.order, error(f, xb, yb)))
    
print("Error de inflexión=%f" % (error(fa, xa, ya) + error(fb, xb, yb)))

# Se extrapola de modo que se proyecten respuestas en el futuro
# Se crea un modelo de aproximacion y ajuste, enviandole los vectores X, Y,
#  y los polinomios f1, f2, f3, f10, f100, la grafica generada se guarda en
# el directiorio char, mx limita el rango de las x, donde el ymax es 10000
# xmin es 0
# -----------------------------------------------------------------
plot_models(
    x, y, [f1, f2, f3, f10, f100],
    os.path.join(CHART_DIR, "1400_01_06.png"),
    mx=np.linspace(0 * 7 * 24, 6 * 7 * 24, 100),
    ymax=10000, xmin=0 * 7 * 24)

#-----------------------------FIN---------------------------------------#