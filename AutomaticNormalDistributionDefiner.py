import main

for path in ['/media/sf_virtualbox/Chi_v07a.txt', '/media/sf_virtualbox/Chi_v07b.txt',
             '/media/sf_virtualbox/Chi_v07c.txt']:
    print('Path is:', path)
    for degree in range(6, 13):
        for i in range(1, 1000):
            if not main.is_normal(significance=i / 1000, path=path, degree=degree):
                print("Degree: ", degree, ', significance: ', (i - 1) / 1000)
                break
