from logging import exception
import math

def Schitaem():
    try:
        operations = ["+", "-", "/", "*", "//", "**", "%", "comb", "Copysign", "ldexp", "Hypot", "PPar", "SPar"]
        a, b = (float(input("Введите число: ")) for i in range(2))
        print("Список операций:")
        for i in range(len(operations)):
            print(operations[i], end=" ")
        operation = input("\nВведите операцию: ")
        match operation:
            case "+":
                print("a + b = ", a + b)
            case "-":
                print("a - b = ", a - b)
            case "/":   
                print("a / b = ", a / b)
            case "*":
                print("a * b = ", a * b)
            case "//":
                print("a // b = ", a // b)
            case "**":
                print("a ** b = ", a ** b)
            case "%":
                print(f"a % b", a % b)
            case "comb":
                print("a comb b = ", math.comb(int(a), int(b)))
            case "Copysign":
                print("a Copysign b = ", math.copysign(a, b))
            case "ldexp":
                print("ldexp(a,b) = ", math.ldexp(int(a), int(b)))
            case "Hypot":
                print("Fabs(a,b) = ", math.hypot(a, b))
            case "PPar":
                d = float(input("Введите дополнительное значение: "))
                f = lambda a, b, d: (a + b + d) * 4
                print("PPar(a,b,c) = ", f(a, b, d))
            case "SPar":
                d = float(input("Введите дополнительное значение: "))
                f = lambda a, b, d: ((a * b) + (a * d) + (d * b)) * 2
                print("SPar(a,b,d) = ", f(a, b, d))
    except Exception:
        print("Нормально вводи!")

def Stroki():
    try:
        str = input("Введите строку: ")
        space = str.count(" ")
        comma = str.count(",")
        strlen = len(str)
        print("Кол-во символов: ", strlen)
        print("Кол-во пробелов: ", space)
        print("Кол-во запятых: ", comma)
    except Exception:
        print("Нормально вводи!")

def Matritsa():
    try:
        a = int(input("Кол-во столбцов в матрице: "))
        b = int(input("Кол-во строк в матрице: "))
        c = int(input("Начальное число: "))
        d = int(input("Шаг: "))
        Matritsa = []
        for i in range(b):
            Matritsa.append([])
            for j in range(a):
                Matritsa[i].append(c)
                c += d
        for i in range(b):
            for j in range(a):
                print(Matritsa[i][j], end = " ")
            print("")
    except Exception:
        print("Нормально вводи!")

def main():
    while True:
        try:
            a = int(input("Выбери задание(1-3), 0-Выход\n"))
            match a:
                case 1:
                    Schitaem()
                case 2:
                    Stroki()
                case 3:
                    Matritsa()
                case 0:
                    break
        except Exception:
            print("Нормально вводи!")

if __name__ == "__main__":
    main()