import pandas as pd
import requests


def obtener_farmacias_turno():
    url = "https://farmanet.minsal.cl/index.php/ws/getLocalesTurnos"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        df = pd.DataFrame(data)
        columnas = ["localidad_nombre", "local_nombre", "local_direccion", "funcionamiento_hora"]
        disponibles = [c for c in columnas if c in df.columns]
        return df[disponibles]
    except requests.RequestException as e:
        print("Error de conexión:", e)
        return None


if __name__ == "__main__":
    df = obtener_farmacias_turno()
    if df is not None and not df.empty:
        print(f"Total farmacias de turno: {len(df)}")
        print("\nPrimeras 5:")
        print(df.head(5).to_string(index=False))
        print(f"\nFila 22:")
        if len(df) > 22:
            print(df.iloc[22].to_string())
        else:
            print("No hay suficientes registros")
    else:
        print("No se pudieron obtener datos")
