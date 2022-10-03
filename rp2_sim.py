def asm_pio(*args, **kwargs):
    def decorador(programa):
        def compilador():
            print("Parámetros", kwargs) 
            programa()
            return None
        return compilador
    return decorador

"""

La función asm_pio es una función que recibe como parametros args que permite recibir un número de argumentos sin definir de la función de entrada (En este caso los pines, estados y demás
parametros de la función de entrada) y kawargs que tiene como finalidad acceder a una lista de argumentos sin necesidad de que todos los argumentos tengan un valor por defecto (Se usa
en las funciones que definen instancias sin necesidad de todos los argumentos pedidos), despues se define el decorador con parametro de entrada una función, se define la función del decoración
que imprime los parametros de entrada y realiza la función, la función compilar no retorna nada, el decorador retorna la función compilador y la función asm_pio retorna el decorador.

"""

def decorador_instr(fun_inst):
    def decoracion_instr(self,*args, **kwargs):
        fun_inst(self,*args, **kwargs)
        return None 
    return decoracion_instr

"""

Se define un decorador, el cual recibe una función y dentro en la función de decoración, se reciben como parametros a la maquina de ejecución(self), un args que permite recibir un número de
argumentos sin definir de la función de entrada y un kwargs, el cual permite acceder a una lista de argumentos sin necesidad de que todos los argumentos tengan un valor por defecto, en la función
de decoración se implementa la función de entrada con los parametros pedidos por la función de decorador

"""

pins='pins'

"""

Define una variable global como string 

"""

class PIO():
    OUT_LOW='PIO.OUT_LOW'
    
"""

Crea una clase de inicialización, donde al parametro OUT_LOW y le define un valor tipo string

"""  


class StateMachine:
  def __init__(self, id_, program, freq=125000000, **kwargs):
        global sm_iniciandose,fsms
        sm_iniciandose=self
        #print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        sm_iniciandose=None
        fsms[id_]=self
        pass

"""

Define una función de la clase statemachine, la cual inicializa las variables es decir es el constructor de la clase, primero define variables globales y despues inicializa una con la maquina de estados de ejecución, define una
lista de instrucciones vacia y ejecuta la función, define el número de funciones realizadas y retorna las variables a vacio
  
"""
        
  def active(self, x=None):
    '''Esta rutina simula exclisivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
    if x==1:
        print('Está pendiente de realizar la simulacón')

"""

Define una función de activación, dentro de la clase State machine, la cual permite simular si la maquina está activa o no

"""

fsms=[None]*8

"""

Crea una lista de maquinas de estado, en nuestro caso son 8 maquinas de estado en las rasberry y inicializa la lista en vacio en los 8 espacios

"""

sm_iniciandose=None    

"""

Inicializa una variable global como vacia


"""

class nop:
    @decorador_instr
    def __init__(self,*args, **kwargs):
        global sm_iniciandose
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass
"""
define una función de inicialización con el decorador instr, el cual pide argumentos de entrada para la función y la ejecuta, la función init define sm_iniciandose como una variable global e imprime el nombre
la función y la añade a lista_instr
"""
     
    def __getitem__(self,name):
        #print('nop.__getattr__',name)
        pass
    
"""
define una función, que necesita 2 parametros de entrada, pero no realiza nada
"""
        
class set(nop):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
    
"""
Crea una clase set y su constructor, la clase hereda de la clase nop la función init osea el constructor
"""
   
class wrap_target(nop):
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass
        
"""
Crea una clase wrap_target y su constructor, la clase hereda de la clase nop la función init osea el constructor
"""

  
class wrap(nop):
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass 
         
"""
Crea una clase wrap y su constructor, la clase hereda de la clase nop la función init osea el constructor
"""