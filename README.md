# `tidypython` - A simple python package designed to syntactically mimic the tidyr package in R. 


Install the package with pip:

    pip install tidypython
    
Load the functions into your script with:

    from tidypython import *
    
You will then have access to the functions:

    gather(*args, **kwargs)
    spread(*args, **kwargs)
    separate(*args, **kwargs)

The syntax is designed to resemble that of the R package `tidyr` as closely as possible. 
All of the functionality is not yet fully implemented, but the basics are there.

All of these functions are designed to work with the `dplython` package operators `>>`.


This package is currently in development, please visit the github page if you'd like to contribute: 
https://github.com/durrantmm/tidypython

# Examples

First, import the dplython package:

    from dplython import *
    
Make sure that your dataframe is a DplyFrame object. You can make sure it is by calling:

    df = DplyFrame(df)

Or you can read in your file directly using the `readpy` package:

    from readpy import *
    df = read_tsv("myfile.tsv")


### `gather()`

The `gather()` command implements the pandas `melt()` function using the `tidyr` syntax.

You can use the `gather` command as:

    df >> gather(X.key, X.value, X.column1, X.column2...)

`X.key` and `X.value` are used to determine the new names of the key and value columns that will be created.

By default, this will use column1, column2, and all other subsequent columns to determine the keys and the values. All
unspecified columns will be used simply as an index. Alternatively, you can use the syntax

    df >> gather(X.key, X.value, X.column1, X.column2, exclude=True)
    
Which will make column1, and column2 the index, and all other unspecified columns will be used for the key and value 
columns.

Using the `mtcars` data as an example:

    >>> mtcars = read_tsv('mtcars.tsv')
    >>> print(mtcars >> head())
                    name   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
    0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
    1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
    2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
    3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
    4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3     2


Lets first gather all of the columns of interest by inclusion:

    >>> mtcars_gathered_inclusion = mtcars >> \
    ... gather(X.info, X.val, X.mpg, X.cyl, X.disp, X.hp, X.drat, X.wt, X.qsec, X.vs, X.am, X.gear, X.carb))
    >>> print(mtcars_gathered_inclusion >> head())
                    name info   val
    0          Mazda RX4  mpg  21.0
    1      Mazda RX4 Wag  mpg  21.0
    2         Datsun 710  mpg  22.8
    3     Hornet 4 Drive  mpg  21.4
    4  Hornet Sportabout  mpg  18.7
    >>> print(mtcars_gathered_inclusion >> tail())
                   name  info  val
    347    Lotus Europa  carb  2.0
    348  Ford Pantera L  carb  4.0
    349    Ferrari Dino  carb  6.0
    350   Maserati Bora  carb  8.0
    351      Volvo 142E  carb  2.0

Now we can do it by exclusion, which is much shorter in this case:

    >>> mtcars_gathered_exclusion = mtcars >> \
    ... gather(X.info, X.val, X.name, exclude=True))
    >>> print(mtcars_gathered_exclusion >> head())
                    name info   val
    0          Mazda RX4  mpg  21.0
    1      Mazda RX4 Wag  mpg  21.0
    2         Datsun 710  mpg  22.8
    3     Hornet 4 Drive  mpg  21.4
    4  Hornet Sportabout  mpg  18.7
    >>> print(mtcars_gathered_exclusion >> tail())
                   name  info  val
    347    Lotus Europa  carb  2.0
    348  Ford Pantera L  carb  4.0
    349    Ferrari Dino  carb  6.0
    350   Maserati Bora  carb  8.0
    351      Volvo 142E  carb  2.0

You can see that it functions very much in the same manner as the `tidyr::gather` function.
    
### `spread()`

The `spread()` command implements the pandas `pivot()` function using the `tidyr` syntax.

You can use the `spread` command as:

    df >> spread(X.key, X.value)

`X.key` and `X.value` are used to specify the existing columns that are pivoted, and all other unused columns are
assumed to be the index.
    
Which will make column1, and column2 the index, and all other unspecified columns will be used for the key and value 
columns.

Using the `mtcars` data as an example:

    >>> mtcars = read_tsv('mtcars.tsv')
    >>> print(mtcars >> head())
                    name   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
    0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
    1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
    2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
    3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
    4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3     2


Lets first gather all of the columns of interest by exclusion:

    >>> mtcars_gathered_exclusion = mtcars >> \
    ... gather(X.info, X.val, X.name, exclude=True))
    >>> print(mtcars_gathered_exclusion >> head())
                    name info   val
    0          Mazda RX4  mpg  21.0
    1      Mazda RX4 Wag  mpg  21.0
    2         Datsun 710  mpg  22.8
    3     Hornet 4 Drive  mpg  21.4
    4  Hornet Sportabout  mpg  18.7
    
We can then pivot the `info` and `val` columns out by using the `spread` function:
    
    >>> print(mtcars_gathered_exclusion >> spread(X.info, X.val) >> head())
                     name   mpg  cyl   disp     hp  drat     wt   qsec   vs   am  gear   carb
    0         AMC Javelin  15.2  8.0  304.0  150.0  3.15  3.435  17.30  0.0  0.0   3.0    2.0
    1  Cadillac Fleetwood  10.4  8.0  472.0  205.0  2.93  5.250  17.98  0.0  0.0   3.0    4.0
    2          Camaro Z28  13.3  8.0  350.0  245.0  3.73  3.840  15.41  0.0  0.0   3.0    4.0
    3   Chrysler Imperial  14.7  8.0  440.0  230.0  3.23  5.345  17.42  0.0  0.0   3.0    4.0
    4          Datsun 710  22.8  4.0  108.0   93.0  3.85  2.320  18.61  1.0  1.0   4.0    1.0


You can see that it functions very much in the same manner as the `tidyr::gather` function. As currently implemented,
the order of the columns will be preserved in python >= 3.6, but the order of the index will not.


### `separate()`

The `separate()` command doesn't have a direct parallel in other python packages that I am aware of.

You can use the `separate` command as:

    df >> separate(X.column, into, sep=myseperator)

`X.column` is the column that you want to split, `into` is a list of the new column names for the split columns,
and `sep` is a regex-expression used to split the X.column. By default, this will split by `[^\w]+`.
    

Let's say that our mtcars dataframe only included a `name`, `mpg`, and `cyl` joined in a single column by the 
separator '|':


    >>> print(mtcars_messy >> head())
                           name  
    0          Mazda RX4|21.0|6
    1       Mazda RX4 Wag|1.0|6
    2         Datsun 710|22.8|4
    3     Hornet 4 Drive|21.4|6
    4  Hornet Sportabout|18.7|8

You could seperate this column into three columns using the command:

    >>> mtcars_clean = mtcars_messy >> separate(X.name, ['name', 'mpg', 'cyl'], sep='\|')
    >>> print(mtcars_clean >> head())
                    name   mpg cyl
    0          Mazda RX4  21.0   6
    1      Mazda RX4 Wag  21.0   6
    2         Datsun 710  22.8   4
    3     Hornet 4 Drive  21.4   6
    4  Hornet Sportabout  18.7   8

Note that all of the columns remain strings after separating. It will also not give any warnings if the number 
of columns specified does not match the number of strings after splitting.