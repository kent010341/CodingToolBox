import numpy as np
from CodingToolBox import DetailRecorder

dr = DetailRecorder(detail_dir='log', show_time=True)
dr.dprint({
    'number': 5,
    'numpy_array': np.random.random((3, 2)), 
    'list': [i for i in range(5)],
    'tuple': (1,2,3)
    })
dr.dprint('='*50)
dr.dprint(1, 2, 3, end='&')