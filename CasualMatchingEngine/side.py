from enum import Enum

class SideEnum(Enum):
    ASK = A = BUY = 1
    BID = B = SELL = -1
    
#     def __init__(self, side: int):
#         self._side = side
#     def repr(self):
        
    
    @staticmethod
    def parse(raw_side: Union[int, str]):
        if isinstance(raw_side, int) and raw_side in {-1, 1}:
            return SideEnum(raw_side)
        elif isinstance(raw_side, str):
            if raw_side.upper() in {'A', 'ASK', 'BUY',}:
                return SideEnum.ASK
            elif raw_side.upper() in {'B', 'BID', 'SELL'}:
                return SideEnum.BID
            else:
                raise ValueError(f'Unrecognized side string: {raw_side}')
        else:
            raise ValueError(f'Unknown input for side: {raw_side}')