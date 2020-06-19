python early:
    from collections import MutableMapping, OrderedDict
    import copy
    class WillFlagBank(MutableMapping):
        def __init__(self, range_=None):
            self._range = range_
            self._flags = {}
            self._init_volatile_states()

        def _init_volatile_states(self):
            self._v_flag_names = WILL_FLAG_NAMES
            self._v_flag_names_reverse = {v: k for k, v in self._v_flag_names.items()}
            self._v_on_update_callback = {}
            self._v_sub_banks = OrderedDict()

        def __getstate__(self):
            # TODO iterate over __dict__
            return {'_flags': self._flags.copy(), '_range': copy.copy(self._range)}

        def __setstate__(self, state):
            self._flags = state.get('_flags', {})
            self._range = state.get('_range', None)
            self._init_volatile_states()

        def __repr__(self):
            return '{{{}}}'.format(', '.join('{}: {}'.format(repr(self._v_flag_names_reverse.get(k, k)), repr(v)) for k, v in self._flags.items()))

        def __str__(self):
            return self.__repr__()

        def __getitem__(self, key):
            '''
            Query the flag bank by either the index or pre-configured alias.
            All flags default to False for compatibility with int flags.
            Raises KeyError if attempting to use an undefined flag alias.
            '''
            addr = self._resolve_flag_addr(key)
            fb = self._resolve_bank_mapping(addr)
            if fb is self:
                return self._flags.get(addr, False)
                
            else:
                return fb[addr]

        def __setitem__(self, key, val):
            addr = self._resolve_flag_addr(key)
            fb = self._resolve_bank_mapping(addr)
            if fb is self:
                cb = self._v_on_update_callback.get(addr)
                if cb is not None:
                    cb(self._flags[addr], val)
                self._flags[addr] = val
            else:
                fb[addr] = val
            

        def __delitem__(self, key):
            addr = self._resolve_flag_addr(key)
            fb = self._resolve_bank_mapping(addr)
            if fb is self:
                cb = self._v_on_update_callback.get(addr)
                if cb is not None:
                    cb(self._flags[addr], False)
                del self._flags[addr]
            else:
                del fb[addr]

        def __iter__(self):
            return iter(self._flags)

        def __len__(self):
            return len(self._flags)

        def _resolve_flag_addr(self, key):
            if isinstance(key, int):
                return key
            else:
                return self._v_flag_names[key]

        def _resolve_bank_mapping(self, addr):
            if self._range is None or addr in self._range:
                return self
            for fb in self._v_sub_banks.values():
                if addr in fb.range_:
                    return fb
            raise KeyError('Unmapped address {}'.format(self.addr2name(addr)))

        @property
        def range_(self):
            return self._range

        def name2addr(self, flag_name):
            '''
            Resolve flag address by name. Raises KeyError when no matches found.
            '''
            return self._v_flag_names[flag_name]

        def addr2name(self, flag_addr):
            '''
            Resolve flag name by address. Returns the address when no matches found.
            '''
            return self._v_flag_names_reverse.get(flag_addr, flag_addr)

        def clear(self):
            '''
            Clear all flags within this flagbank.
            '''
            self._flags.clear()

        def on_update(self, key, callback):
            '''
            Register flagbank update callback. Note that the callback is only
            called when the flag belongs to this flagbank (i.e. it does not
            propagate through map_()s). Callback function should accept two
            parameters: one for the old value and one for the new value.
            '''
            self._v_on_update_callback[self._resolve_flag_addr(key)] = callback

        def off_update(self, key):
            '''
            Unregister a previously registered flagbank callback by flag key.
            '''
            del self._v_on_update_callback[self._resolve_flag_addr(key)]

        def map_(self, other):
            '''
            Map another flagbank to this one. Get/set/delete operations on the
            current flagbank will be forwarded to the corresponding flagbank
            when they are mapped to the current flagbank. Clear operations are
            not forwarded.

            Note that the mapping is volatile and must be redone before each
            access to make sure it is still valid.

            This can be used to implement indirect references where it is
            impossible to tell beforehand whether the referenced flag is
            persistent or not.
            '''
            if not isinstance(other, self.__class__):
                raise TypeError('Can only map to other flagbank instances')
            
            self._v_sub_banks[other.range_] = other
            return self

