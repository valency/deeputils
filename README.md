# Deepera Development Utils
A set of utilities for daily development.

## Common
```
from deeputils.common import *
```
- Log to console
```
log(msg, color="green")
```
- Search dictionary array by key value pair
```
dict_search(d, k, v)
```
Search dictionary array `d` with key `k` and value `v`, return index `i` if `d[i][k] == v` exists or `None` if not.
- Search tuples by key value pair
```
tuple_search(t, k, v)
```
Search tuples `t` with key `k` and value `v`, return tuple `e` if `e[k] == v` exists or `None` if not.
- Insert string between strings
```
string_insert(str1, str2, i)
```
Insert `str2` between `str1` split at position `i`.
- Format date / time
```
format_datetime(t)
format_date(t)
```
Format date / time in `%Y-%m-%d %H:%M:%S`, `%Y-%m-%d`, or `%H:%M:%S`.

## Serializers
Too complicated, see source code for details.
