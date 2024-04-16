from ..core.data_frame import DataFrame

def filter_by_order(data_frame: DataFrame, ascending="ASC"):
    data_frame.filter(False if ascending == "ASC" else True)