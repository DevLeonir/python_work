import t_shirts_2_function
t_shirts_2_function.make_shirt('G', texto='Funciona na minha máquina.')

from t_shirts_2_function import make_shirt
make_shirt('G', texto='Funciona na minha máquina.')

from t_shirts_2_function import make_shirt as ms
ms('G', texto='Funciona na minha máquina.')

import t_shirts_2_function as tf
tf.make_shirt('G', texto='Funciona na minha máquina.')

from t_shirts_2_function import *
make_shirt('G', texto='Funciona na minha máquina.')