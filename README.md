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