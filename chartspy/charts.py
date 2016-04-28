from chartspy.helpers import PositionDistance
from chartspy.svg import create_element


def create_bar_chart(svg, data, margin=20, bar_spacing=20, fill_color='url(#gradient1)'):
    """
    Generate a bar chart in the svg

    :param svg: the container for the chart
    :param data: the data (e.g. [{'value': 3, 'label': 'sales', 'fill_color':'#ff0000'},{..}])
    :param margin: margin tuple like CSS (e.g. (10, 15, 5, 0))
    :param bar_spacing: bar_spacing the distance between bars
    :param fill_color: fill_color the default color for a bar
    :return:
    """
    margin = PositionDistance(margin)

    # Calculate the maximum value
    max_value = max(*data, key=lambda x: x['value'])['value']

    total_spacing = bar_spacing * (len(data) - 1)
    bar_width = (svg.width - margin.hor() - total_spacing) / len(data)
    height_ratio = float(svg.height - margin.ver()) / max_value
    chart_bottom = svg.height - margin.bottom

    # Create the geometry group for the bars
    g = create_element('g', transform='translate({} {})'.format(
        margin.left,
        chart_bottom
    ))

    # Create the SVG elements for the bars
    elms = [create_element(
        'rect',
        width=bar_width,
        height=d['value'] * height_ratio,
        x=i * (bar_width + bar_spacing),
        y=- d['value'] * height_ratio,
        fill=d.get('fill_color', fill_color)
    ) for i, d in enumerate(data)]

    g.extend(elms)
    svg.append(g)
    return svg
