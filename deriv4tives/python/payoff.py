import numpy as np
import matplotlib.pyplot as plt
import pdb


class deriv:

    def __init__(self):
        pass
    @staticmethod
    def call_long_payoff(S,k):
        return np.array([max(s - k, 0) for s in S])
    @staticmethod
    def call_short_payoff(S, k):
        return np.array([-max(s - k, 0) for s in S])
    @staticmethod
    def put_long_payoff(S, k):
        return np.array([max(k - s, 0) for s in S])
    @staticmethod
    def put_short_payoff(S, k):
        return np.array([-max(k - s, 0) for s in S])
    def futures_long(self,price,k):
        def payoff(S,k):
            return S-k
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price,payoff(price,k))
        plt.axhline(y=0,color='black',linestyle='-')
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/payoff/futures_long.png')
        plt.close()
    def futures_short(self,price,k):
        def payoff(S,k):
            return k-S
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price,payoff(price,k))
        plt.axhline(y=0, color='black', linestyle='-')
        plt.savefig('/Users/emmanueldjanga/deriv.com/img//payoff/futures_short.png')
        plt.close()
    def call_option_long(self,price,k):
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price,self.call_long_payoff(price,k))
        plt.axhline(y=0, color='black', linestyle='-')
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/payoff/call_option_long.png')
        plt.close()
    def call_option_short(self,price,k):
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price,self.call_short_payoff(price,k))
        plt.axhline(y=0, color='black', linestyle='-')
        plt.savefig('/Users/emmanueldjanga/deriv.com/img//payoff/call_option_short.png')
        plt.close()
    def put_option_long(self,price,k):
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price,self.put_long_payoff(price,k))
        plt.axhline(y=0, color='black', linestyle='-')
        plt.savefig('/Users/emmanueldjanga/deriv.com/img//payoff/put_option_long.png')
        plt.close()
    def put_option_short(self,price,k):
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price,self.put_short_payoff(price,k))
        plt.axhline(y=0, color='black', linestyle='-')
        plt.savefig('/Users/emmanueldjanga/deriv.com/img//payoff/put_option_short.png')
        plt.close()
    def put_call_parity(self,price,k):
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price,self.call_long_payoff(price,k),color='green',linewidth=3,label='long_call')
        plt.plot(price,self.put_short_payoff(price,k),color='blue',linestyle='-.',linewidth=3,label='short_put')
        plt.axhline(y=0,color='black',linestyle='-')
        plt.legend()
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/structure/put_call_parity_structure.png')
        plt.close()
        put_call_parity = self.call_long_payoff(price,k)+self.put_short_payoff(price,k)
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price,put_call_parity,color='orange',linestyle='--', linewidth=3,label='put-call parity')
        plt.legend()
        plt.axhline(y=0, color='black', linestyle='-')
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/payoff/put_call_parity_payoff.png')
        plt.close()
    def bull_spread(self,price,k1,k2):
        """
        Portfolio composed of one European option with a strike k1 and another with a strike k2 such that k2 > k1
        (Bullish)
        """
        call1 = self.call_long_payoff(price,k1)
        call2 = self.call_short_payoff(price,k2)
        plt.plot(self.call_long_payoff(price, k1), color='green', linewidth=3, label='long_call_low_strike')
        plt.plot(self.call_short_payoff(price, k2), color='blue', linestyle='-.', linewidth=3, label='short_call_high_strike')
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.axhline(y=0, color='black', linestyle='-')
        plt.legend()
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/structure/bull_spread_calls_structure.png')
        plt.close()
        put1 = self.put_long_payoff(price,k1)
        put2 = self.put_short_payoff(price,k2)

        plt.plot((self.put_long_payoff(price, k1)-1.30), color='green', linewidth=3, label='long_put_low_strike')
        plt.plot((self.put_short_payoff(price, k2)+3.2), color='blue', linestyle='-.', linewidth=3,
                 label='short_put_high_strike')
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.axhline(y=0, color='black', linestyle='-')
        plt.legend()
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/structure/bull_spread_puts_structure.png')
        plt.close()
        bull_spread_call = call1+call2
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price,bull_spread_call)
        plt.axhline(y=0, color='black', linestyle='-')
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/payoff/bull_spread_call.png')
        plt.close()
        bull_spread_put = (put1-1.2)+(put2+3)
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price, bull_spread_put)
        plt.axhline(y=0, color='black', linestyle='-')
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/payoff/bull_spread_put.png')
        plt.close()
    def bear_spread(self,price,k1,k2):
        """
        Portfolio composed of one European option with a strike k1 and another with a strike k2 such that k2 > k1
        (Bearish)
        """
        call1 = self.call_short_payoff(price,k1)
        call2 = self.call_long_payoff(price,k2)
        put1 = self.put_long_payoff(price,k1)
        put2 = self.put_short_payoff(price,k2)
        bear_spread_call = call2+call1
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price,bear_spread_call)
        plt.axhline(y=0, color='black', linestyle='-')
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/bear_spread_call.png')
        plt.close()
        bear_spread_put = put2+put1
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price, bear_spread_put)
        plt.axhline(y=0, color='black', linestyle='-')
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/bear_spread_put.png')
        plt.close()
    def box_spread(self,price,k1,k2):
        """
        Portfolio composed of one bull call spread with strikes k1 and k2 as well as a bear put spread with the same strikes.
        """
        bull_call_spread = self.call_option_long(price,k1)-self.call_option_short(price,k2)
        bear_call_spread = self.put_option_long(price, k2) - self.put_option_short(price, k1)
        box_spread = bull_call_spread + bear_call_spread
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.plot(price, box_spread)
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/box_spread.png')
        plt.close()
    def straddle(self,price,k1):
        """
        Portfolio composed of one long call and one long put on the same stock with same strike and maturity.
        """
        plt.plot(price,self.call_long_payoff(price,k1),color='green',linewidth=3,label='long_call')
        plt.plot(price,self.put_long_payoff(price,k1),color='blue',linestyle='-.',linewidth=3,label='long_put')
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.axhline(y=0,color='black',linestyle='-')
        plt.legend()
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/structure/straddle_structure.png')
        plt.close()
        straddle = self.call_long_payoff(price,k1)+self.put_long_payoff(price,k1)
        plt.plot(price,straddle,color='orange',linestyle='--', linewidth=3, label='straddle')
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.axhline(y=0, color='black',linestyle='-')
        plt.legend()
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/payoff/straddle_payoff.png')
        plt.close()
    def strip(self,price,k1):
        """
        Portfolio composed of one long call and 2 long puts on the same stock with same strike and maturity
        """
        plt.plot(price,self.call_long_payoff(price,k1),color='green',linewidth=3,label='long_call')
        plt.plot(price,2*self.put_long_payoff(price,k1),color='blue',linestyle='-.',linewidth=3,label='long_put')
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.axhline(y=0,color='black',linestyle='-')
        plt.legend()
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/structure/strip_structure.png')
        plt.close()
        strip = self.call_long_payoff(price,k1)+2*self.put_long_payoff(price,k1)
        plt.plot(price,strip,color='orange',linestyle='--', linewidth=3, label='strip')
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.axhline(y=0, color='black',linestyle='-')
        plt.legend()
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/payoff/strip_payoff.png')
        plt.close()
    def strap(self,price,k1):
        """
        Portfolio composed of two long calls and 1 long put on the same stock with same strike and maturity
        """
        plt.plot(price,2*self.call_long_payoff(price,k1),color='green',linewidth=3,label='long_call')
        plt.plot(price,self.put_long_payoff(price,k1),color='blue',linestyle='-.',linewidth=3,label='long_put')
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.axhline(y=0,color='black',linestyle='-')
        plt.legend()
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/structure/strap_structure.png')
        plt.close()
        strap = 2*self.call_long_payoff(price,k1)+self.put_long_payoff(price,k1)
        plt.plot(strap,color='orange',linestyle='--', linewidth=3, label='strap')
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.axhline(y=0, color='black',linestyle='-')
        plt.legend()
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/payoff/strap_payoff.png')
        plt.close()
    def strangle(self,price,k1,k2):
        """
        Portfolio composed of one long call and one long put on the same stock with different strike and same maturity
        """
        plt.plot(price,self.call_long_payoff(price,k1),color='green',linewidth=3,label='long_call')
        plt.plot(price,self.put_long_payoff(price,k2),color='blue',linestyle='-.',linewidth=3,label='long_put')
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.axhline(y=0,color='black',linestyle='-')
        plt.legend()
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/structure/strangle_structure.png')
        plt.close()
        strangle = self.call_long_payoff(price,k1)+self.put_long_payoff(price,k2)
        plt.plot(price,strangle,color='orange',linestyle='--', linewidth=3, label='strangle')
        plt.xlabel('Price')
        plt.ylabel('Payoff')
        plt.grid()
        plt.axhline(y=0, color='black',linestyle='-')
        plt.legend()
        plt.savefig('/Users/emmanueldjanga/deriv.com/img/payoff/strangle_payoff.png')
        plt.close()