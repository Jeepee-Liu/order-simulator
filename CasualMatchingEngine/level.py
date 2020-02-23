from sortedcontainers import SortedDict

from .side import SideEnum


class Level(object):
    __slots__ = ['_info', '_orders', ]
    
    def __init__(self, side:str, px:Number, orders:Iterable[Order]):
        self._orders: SortedDict = SortedDict((order.id, order) for order in orders)
        self._info: Dict = {
            'side': SideEnum.parse(side),
            'px': px,
            'n': len(orders),
            'qty': sum(order.qty for order in orders),
        }
            
    @property
    def side(self):
        return self._info['side']
    
    @side.setter
    def n(self, _side: str):
        self._info['side'] = SideEnum.parse(_side)
    
    @property
    def n(self):
        return self._info['n']
    
    @property
    def qty(self):
        return self._info['qty']
    
    @property
    def px(self):
        return self._info['px']
    
    def __repr__(self):
        orders_str = '\n'.join(f'\t{order}' for order in self._orders.values())
        return f'Level {self._info}' + ' {\n' + orders_str + '\n}'