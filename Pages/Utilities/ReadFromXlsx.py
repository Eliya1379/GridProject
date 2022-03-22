import xlrd as xlrd


def read_from_xlsx(path_file, sheet=0):
    workbook = xlrd.open_workbook(path_file)
    # Open the worksheet
    worksheet = workbook.sheet_by_index(sheet)
    title = []
    value = []
    d = worksheet.nrows
    n = worksheet.ncols
    # Iterate the rows and columns
    for i in range(worksheet.nrows):
        for j in range(worksheet.ncols):
            if i == 0:
                title.append(worksheet.cell_value(i, j))
            else:
                value.append(worksheet.cell_value(i, j))
                print(worksheet.cell_value(i, j), end='\t')

    final = []
    help = {}
    for i in range(len(value)):
        if i % len(title) == 0 and i != 0:
            final.append(help.copy())
            help.clear()
        help[title[i % len(title)]] = value[i]
    final.append(help.copy())
    return final
