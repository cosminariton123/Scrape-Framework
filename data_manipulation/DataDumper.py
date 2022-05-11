import pandas
import os

def save_results(results, result_path, input_file_name):

    succes = list()
    error = list()

    for key, value in results.items():
        if value == "Error":
            error.append(key)

        else:
            succes.append([key, value])

    success_write_file(succes, result_path, input_file_name)
    error_write_file(error, result_path, input_file_name)


def success_write_file(results, result_path, input_file_name):
    data_frame_ok = pandas.DataFrame(results)
    data_frame_ok.to_excel(os.path.join(result_path , "Succsess " + input_file_name))

def error_write_file(results, result_path, input_file_name):
    data_frame_er = pandas.DataFrame(results)
    data_frame_er.to_excel(os.path.join(result_path , "Error " + input_file_name))