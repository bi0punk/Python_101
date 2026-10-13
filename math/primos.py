class Primo:
    def __init__(self, num):
        self.num = num
        
    def es_primo(self):
        if self.num < 2:
            return False
        return all(self.num % i != 0 for i in range(2, int(self.num**0.5) + 1))

if __name__ == "__main__":
    print("Numeros primos")
    num = int(input("Ingrese un numero: "))
    primo = Primo(num)
    if primo.es_primo():
        print("El numero es primo")
    else:
        print("El numero no es primo")
