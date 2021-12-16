# put your python code here
length = int(input())
width = int(input())
height = int(input())
sum_edge_lengths = 4 * (length + width + height)
surface_area = 2 * (length * width + width * height + height * length)
volume = length * width * height
print(sum_edge_lengths)
print(surface_area)
print(volume)