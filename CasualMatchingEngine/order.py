import numpy as np

class Order(object):
    __slots__ = ['_info']
    
    def __init__(self, order_id : Optional[int] = None, qty : Optional[int] = None):
        self._info = {
            'order_id': order_id or np.random.randint(np.iinfo(np.int64).max),
            'qty': qty or np.random.binomial(50, .5),
        }
        
    @classmethod
    def random_init(cls, order_id : Optional[int] = None, qty : Optional[int] = None):
        order_id = order_id or np.random.randint(np.iinfo(np.int64).max)
        qty = qty or np.random.binomial(50, .5)
        return cls(order_id=order_id, qty=qty)
    
    @property
    def order_id(self):
        return self._info['order_id']
    
    @order_id.setter
    def order_id(self, order_id):
        assert isinstance(order_id, int)
        self._info['order_id'] = order_id
    
    id = order_id
    
    @property
    def qty(self):
        return self._info['qty']
    
    @qty.setter
    def qty(self, qty): 
        assert isinstance(qty, int) and qty > 0
        self._info['qty'] = qty
        
    def __repr__(self):
        return f"[Order {self.order_id:019d}]: {self.qty}"