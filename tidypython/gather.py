import dplython
from dplython import Verb, DplyFrame, X
from readpy import *


class gather(Verb):

    __name__ = 'gather'

    def __call__(self, df):

        if len(self.args) >= 2:

            if not isinstance(self.args[0], dplython.later.Later) or \
                not isinstance(self.args[1], dplython.later.Later):

                raise ValueError("Arguments must be of the form \"X.column1, X.column2, ...\"")

            sp_key = self.args[0]._name
            sp_value = self.args[1]._name

        else:

            raise ValueError("You must provide at least two arguments, the key and the value.")



        all_id_cols = []
        all_value_cols = list(df.columns)

        if len(self.args) > 2:

            if 'exclude' in self.kwargs and self.kwargs['exclude'] == True:

                for arg in self.args[2:]:

                    if not isinstance(arg, dplython.later.Later):
                        raise ValueError("Arguments must be of the form \"X.column1, X.column2, ...\"")

                    all_id_cols.append(arg._name)
                    all_value_cols.remove(arg._name)


            else:

                all_id_cols = list(df.columns)
                all_value_cols = []

                for arg in self.args[2:]:

                    if not isinstance(arg, dplython.later.Later):
                        raise ValueError("Arguments must be of the form \"X.column1, X.column2, ...\"")

                    all_id_cols.remove(arg._name)
                    all_value_cols.append(arg._name)

        outdf = DplyFrame(df.melt(id_vars=all_id_cols, value_vars=all_value_cols))


        cols = list(outdf.columns)
        cols[-2:] = sp_key, sp_value
        outdf.columns = cols

        return outdf


    def __rrshift__(self, other):
        return self.__call__(DplyFrame(other.copy(deep=True)))


if __name__ == '__main__':

    mtcars = read_tsv('test/data/mtcars.tsv')
    print(mtcars >> gather(X.info, X.val, X.mpg, X.cyl, X.disp, X.hp, X.drat, X.wt, X.qsec, X.vs, X.am, X.gear, X.carb))