from chartspy.svg import create_element


def create_bar_chart(svg, data, **options):

    v_margin = options.pop('v_margin', 20)
    h_margin = options.pop('h_margin', 20)
    bar_spacing = options.pop('bar_spacing', 20)
    fill_color = options.pop('fill_color', '#00000')

    max_value = max(*data, key=lambda x: x['value'])['value']
    work_width = svg.width - 2 * h_margin
    bar_width = (work_width-bar_spacing*(len(data) - 1))/len(data)
    work_height = svg.height - 2 * v_margin
    v_ratio = float(work_height) / max_value

    elms = [create_element(
        'rect',
        width=bar_width,
        height=d['value']*v_ratio,
        x=h_margin+i*(bar_width+bar_spacing),
        y=svg.height-v_margin-d['value']*v_ratio,
        fill=d.get('fill_color', fill_color)
    ) for i, d in enumerate(data)]
    svg.extend(elms)
    return svg

