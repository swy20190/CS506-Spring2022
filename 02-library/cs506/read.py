def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    with open(csv_file_path) as f:
        raw = f.readlines()

    for raw_line in raw:
        raw_list = raw_line.strip().split(',')
        res_list = []
        for raw_v in raw_list:
            try:
                res_list.append(int(raw_v))
            except Exception:
                res_list.append(raw_v[1:-1])

        res.append(res_list)

    return res
