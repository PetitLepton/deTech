'''This module provides a set of functions to render HTML tables.'''


def align_left(df, row_heading=False, hide_row_heading=False, columns=None):
    '''This function aligns the column headers to the left as well
    as provided columns.

    Args:
        df (pandas.DataFrame): the input DataFrame
        row_heading (bool, default False): if True, align left the
            index column
        columns (list, default None): list of columns to align left
    Returns:
        pandas.io.formats.style.Styler'''

    left_text = dict(props=[('text-align', 'left')])
    right_text = dict(props=[('text-align', 'right')])

    styles = [
        dict(selector='th.col_heading', **left_text),
        dict(selector='th.index_name', **left_text), ]

    if not columns:
        columns = []

    if row_heading:
        styles.append(dict(selector='th.row_heading', **left_text))
    else:
        if hide_row_heading:
            styles.extend([
                dict(selector='th.row_heading', props=[('display', 'none')]),
                dict(selector='th.index_name', props=[('display', 'none')])])
        else:
            styles.append(dict(selector='th.row_heading', **right_text))

    for n, column in enumerate(df.columns):
        if column in columns:
            styles.append(dict(selector='td.col{}'.format(n), **left_text))
        else:
            styles.append(dict(selector='td.col{}'.format(n), **right_text))

    return df.style.set_table_styles(styles)
