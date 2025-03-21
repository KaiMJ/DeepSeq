"""
INPUT: 
    - TICKER/USD
    - Scaling: OHLC[V] (“logarithmic” or “minmax” or “standard scaling”)
    - Timesteps: OHLC[V] (“1min”, “5min”, “15m”, …., “24hr”)
        1min: One of 1min / 5min / … / 4 hr/ daily
         - [O, H, C, L]
         [1min, 5min]: 
         - [O_1min, O_5min, H_1min, H_5min, C_1min, C_5min, L_1min, L_5min]
    - Indicators(moving_average=[“sma”, “ema”], rsi=True, MACD=True …)
        - Simple Moving Average
        - Exponential moving average
        - WaveTrend (wave_trend, stochastic_rsi, stochastic_rsi_diff, money_flow_index)
        - Look into code to determine Support / Resistance regions
        - Bollinger band
        - PPO
        - MACD
    For future:
        - Fast Fourier Transform
        - Converting time series to image domain via recurrence plot, Gramian Angular Field, and Markov Transition Field.
        - Volume Profile

OUTPUT: (could be combination)
    - OHLC[V]
    - T: next timesteps ([1, 5, 10], or 10)
    - Include indicators in outputs so something like [OHLCV, RSI, WAVE]
        - Probability that Price hits in next T timesteps
        - Certain strike price [X_1, X_2, X_3]
    - Hits [5EMA, 10EMA, 20EMA, 50EMA]
    - Probability that price closes lower/higher in T timesteps
"""
