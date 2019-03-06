import dplython
from dplython import Verb, DplyFrame, X, select, mutate, head
from readpy import *
import re

class separate(Verb):

    __name__ = "separate"

    def __call__(self, df):

        if len(self.args) >= 2:

            if not isinstance(self.args[0], dplython.later.Later):
                raise ValueError("First argument must be of the form \"X.column1, X.column2, ...\"")

            if not isinstance(self.args[1], list):
                raise ValueError("Second argument must be a list.")

            sp_col = self.args[0]._name
            sp_into = self.args[1]

        else:
            raise ValueError("You must provide at least two arguments, the key and the value.")

        if len(self.args) >= 3:
            if not isinstance(self.args[2], str):
                raise ValueError("Third argument should be the string separator.")

            sep = self.args[2]

        elif 'sep' in self.kwargs:
            sep = self.kwargs['sep']

        else:
            sep = r'[^\w]+'

        print(sep)

        splitcol = list(map(lambda x: re.compile(sep).split(x), df[sp_col]))

        for i, into_col in enumerate(sp_into):
            df[into_col] = [row[i] if len(row) > i else None for row in splitcol]

        columns = list(df.columns)

        reorder_columns = columns[:columns.index(sp_col)] + sp_into + columns[(columns.index(sp_col)+1):-len(into_col)-1]

        return df[reorder_columns]


    def __rrshift__(self, other):
        return self.__call__(DplyFrame(other.copy(deep=True)))


if __name__ == '__main__':

    mtcars = read_tsv('test/data/mtcars.tsv')
    mtcars = mtcars >> select(X.name, X.mpg, X.cyl)

    d = zip(map(str, mtcars['name']), map(str, mtcars['mpg']), map(str, mtcars['cyl']))
    d = ['|'.join(x) for x in d]
    mtcars['name'] = d

    mtcars = mtcars >> select(X.name)
    mtcars_clean = mtcars >> separate(X.name, ['name', 'mpg', 'cyl'], ' ')

    print(mtcars_clean >> head())