def calcular_retorno_diario(precio_actual, precio_anterior):
    if precio_anterior == 0:
        raise ValueError("precio_anterior no puede ser 0 (division por cero)")

    return ((precio_actual - precio_anterior) / precio_anterior) * 100


def categorizar_volatilidad(desviacion_estandar):
    if desviacion_estandar < 2:
        return "Baja"
    elif desviacion_estandar <= 5:
        return "Media"
    else:
        return "Alta"
