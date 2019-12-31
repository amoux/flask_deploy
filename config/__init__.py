import config.settings
import os
import sys

# create settings object corresponding to specified enviroment
APP_ENV = os.environ.get("APP_ENV", "Dev")
_current = getattr(sys.modules["config.settings"], "{0}Config".format(APP_ENV))()

# copy attributes to the moduke for convenience
for atr in [f for f in dir(_current) if not '__' in f]:
    # enviroment can override anything
    val = os.environ.get(atr, getattr(_current, atr))
    setattr(sys.modules[__name__], atr, val)


def as_dict():
    res = {}
    for atr in [f for f in dir(config) if not "__" in f]:
        val = getattr(config, atr)
        res[atr] = val
    return res
