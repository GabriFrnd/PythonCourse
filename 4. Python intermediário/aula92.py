# Recarregando módulos, 'importlib' e singleton (156)

import importlib
import modulo92 # Singleton: só pode existir uma instância

importlib.reload(modulo92) # Recarregando o módulo (será executado novamente)