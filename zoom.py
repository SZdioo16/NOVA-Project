# Celda 1: Zoom básico con matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Cargar imagen
img = Image.open("galaxy.jpg")
img_array = np.array(img)

# Mostrar con zoom interactivo
plt.figure(figsize=(10, 8))
plt.imshow(img_array)
plt.title("Haz click y arrastra para hacer zoom")
plt.axis('off')
plt.tight_layout()
plt.show()

print("🔍 Controles de matplotlib:")
print("   • Click izquierdo + arrastra: Zoom rectangular")
print("   • Click derecho: Zoom out")
print("   • Rueda del mouse: Zoom in/out")
print("   • Botones de navegación: Home, Back, Forward")