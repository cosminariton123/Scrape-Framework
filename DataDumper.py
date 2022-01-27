import pandas
import os

def save_results(results, result_path):

    succes = list()
    error = list()

    for key, value in results.items():
        if value == "NotFoundException":
            error.append(key)

        else:
            succes.append([key, value])

    success_write_file(succes, result_path)
    error_write_file(error, result_path)


def success_write_file(results, result_path):
    data_frame_ok = pandas.DataFrame(results)
    data_frame_ok.to_excel(os.path.join(result_path , "Succsess.xlsx"))

def error_write_file(results, result_path):
    data_frame_er = pandas.DataFrame(results)
    data_frame_er.to_excel(os.path.join(result_path , "Error.xlsx"))