rows = int(input("Hvor mange rader?")) + 1
columns = int(input("Hvor mange kolonner?")) + 1

highlight_row_start = int(input("Første markerte rad"))
highlight_row_stop = int(input("Siste markerte rad"))
highlight_column_start = int(input("Første markerte kolonne"))
highlight_column_stop = int(input("Siste markerte kolonne"))

highlight_coordinates = [highlight_row_start, highlight_row_stop,
                         highlight_column_start, highlight_column_stop]

html_table = ['\n\n<table style="border-collapse: collapse;">\n<tbody>',
              '</tbody>\n</table>']

highlight_green = '#237447'
header_background = ' background-color: #f5f5f5;'
default_background = ' background-color: #ffffff;'
highlight_background = ' background-color: #c7c7c7;'
header_highlight_background = ' background-color: #DAD8D6;'
header_color = ' color: #5e5e5e;'
header_font_weight = ' font-weight: bold;'
header_highlight_color = f' color: {highlight_green};'
header_border = ' border: thin solid #dfdfdf;'
highlight_border = ' border: thin solid #A6A6A6;'
default_border = ' border: thin solid #D4D4D4;'
header_highlight_border = 'border: thin solid #BFBFBF;'
header_edge_border_value = ' thin solid #BBBBBB;'
highlight_edge_border_value = f' 2px solid {highlight_green};'
header_highlight_edge_border_value = f'2px solid {highlight_green};'
header_height = ' height: 25px;'
default_height = ' height: 30px;'
span_style = ' text-align: center; display: block;'
span_header_style = f'{span_style} font-family: sans-serif;'


def add_top_row(cols, row, highlight_coordinates):
    row.append(f'<tr style="{header_height}">\n')
    highlight_addon = f' border-right: {header_edge_border_value}' if highlight_coordinates[2] == 1 else ''
    highlight_addon += f' border-bottom: {header_edge_border_value}' if highlight_coordinates[0] == 1 else ''
    row.append(
        f'<td style="{header_background}{header_border}{highlight_addon}">&nbsp;</td>\n')
    for i in range(1, cols):
        highlighted = i >= highlight_coordinates[2] and i <= highlight_coordinates[3]
        cell = format_header_cell(highlighted, highlight_coordinates[2]-1 == i, i, 0)
        row.append(cell)
    row.append('</tr>\n')
    return row


def add_other_row(cols, row, row_nr, highlight_coordinates):
    row.append(f'<tr style="{default_height}">\n')
    highlighted = row_nr >= highlight_coordinates[0] and row_nr <= highlight_coordinates[1]
    cell = format_header_cell(highlighted, highlight_coordinates[0]-1 == row_nr, 0, row_nr)
    row.append(cell)
    highlight_row = True if row_nr >= highlight_coordinates[0] and row_nr <= highlight_coordinates[1] else False
    for i in range(1, cols):
        highlight_col = True if i >= highlight_coordinates[2] and i <= highlight_coordinates[3] else False
        row_str = '<td style="'
        if(highlight_row and highlight_col and not (row_nr == highlight_coordinates[0] and i == highlight_coordinates[2])):
            row_str += highlight_background
        else:
            row_str += default_background
        row_str += highlight_border if highlight_row and highlight_col else default_border
        if (row_nr == highlight_coordinates[0] and highlight_col):
            row_str += f' border-top: {highlight_edge_border_value}'
        if (row_nr == highlight_coordinates[1] and highlight_col):
            row_str += f' border-bottom: {highlight_edge_border_value}'
        if (i == highlight_coordinates[2] and highlight_row):
            row_str += f' border-left: {highlight_edge_border_value}'
        if (i == highlight_coordinates[3] and highlight_row):
            row_str += f' border-right: {highlight_edge_border_value}'
        row_str += f'"><span style="{span_style}"></span></td>\n'
        row.append(row_str)
    row.append('</tr>\n')
    return row


def list_to_string(table_list, table_str):
    for entry in table_list:
        if (isinstance(entry, list)):
            table_str += list_to_string(entry, '')
        else:
            table_str += entry
    return table_str

def format_header_cell(highlighted, before_highlighted, x, y):
    cell = f'<td style="'
    cell += header_highlight_background if highlighted else header_background
    cell += header_highlight_border if highlighted else header_border
    cell += ' border-bottom:' if y == 0 else ' border-right:'
    cell += header_highlight_edge_border_value if highlighted else header_edge_border_value
    if (before_highlighted):
        cell += ' border-'
        if (y == 0):
            cell += 'right: '
        else:
            cell += 'bottom: '
        cell+= header_edge_border_value
    cell += f'"><span style="{span_header_style}'
    cell += header_highlight_color if highlighted else header_color
    if (highlighted): 
        cell += header_font_weight
    if (y == 0):
        letter = chr(64+x)
        cell += f'">{letter}</span></td>\n'
    else:
        number = y
        cell += f'">{number}</span></td>\n'
    return cell



html_table.insert(1, add_top_row(columns, [], highlight_coordinates))
for i in range(1, rows):
    html_table.insert(-1, add_other_row(columns, [], i, highlight_coordinates))
print(list_to_string(html_table, ''))
