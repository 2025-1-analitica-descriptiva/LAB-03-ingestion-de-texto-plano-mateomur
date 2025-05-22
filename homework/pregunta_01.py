"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.rstrip("\n") for line in lines[4:] if line.strip() != ""]

    registros = []
    actual = []

    for line in lines:
        if re.match(r"^\s*\d+\s+", line):
            if actual:
                registros.append(" ".join(actual))
            actual = [line.strip()]
        else:
            actual.append(line.strip())
    if actual:
        registros.append(" ".join(actual))

    datos = []
    for reg in registros:
        match = re.match(r"^\s*(\d+)\s+(\d+)\s+([\d,]+)\s+(.*)", reg)
        if match:
            cluster = int(match.group(1))
            cantidad = int(match.group(2))
            porcentaje = float(match.group(3).replace(",", "."))
            palabras = match.group(4).strip().rstrip(".")
            palabras = re.sub(r"^\%+\s*", "", palabras)  
            palabras = re.sub(r"\s+", " ", palabras)
            palabras = ", ".join([p.strip() for p in palabras.split(",")])
            datos.append([cluster, cantidad, porcentaje, palabras])

    columnas = [
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave",
    ]
    df = pd.DataFrame(datos, columns=columnas)
    return df