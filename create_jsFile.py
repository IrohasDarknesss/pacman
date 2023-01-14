name_list = ['game','ghost', 'pacman']
extension = '.js'

for name in name_list:
    with open(name + extension, 'w') as f:
        f.close()