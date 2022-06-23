import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'Office': ['Яндекс (Москва)', 'Яндекс (Казань)', 'Яндекс (Екатеринбург)'],
        'Stuff': [789, 543, 450],
        'Number': [123, 345, 567]}
        
frame = pd.DataFrame(data)
print(frame)

frame1 = frame.query('Number > 350 & Stuff < 700')
print(frame1)
