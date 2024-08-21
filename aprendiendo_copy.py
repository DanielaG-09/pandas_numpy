import numpy as np
arr = np.arange(0,11)
print(arr)
trozo_de_arr = arr[0:6] 
print(trozo_de_arr)
#A todo mi arreglo le quiero quitar todos los valores y dejarlos en cero
trozo_de_arr[:] = 0
print(trozo_de_arr)
#Si ahora imprimimos el array completo veremos que todos los valores han sido cambiados
print(arr)
#Para solucionar esto utilizaremos el comando copy
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)
#No obstante, la lista orginal permanece intacta
print(arr)