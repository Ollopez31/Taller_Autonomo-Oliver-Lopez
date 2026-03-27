
import itertools
import time
import matplotlib.pyplot as plt

contra = "alp"
alphabet = "abcdefghijklmnopqrstuvwxyz"
intentos = 0
tiempo = time.time()
clave = False

for longitud in range(1, 10):
    if clave:
        break
        
    for adivina in itertools.product(alphabet, repeat=longitud):
        intentos += 1
        contra_for = "".join(adivina)
        
        if contra_for == contra:
                       
            print(f"Contraseña '{contra_for}' encontrada.")
            print(f"Intentos totales: {intentos}")
            
            clave = True
            break

if not clave:
    print("No se encontró la contraseña dentro del límite de longitud establecido.")



alfabeto = "abcdefghijklmnopqrstuvwxyz"
longitudes = [1, 2, 3, 4] 
tiempos = []

print("--- Iniciando Experimento de Fuerza Bruta (Oliver) ---")


for L in longitudes:
    target = "a" * L 
    
    inicio = time.time()
    
    
    for combinacion in itertools.product(alfabeto, repeat=L):
        intento = "".join(combinacion)
        
        if intento == target:
            fin = time.time()
            tiempo_total = fin - inicio
            tiempos.append(tiempo_total) # Guardamos el tiempo para el gráfico
            print(f"Longitud {L}: Encontrada en {tiempo_total:.6f} segundos.")
            break


import matplotlib.pyplot as plt

# Aquí pegas los resultados que salieron en la terminal del primer código
longitudes = [1, 2, 3, 4] 
tiempos = [0.0001, 0.0025, 0.0650, 1.6800] # Ejemplo de lo que te salga en la terminal

# --- PLANO CARTESIANO ---
plt.figure(figsize=(8, 5))

# TENDENCIA ALCISTA (Tiempo aumenta con la longitud)
plt.plot(longitudes, tiempos, marker='o', color='cyan', label='Tendencia Alcista (Tiempo)')

# TENDENCIA BAJISTA (Conceptualmente: si achicamos el alfabeto, los puntos bajarían)
# Agregamos una línea punteada para mostrar la diferencia
tiempos_bajos = [t * 0.1 for t in tiempos] 
plt.plot(longitudes, tiempos_bajos, linestyle='--', color='orange', label='Tendencia Bajista (Menos caracteres)')

plt.title('Gráfico de Complejidad - Oliver')
plt.xlabel('Longitud de Contraseña')
plt.ylabel('Tiempo (Segundos)')
plt.legend()
plt.grid(True, alpha=0.3)

print("Mostrando el plano cartesiano...")
plt.show()








