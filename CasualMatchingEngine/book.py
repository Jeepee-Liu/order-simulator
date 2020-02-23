from sortedcontainers import SortedDict
from .level import Level
from .order import Order
import numpy as np

class Book(object):
    def __init__(self):
        self._bid = SortedDict()
        self._ask = SortedDict()
        self._info = {}
    
    def random_init(self):
        for px, count in zip(np.arange(1, 11), np.histogram(np.clip(np.random.poisson(4,1000), 1, 10,), bins=10)[0]):
            self._ask[px] = Level("ASK", px, [Order() for _ in range(count)])
        for px, count in zip(np.arange(0, -10, -1), np.histogram(np.clip(np.random.poisson(4,1000), 1, 10,), bins=10)[0]):
            self._bid[px] = Level("BID", px, [Order() for _ in range(count)])
        return self
       
#     def is_crossed(self) -> bool:
#         if 
    
    def imshow(self):
        fig, ax = plt.subplots(figsize=(16,10))
        ax.barh(self._ask.keys(), [level.qty for level in self._ask.values()], color='red')
        ax.barh(self._bid.keys(), [-level.qty for level in self._bid.values()], color='blue')
        ax.grid()
        ax.set_yticks(range(self._bid.peekitem(0)[0], self._ask.peekitem(-1)[0]+1))
        plt.show()
        
    def __repr__(self):
        ask_str = '\n'.join(f'\t{level}' for level in self._ask.values())
        bid_str = '\n'.join(f'\t{level}' for level in self._bid.values())
        return f'Book {self._info}' + ' {\n' + (ask_str + bid_str).replace('\n', '\n\t') + '\n}'