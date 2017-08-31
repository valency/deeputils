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
Format date / time in `%Y-%m-%d %H:%M:%S`.
## Exceptions
Contains a list of Django exceptions, including:
- `400` / `BadRequest`: This field may not be empty.
- `401` / `Unauthorized`: The requested user is not authorized.
- `403` / `Forbidden`: The requested user is not authorized to access certain API.
- `404` / `NotFound`: Not found.
- `406` / `NotAcceptable`: This field value is not acceptable according to its definition.
- `409` / `Conflict`: This field value is unique but already exists.
```
from deeputils.exceptions import *
raise BadRequest({'detail': 'It is a bad request.'})
```
## Serializers
Too complicated, see source code for details.
