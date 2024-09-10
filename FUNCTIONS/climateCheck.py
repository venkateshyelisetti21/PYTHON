def climate(temperature):
    if temperature < 22: return "Cold"
    elif temperature >= 22 and temperature < 35: return "Warm"
    else: return "Hot"
temperature = int(input())
print(climate(temperature))
