def read_txt(path: str, mode: str) -> list:
    return_arr = []
    with open(path, mode) as f:
        data = f.readlines()
        for i in data:
            if i[-1] == "\n":
                return_arr.append(i[:-1])
            else:
                return_arr.append(i)
    return list(set(return_arr))
