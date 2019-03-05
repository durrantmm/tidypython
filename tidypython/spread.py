import dplython
from dplython import Verb, DplyFrame, X, select, mutate, head
from readpy import *


class spread(Verb):

    __name__ = "spread"

    def __call__(self, df):

        if len(self.args) >= 2:

            if not isinstance(self.args[0], dplython.later.Later) or \
                not isinstance(self.args[1], dplython.later.Later):

                raise ValueError("Arguments must be of the form \"X.column1, X.column2, ...\"")

            sp_key = self.args[0]._name
            sp_value = self.args[1]._name

        else:
            raise ValueError("You must provide at least two arguments, the key and the value.")


        multiindex = [s for s in df.columns if s != sp_key and s != sp_value]


        outdf = DplyFrame(df.set_index(multiindex).pivot(columns=sp_key, values=sp_value)).reset_index()
        outdf.columns.name = None

        return outdf


    def __rrshift__(self, other):
        return self.__call__(DplyFrame(other.copy(deep=True)))