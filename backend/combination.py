def comb_generator(var_list:list, comb_list: list = None, val_dict:dict = None):
    if val_dict is None or comb_list is None:
        val_dict = {}
        comb_list = []

    if len(var_list) == 0:
        comb_list.append(val_dict)
        return
    
    current_value = var_list[0]
    rem_vars = var_list[1:]
    
    val_dict[current_value] = True
    comb_generator(rem_vars, comb_list, val_dict.copy())

    val_dict[current_value] = False
    comb_generator(rem_vars, comb_list, val_dict.copy())

    return comb_list