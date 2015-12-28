from __future__ import print_function, division

# from numpy import mean as np_mean, min as np_min
from numpy import array
from numpy.linalg import lstsq, LinAlgError


def time_series_detrend(ts, polynomial_order, verbosity=False):

    """
    Time series detrend using the user chosen polynomial order. Subroutine
    fits a ploynomial to the time series data and subtracts from the time
    series to zero out data.

    Parameters
    ----------
    ts : ndarray
        Nx2[3] array containing time series information.
    polynomial_order : int
        The order of the polynomial to be fit and subtracted.
    verbosity : bool
        Prints more information.

    Returns
    -------
    detrend_ts : ndarray
        Detrended `ts` timeseries
    """

    x = ts[:, 0]
    y = ts[:, 1]
    A = array([x**n for n in range(polynomial_order, -1, -1)]).T

    try:
        least_sq_fit = lstsq(A, y)
    except LinAlgError:
        print("Poor fit")
    else:
        p0 = least_sq_fit[0]

#
#
# def set_unitytime(ts1, ts2):
#
#     """
#         Subroutine - set_unitytime
#           Simply shifts both time series so that one starts at zero.
#     """
#
#     unitytime = min(np_min(ts1[:,0]), np_min(ts2[:,0]))
#     ts1[:,0] = ts1[:,0] - unitytime
#     ts2[:,0] = ts2[:,0] - unitytime
#
#     return ts1, ts2
#
#
# def chck_tserr(ts):
#
#     """
#         Subroutine - chck_tserr
#           Makes sure user has entered a properly formatted ts file.
#           Checks to see if input time series has a measurement error column - third
#           column of input file.
#     """
#
#     assert ((ts.shape[1] == 2) or (ts.shape[1] == 3)), "TS SHAPE ERROR"
#
#     if ts.shape[1] == 2:
#         ts_fill = zeros((ts.shape[0], 3))
#         ts_fill[:,0:2] = ts[:,0:2]
#
#         return ts_fill
#
#     else:
#
#         return ts
#
#
# def get_timeseries(infile1, infile2, vrbs, plyft):
#
#     """
#         Subroutine - get_timeseries
#           Takes the user specified filenames and runs tsdtrnd and set_unitytime.
#           Returns the prepared time series for DCF.
#     """
#
#     ts1_in = loadtxt(infile1, comments='#', delimiter=',')
#     ts2_in = loadtxt(infile2, comments='#', delimiter=',')
#
#     ts1 = chck_tserr(ts1_in)
#     ts2 = chck_tserr(ts2_in)
#
#     ts1, ts2 = set_unitytime(ts1, ts2)
#     ts1 = tsdtrnd(ts1, vrbs, plyft)
#     ts2 = tsdtrnd(ts2, vrbs, plyft)
#
#     return ts1, ts2
