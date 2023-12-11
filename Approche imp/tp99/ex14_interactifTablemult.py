while True:
    val = input("Donner un chiffre")
    value = int(val)
    if 0 < value <=10:
        print("ok")
        for i in range(11):
            result = value * i
            print(f"{value} * {i} = {result}")
    break
