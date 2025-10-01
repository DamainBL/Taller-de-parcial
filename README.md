# Taller Parcial

Este repositorio contiene el taller parcial resuelto, diseñado como material de estudio de clases en python y mas importante los modificadores de acceso

## Contenido

📄 `taller python.pdf`: Documento en formato PDF con 19 preguntas resueltas.

🧾 `contador(punto20).txt`: Archivo de texto que contiene el código correspondiente a la pregunta 20.

## repuestas


### 1) Selección múltiple
A. B. D.

### 2) Salida del programa

imprime "false" en el primer parentesis y "true" en el segundo

### 3) Verdadero/Falso (explica por qué)

A). verdadero ya que esta limitado a solo a la clase y subclases
B). falso ya que este solo hace un name mangling
C). verdadero ya que segun este sera el como se realizara el
name mangling

### 4) Lectura de código

imprime "abc" porque al usar solo un "_" no se restringe su acceso mediante otras subclases

### 5) Name mangling en herencia

la salida sera "2,1" ya que primero se esta llamando a clase "sub" para luego llamar a "show" que le devuelve "__v=2" y luego "_base__v=1" que esta en la clase base

### 6) Identifica el error

nos da error porque al hacer "c.y=20" y no esya atribuido

### 7) Rellenar espacios

._numero

### 8) Lectura de métodos “privados”

este imprime " true, false, true" ya que primero verifica si "_step" esta atribuido y como este tiene solo un "_" entonces da true, "__tick" da false ya que esta protegido por doble "_" entonces no es hasta que ya pone "_m_tick" que vuelve a dar true

### 9) Acceso a atributos privados

Print(s._S__data)

### 10) Comprensión de dir y mangling

el unico que podria aparecer seria "_D__a" ya que no existe "a" y al momento de llamar a "__a" como esta tiene los dos "_" su nombre cambia debido al name mangling

### 11) Completar propiedad con validación

-- return

-- if value

### 12) Propiedad de solo lectura

def temperatura_f(self):
 return self._c * 9 / 5 + 32

### 13) Invariante con tipo

def nombre(self):
  return self._nombre
def nombre(self, value):
  if isinstance(value, str):
self._nombre = value
  else:
  raise TypeError("El
nombre debe ser una cadena
(str)")

### 14) Encapsulación de colección

def items(self):
  return tuple(self.__items)

### 15) Refactor a encapsulación

def velocidad(self):
 return self._velocidad
def velocidad(self, value):
 if (0 <= value <= 200):
 self._velocidad = value

### 16) Elección de convención

en el primer caso de "_atributo" seria para organizar los libros mientras que "__atributo" seria para
los administradores del lugar que deciden que se hace o no con un libro

### 17) Detección de fuga de encapsulación

def get_data(self):
 return self._data.copy()

### 18) Diseño con herencia y mangling

falla en "return self.__x" ya que no puede acceder de esa
manera tendria que ser usando "sef._A__x"

### 19) Composición y fachada

def guardar(self, k, v):
 self.__repo.guardar(k, v)


