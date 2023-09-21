length = int(input())
width = int(input())
height = int(input())
percent_acc = float(input())

volume_centimeters = length * width * height
volume_litres = volume_centimeters * 0.001
acc = volume_litres * (percent_acc / 100)
total_litres = volume_litres - acc
print(total_litres)