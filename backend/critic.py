def critic_ident(ans_list:list):
    critic_index_list = []
    for i in range(len(ans_list)):
        aborted = False
        for j in range(len(ans_list[i]) - 1):
            if ans_list[i][j] == False:
                aborted = True
                break
        if not aborted:
            critic_index_list.append(i)
    return critic_index_list

def invalid_ident(critic_index_list:list, ans_list:list):
    invalid_index_list = []
    for i in critic_index_list:
        if ans_list[i][-1] is False:
            invalid_index_list.append(i)
    return invalid_index_list