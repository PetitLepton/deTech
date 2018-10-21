""""""

BG_COLOR = "#FFFFFF"
LEGEND_BG_COLOR = "#FFFFFF"
LEGEND_BORDER_COLOR = "#FFFFFF"
DARK_TEXT_COLOR = "#000000"
LIGHT_TEXT_COLOR = "#808080"  # gray
GRID_COLOR = "#DCDCDC"  # gainsboro
FONT_FAMILY = "sans-serif"
BASE_FONT_SIZE = 16  # px
BASE_LINE_HEIGHT = 24  # px


"""The following functions are inspired from
http://sunlightfoundation.com/blog/2014/03/12/datavizguide/ and
https://betterwebtype.com/rhythm-in-web-typography

In the future, the parameters could be defined by data classes introduced
in python 3.7."""


def layout_by_line_height(
    font_family=FONT_FAMILY,
    font_size=BASE_FONT_SIZE,
    line_height=BASE_LINE_HEIGHT,
    bgcolor=BG_COLOR,
    dark_text_color=DARK_TEXT_COLOR,
    light_text_color=LIGHT_TEXT_COLOR,
    n_canva=12,
    canva_width=600,
    left_margin=40,
    right_margin=80,
    title="title",
    subtitle="subtitle",
    ylabel="ylabel",
    xlabel="xlabel",
    **kwargs
):
    """This function returns a dictionary to be used in
    plotly.graph_objs.Figure(data=[...], layout=[...]). The axes labels and
    title are handled by annotations instead of the axes themselves in order
    to use horizontal labelling for the vertical axis as well as a title and
    a subtitle. The vertical dynamics is handled by a the lineheight.

    Args:
        font_family (str, default: FONT_FAMILY): font family
        font_size (int, default: BASE_FONT_SIZE): font size of labels
        line_height (int, default: BASE_LINE_HEIGHT)
        bgcolor (str, default: BG_COLOR): background color,
        dark_text_color (str, default: DARK_TEXT_COLOR): primary
            color of the text in hexcode
        light_text_color (str, defulat: LIGHT_TEXT_COLOR): secondary
            color of the text in hexcode
        n_canva (int, default: 12): the height of the canva in number
            of line height
        canva_width (float, defaults: 600): the plot (not chart) width
            in pixels, the chart width is
            canva_width + left_margin + right_margin
        left_margin (int, default: 80): the left margin in pixels
        right_margin (int, default: 80): the right margin in pixels

    Returns:
        dict: dictionary containing the parameters of the layout
    """
    # Height and width of the plot
    canva_height = n_canva * line_height

    padding = 0.5 * line_height

    # All positions are calculated in regard to the plot and
    # at the baseline
    parameters = dict(
        xref="paper", yref="paper", yanchor="bottom", align="left", showarrow=False
    )

    # X label position
    if xlabel:
        x_label_bottom = 0.5 * line_height
        x_label_height = 2.5 * line_height
    else:
        x_label_bottom = 0.5 * line_height
        x_label_height = 1.5 * line_height

    # Y label position on top of the plot
    if ylabel:
        y_label_bottom = padding
        y_label_height = 1.0 * line_height + 2.0 * padding
    else:
        y_label_bottom = padding
        y_label_height = 2.0 * padding

    # If there is a subtitle, the number of lines is calculated
    # from the number of <br>. Each line is treated independently.
    subtitle_labels = []
    if subtitle:
        lines = list(reversed(subtitle.split("<br>")))

        subtitle_height = line_height
        for n, line in enumerate(lines):
            subtitle_bottom = y_label_bottom + y_label_height + n * subtitle_height
            subtitle_labels.append(
                dict(
                    font=dict(size=0.889 * font_size, color=dark_text_color),
                    y=1 + subtitle_bottom / canva_height,
                    text=line,
                )
            )
    else:
        subtitle_bottom = y_label_bottom + y_label_height
        subtitle_height = 0

    # Title position
    title_bottom = subtitle_bottom + subtitle_height
    title_height = 1.5 * line_height

    # Margins are calculated from the extreme positions: the title and
    # the position of X label
    bottom_margin = x_label_bottom + x_label_height
    top_margin = title_bottom + title_height

    # The left margin should take into account the number
    # position of the labels
    left_position_min = 40  # px
    margin = dict(
        l=max(left_margin, left_position_min + 5),
        r=right_margin,
        t=top_margin,
        b=bottom_margin,
    )
    height = canva_height + margin["t"] + margin["b"]
    width = canva_width + margin["l"] + margin["r"]

    titles_left = -left_margin / canva_width

    labels = []
    if subtitle_labels:
        for s in subtitle_labels:
            labels.append(dict(x=titles_left, **s, **parameters))

    labels += [
        dict(
            **parameters,
            x=titles_left,
            xanchor="left",
            y=1 + title_bottom / canva_height,
            font=dict(size=1.424 * font_size, color=dark_text_color),
            text=title
        ),
        dict(
            **parameters,
            x=titles_left,
            xanchor="left",
            y=1 + y_label_bottom / canva_height,
            font=dict(size=font_size, color=dark_text_color),
            text=ylabel
        ),
        dict(
            **parameters,
            x=0.5,
            xanchor="center",
            y=-1.0 * x_label_height / canva_height,
            font=dict(size=font_size, color=light_text_color),
            text=xlabel
        ),
    ]

    layout = dict(
        width=width,
        height=height,
        font=dict(family=font_family),
        hoverlabel=dict(font=dict(family=font_family)),
        plot_bgcolor=bgcolor,
        paper_bgcolor=bgcolor,
        margin=margin,
        annotations=labels,
    )
    layout.update(kwargs)

    return layout


