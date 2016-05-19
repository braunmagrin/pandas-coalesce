import pandas as pd


def coalesce(self, columns, name='coalesced'):
    """
    Coalesce the DataFrame's columns in order

    Parameters
    ----------
    columns : list-like

    Returns
    -------
    coalesced : Series
    """
    from functools import reduce
    return reduce(lambda series, col: series.fillna(self[col]),
                  columns[1:],
                  pd.Series(self[columns[0]], name=name))


pd.DataFrame.coalesce = coalesce
