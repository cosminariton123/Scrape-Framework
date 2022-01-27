import pandas

def read_items(filepath):
    df = pandas.read_excel(filepath, sheet_name= "Sheet1")
    searched_items = df["Stringuri de cautat"]
    searched_items = [str(elem) for elem in searched_items]
    return searched_items