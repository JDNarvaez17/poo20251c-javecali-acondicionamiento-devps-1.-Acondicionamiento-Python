def suma_digitos(numero: int) -> int:
    return sum(int(d) for d in str(abs(numero)))


def contar_vocales(cadena: str) -> int:
    return sum(1 for c in cadena.lower() if c in "aeiou")


def es_palindromo(cadena: str) -> str:
    cadena_limpia = "".join(c for c in cadena.lower() if c.isalnum())
    return "Si" if cadena_limpia == cadena_limpia[::-1] else "No"


def invertir_lista(lista: str) -> str:
    return " ".join(lista.split()[::-1])


def contar_palabras(cadena: str) -> int:
    return len(cadena.split())


def max_min(lista: str) -> str:
    numeros = list(map(int, lista.split()))
    return f"{max(numeros)} {min(numeros)}"


# Ejemplo de uso
if __name__ == "__main__":
    print(suma_digitos(9876))  # Salida: 30
    print(contar_vocales("El rápido zorro"))  # Salida: 6
    print(es_palindromo("La ruta natural"))  # Salida: Si
    print(invertir_lista("10 20 30 40 50"))  # Salida: 50 40 30 20 10
    print(contar_palabras("Python es un gran lenguaje"))  # Salida: 5
    print(max_min("7 2 8 3 6 4"))  # Salida: 8 2
