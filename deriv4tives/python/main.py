import os
from importlib import reload
import payoff
import numpy as np
reload(payoff)


if __name__ == "__main__":
    if os.getcwd() == '/Users/emmanueldjanga/deriv.com/python':
        deriv_obj = payoff.deriv()
        price = np.linspace(90,140,51)
        k1 = 95
        k2 = 110
        #deriv_obj.futures_long(price,k1)
        #deriv_obj.futures_short(price,k1)
        #deriv_obj.call_option_long(price,k1)
        #deriv_obj.call_option_short(price, k1)
        #deriv_obj.put_option_long(price,k1)
        #deriv_obj.put_option_short(price,k1)
        #deriv_obj.put_call_parity(price,k1)
        #deriv_obj.bull_spread(price,k1,k2)
        #deriv_obj.bear_spread(price,k1,k2)
        #deriv_obj.straddle(price,k2)
        deriv_obj.strip(price,k1)
        #deriv_obj.strap(price,k1)
        #deriv_obj.strangle(price,k1,k2)
