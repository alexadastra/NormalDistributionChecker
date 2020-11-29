import main

paths = ['/media/sf_virtualbox/Chi_v07a.txt', '/media/sf_virtualbox/Chi_v07b.txt', '/media/sf_virtualbox/Chi_v07c.txt']
h = 0.0001
significance = \
    [0.995, 0.9, 0.8, 0.6, 0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]

num = 0
for i in paths:
    print('Distribution ', num)
    for j in significance:
        if main.is_normal(h=h, significance=j, path=i):
            print(j, ": NORMAL")
        else:
            print(j, ": NOT NORMAL")
    num += 1
