import matplotlib.pyplot as plt

plt.style.use('seaborn')


def find_bm(s, u, b):
    """
    returns bending moment at x=b due to unit Load at x=u on a span of length s
            Parameters:
                        s = span length
                        u = position of unit Load (from left end)
                        b = location at which bending moment is required (from left end)
            Returns:
                        bm = bending moment
    """
    if u < 0 or u > s:
        bm = 0
    elif 0 <= u < b:
        bm = u / s * (s - b)
    else:
        bm = (s - u) / s * b

    return bm


def find_sf(s, u, b):
    """
    returns shear force at x=b due to unit Load at x=u on a span of length s
            Parameters:
                        s = span length
                        u = position of unit Load (from left end)
                        b = location at which shear force is required (from left end)
            Returns:
                        sf = shear force
    """
    if u < 0 or u > s:
        sf = 0
    elif 0 <= u < b:
        sf = -u / s
    else:
        sf = (s - u) / s
    return sf


def il(span, at, of='bm', detail=25):
    """
    function for ild on a specific point
            Parameters:
                        span = Span length
                        at = point at which influence line is to be calculated
                        of = 'bm' bending moment(default) or 'sf' shear force
                        detail = number of inf_line points
            Returns:
                        inf_line(dict) = ild coordinates in the form of a dictionary {'x': [], 'y': []}
    """

    inf_line = {'x': [], 'y': []}
    if of == 'bm':
        for i in range(detail + 1):
            bm = find_bm(span, span / detail * i, at)
            inf_line['x'].append(span / detail * i)
            inf_line['y'].append(bm)
    if of == 'sf':
        for i in range(detail + 1):
            sf = find_sf(span, span / detail * i, at)
            inf_line['x'].append(span / detail * i)
            inf_line['y'].append(sf)
    return inf_line
