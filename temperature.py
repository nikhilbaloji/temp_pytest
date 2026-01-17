def classify(temp):
    if temp < 20: return "Cold"
    if temp <= 30: return "Normal"
    return "Hot"

if __name__ == "__main__":
    t=float(input())
    print(classify(t))
