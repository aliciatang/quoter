#! /usr/local/bin/python3

def render(alerts):
    '''
    Renders the result of watch.
    '''
    html = "<html><body><ul>"
    for key, value in alerts.items():
        price = value['price']
        item = ""
        if 'factor' in value:
            price = price / value.get('multiplier', 1)
        if 'upper' in value and value['upper'] and price >= value['upper']:
            item = "<li>" + key + "($" + str(value['price']) + ")" + " exceeds upper limit($" + str(value['upper'])
        elif 'lower' in value and value['lower'] and price <= value['lower']:
            item = "<li>" + key + "($" + str(value['price']) + ")" + " falls below limit($" + str(value['lower'])
        elif not item and 'adjLower' in value and value['adjLower'] and price <= value['adjLower']:
            item = "<li>" + key + "($" + str(value['price']) + ")" + " falls below adjusted limit($" + str(value['adjLower'])
        elif not item and 'adjUpper' in value and value['adjUpper'] and price <= value['adjUpper']:
            item = "<li>" + key + "($" + str(value['price']) + ")" + " exceeds upper adjusted limit($" + str(value['adjUpper'])
        if 'factor' in value and value['factor'] is not None:
            item = item + " with factor:" + ("%.2f" % (value['factor'] * 100)) + "%"
        if item:
            item = item + ")</li>"
            html = html + item
    html = html + "</body></ul></html>"
    return html

