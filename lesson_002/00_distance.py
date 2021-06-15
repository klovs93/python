
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}
coor_mos_to_lon = sites.get('Moscow')
coor_lon_to_mos = sites.get('London')
coor_mos_to_par = sites.get('Moscow')
coor_par_to_mos = sites.get('Paris')
coor_par_to_lon = sites.get('Paris')
coor_lon_to_par = sites.get('London')

distances={
    'MoscowToLondon':{(((coor_mos_to_lon.__getitem__(0)-coor_lon_to_mos.__getitem__(0))**2) +((coor_mos_to_lon.__getitem__(1)-coor_lon_to_mos.__getitem__(1))**2))**0.5},
    'MoscowToParis':{(((coor_mos_to_par.__getitem__(0)-coor_par_to_mos.__getitem__(0))**2) +((coor_mos_to_par.__getitem__(1)-coor_par_to_mos.__getitem__(1))**2))**0.5},
    'ParisToLondon':{(((coor_par_to_lon.__getitem__(0)-coor_lon_to_par.__getitem__(0))**2) +((coor_par_to_lon.__getitem__(1)-coor_lon_to_par.__getitem__(1))**2))**0.5}
}
print(distances)




