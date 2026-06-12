import requests


def obtener_clima(ciudad="Santiago"):
    url = f"https://wttr.in/{ciudad}?format=%C+|+%t+|+%h+|+%w"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        partes = resp.text.strip().split(" | ")
        if len(partes) >= 2:
            print(f"Clima en {ciudad}:")
            print(f"  Estado: {partes[0]}")
            print(f"  Temperatura: {partes[1]}")
            if len(partes) >= 3:
                print(f"  Humedad: {partes[2]}")
            if len(partes) >= 4:
                print(f"  Viento: {partes[3]}")
        else:
            print(resp.text)
    except requests.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    ciudad = input("Ciudad (Enter para Santiago): ").strip()
    obtener_clima(ciudad or "Santiago")
