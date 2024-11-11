from aspose.threed import Scene
from aspose.threed.entities import Sphere

import matplotlib.pyplot as plt

# Crear un objeto de la clase Escena.
scene = Scene()

# Crear un modelo de esfera
scene.root_node.create_child_node("Sphere", Sphere())

plt.show()

