# Python 101

Ejercicios prácticos de Python organizados por categoría. Ideal para repasar fundamentos, algoritmos, y herramientas del día a día.

## Requisitos

- Python 3.8+
- `pip install -r requirements.txt`

## Estructura

### basics/
| Script | Qué hace |
|---|---|
| `ciclo_for.py` | Itera días de la semana con un `for` |
| `cargar_lista.py` | Ingreso interactivo de nombres |
| `notas.py` | Calcula promedio de notas (1.0-7.0) |
| `palindromo.py` | Verificador de palabras/frases palíndromas |
| `password_gen.py` | Generador de contraseñas configurables |
| `to_do_cli.py` | Lista de tareas CLI con persistencia JSON |

### math/
| Script | Qué hace |
|---|---|
| `primos.py` | Verifica si un número es primo |
| `matrices.py` | Clasifica matrices en simétrica/antisimétrica |
| `ordenamiento_vectores.py` | Ordenamiento por selección (selection sort) |
| `fibonacci.py` | Serie Fibonacci (iterativo + recursivo) |

### games/
| Script | Qué hace |
|---|---|
| `casino-montecarlo.py` | Simulación ruleta con Monte Carlo y barra de progreso |
| `ruleta_rusa.py` | Juego de ruleta rusa con límite de intentos |

### gui/
| Script | Qué hace |
|---|---|
| `tkinter001.py` | Login/registro con contraseñas hasheadas (SHA-256) |

### chile/
| Script | Qué hace |
|---|---|
| `valida_rut.py` | Valida RUT chileno con algoritmo módulo-11 |
| `correo.py` | Envía correos vía Gmail SMTP desde variables de entorno |

### data/
| Script | Qué hace |
|---|---|
| `dic_a_dataframe.py` | Convierte JSON anidado a DataFrame de pandas |
| `test_json_df.py` | Consulta farmacias de turno (API MINSAL) y lo muestra como tabla |
| `api_weather.py` | Clima actual vía wttr.in |
| `turtle_spiral.py` | Espiral colorida con turtle graphics *(demo gráfica)* |

### stats/
| Script | Qué hace |
|---|---|
| `promedios.py` | Calcula promedio de notas ingresadas por el usuario |

## Cómo usar

```bash
git clone https://github.com/bi0punk/Python_101
cd Python_101
pip install -r requirements.txt
python basics/notas.py
```

## Proyectos adicionales relacionados

- [machine-learning-101](https://github.com/bi0punk/machine-learning-101)
- [tabla-periodic-API](https://github.com/bi0punk/tabla-periodic-API)

## Licencia

MIT
