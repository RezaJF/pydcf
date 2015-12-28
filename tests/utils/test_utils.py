from pytest import fixture

from numpy import array

from utils.utils import time_series_detrend

class TestTimeSeriesDetrend(object):

    @fixture
    def test_ts(self):
        x = array([0, 1, 2, 3, 4])
        y = array([-1, 0.2, 0.9, 2.1, 2.8])
        return array([x, y]).T

    def test_polynomial_fit(self, test_ts):
        import ipdb; ipdb.set_trace()
        assert True

    def test_thing_again(self):
        assert False
