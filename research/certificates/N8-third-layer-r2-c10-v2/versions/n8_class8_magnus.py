#!/usr/bin/env python3
"""Same exact Magnus arithmetic, with balanced cached word expansion."""
from functools import lru_cache
from n8_fast_magnus import Magnus as SequentialMagnus
from n8_class5 import reduced

class Magnus(SequentialMagnus):
    def expansion(self,word):
        word=tuple(reduced(word))
        @lru_cache(maxsize=256)
        def expand(part):
            if len(part)<=16:
                return SequentialMagnus.expansion(self,part)
            cut=len(part)//2
            return self.mul(expand(part[:cut]),expand(part[cut:]))
        return expand(word)
