import pandas as pd


def out_excel(arr_obj: list, arr_id: list):
    arr_name = []
    arr_h_index = []
    arr_publication = []
    arr_total_time_cited = []
    for i in arr_obj:
        arr_name.append(i.name)
        arr_publication.append(i.publication)
        arr_total_time_cited.append(i.total_time_cited)
        arr_h_index.append(i.h_index)
    df = pd.DataFrame({
        "name": arr_name,
        "id": arr_id,
        "publication": arr_publication,
        "total time cited": arr_total_time_cited,
        "h index": arr_h_index
    })
    df.to_excel("Out.xlsx", index=False)
