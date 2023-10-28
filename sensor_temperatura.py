from matplotlib import pyplot as plt
from matplotlib import animation
import Adafruit_DHT # Para usar DHT-11 más convenientemenete 

"""
Asegurarse de introducir los comandos en la terminal para reducir la posibilidad de algunos bloqueos:
sudo apt-get install libatlas-base-dev
pip3 uninstall numpy
sudo apt install python3-matplotlib python3-numpy python3-pandas
"""

sensor = Adafruit_DHT.DHT11
pin = 20

fig = plt.figure() # Crear objeto matplotlib.pyplot.
ax = plt.axes(xlim=(0, 30), ylim=(15,45)) # Se establece el eje 
max_points = 30 # Cantidad de Datos que se expresaraán como el número de puntos
line, = ax.plot(np.arange(max_points),
                np.ones(max_points, dtype=np.float) * np.nan, lw=1, c='blue', marker = 'd', ms = 2)
"""
Trazar con max_points componentes-x de la forma (0, 1, 2 ... max_point-1) y componentes-y
con max_points en una matriz que contiene 1
"""

def init():
    return line 

h, t = Adafruit_DHT.read_retry(sensor, pin) # Almacena la humedad y la temperatura en DHT-11 a h y t, respectivamente

def animate (i):
    h, t = Adafruit_DHT.read_retry(sensor, pin) # Valor de temperatura del sensor a y para la visualización animada.
    y = t
    old_y = line.get_ydata() # Obtener los datos de la linea
    new_y = np.r_[old_y[1:], y] # Moverlos un espacio a la derecha 
    line.set_ydata(new_y) # Asignarlos como los nuevos ydata para la línea
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval = 200, interval = 20, blit = False)
"""
    - fig: es un objeto plt
    - animate: función para animación 
    - init_func: Función de inicialización 
"""
plt.show() # Se imprime en pantalla 
