def var_finder(prem_l: list):
    var_list = []

    for prem in prem_l:
        i = 0
        while i < len(prem):
            c = prem[i]

            if c.isspace():
                i += 1
                continue

            if c.isalnum() or c == '_':
                start = i

                while i < len(prem) and (prem[i].isalnum() or prem[i] == '_'):
                    i += 1
                
                name = prem[start:i]

                if name not in var_list:
                    var_list.append(name)

                continue

            i += 1

    return var_list