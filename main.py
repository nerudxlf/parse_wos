from IO.out import out_excel
from IO.readTxt import read_txt
from parse.parseList import ParseList


def main():
    name_txt = "id.txt"
    mode = "r"
    chrome_driver_path = 'C:/programs/chrome/chromedriver'

    arr_id = read_txt(name_txt, mode)  # read id
    pars = ParseList(chrome_driver_path)  # create object
    arr_teacher = pars.parse(arr_id)  # get info
    out_excel(arr_teacher, arr_id)  # write info
