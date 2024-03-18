import pandas as pd


class DataFrame:
    def __init__(self, data=None):
        self.df = pd.DataFrame(data)

    def display(self):
        print(self.df)

    def add_row(self, new_row):
        self.df = self.df.append(new_row, ignore_index=True)

    def delete_row(self, index):
        self.df = self.df.drop(index)
