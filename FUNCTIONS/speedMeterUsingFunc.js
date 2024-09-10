def speedMeter(speed):
    if speed < 60: return "Normal"
    elif speed >= 60 and speed < 80: return "Warning"
    else: return "Over Speed"
speed = int(input())
print(speedMeter(speed))