def axis_no_title(
    font_size=0.889 * BASE_FONT_SIZE,
    ticklen=5,
    showgrid=True,
    gridcolor=GRID_COLOR,
    gridwidth=2,
    zeroline=False,
    linewidth=6,
    linecolor=BG_COLOR,
    **kwargs
):
    """
    This function returns the parameters for an axis. The color of the axes are
    by default the background ones, being therefore “transparent”. Ticks are
    shown.

    Args:
        font_size (int, default: 0.889 * BASE_FONT_SIZE): font size
        ticklen (int, default: 5)
        showgrid (bool, default: True)
        gridcolor (str, default: GRID_COLOR)
        gridwidth (int, default: 2): manages the tick width too
        zeroline (bool, default: False): show line for the axis
        linewidth (int, default: 6),
        linecolor (str, default: BG_COLOR)

    Returns:
        dict: dictionary containing the parameters of the axis
    """
    d = dict(
        tickfont=dict(size=font_size),
        ticklen=ticklen,
        tickwidth=gridwidth,
        showgrid=showgrid,
        gridcolor=gridcolor,
        gridwidth=gridwidth,
        zeroline=zeroline,
        linewidth=linewidth,
        linecolor=linecolor,
    )
    d.update(kwargs)
    return d


def legend_dark(
    bgcolor=LEGEND_BG_COLOR,
    bordercolor=LEGEND_BORDER_COLOR,
    borderwidth=1,
    font_size=0.889 * BASE_FONT_SIZE,
    font_color=DARK_TEXT_COLOR,
    traceorder="normal",
    xanchor="left",
    x=1.05,
    yanchor="bottom",
    y=0.0,
    **kwargs
):
    """
    This function returns the parameters for the legend. The position is
    determined in regards of the plotting area (paper ref).

    Args:
        bgcolor (str, default: LEGEND_BG_COLOR)
        bordercolor (str, default: LEGEND_BORDER_COLOR)
        borderwidth (int, default: 1)
        font_size (int, default: 20)
        font_color (str, default: DARK_TEXT_COLOR)
        traceorder (str, default:normal)
        xanchor (str, default: left)
        x (float, default: 1.05): legend X position
        yanchor (str, default: bottom)
        y (float, default: 0.): legend Y position
    """
    legend = dict(
        traceorder=traceorder,
        bgcolor=bgcolor,
        bordercolor=bordercolor,
        borderwidth=borderwidth,
        font=dict(size=font_size, color=font_color),
        xanchor=xanchor,
        x=x,
        yanchor=yanchor,
        y=y,
    )
    legend.update(kwargs)
    return legend


def main():
    pass


if __name__ == "__main__":
    main()
