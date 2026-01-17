import sys

def temperature(temp):
    if temp < 20:
        return "cold"
    elif temp <= 30:
        return "normal"
    else:
        return "hot"


if __name__ == "__main__":
    temp = float(sys.argv[1])
    print(temperature(temp))
