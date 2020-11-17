# datafunc

Python package of various functions for dict, list, and other data structures.

[![Actively Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://gitHub.com/TensorTom/datafunc/graphs/commit-activity)
[![MIT License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/datafunc/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/datafunc/)

### Changelog
- **11/17/2020 - 0.0.4** : Add missing type annotation. Generate docs.
- **11/17/2020 - 0.0.3** : Added `duplicate()` and `add_sibling()` methods. Added some missing type declarations.
- **11/15/2020 - 0.0.2** : Type annotations & minor refactors.
- **11/15/2020 - 0.0.1** : Initial methods.

## Reference

#### flatten

```python
flatten(var: object) -> Data
```

Traverse a dict-like object and return a new one with all
the same values but only one layer deep.

**Arguments**:

- `var`: Dict-like variable to flatten.

**Returns**:

A mo-dots dict-like Data object.

<a name="datafunc.iterable"></a>
#### iterable

```python
iterable(var: Any) -> Boolean
```

Determine whether or not the input variable is iterable.

**Arguments**:

- `var`: Any

**Returns**:

Boolean

<a name="datafunc.listlike"></a>
#### listlike

```python
listlike(var: Any) -> Boolean
```

Determine if the input variable is list-like
(Not a str, not dict-like, but is iterable)

**Arguments**:

- `var`: Any

**Returns**:

Boolean

<a name="datafunc.mo_dotian"></a>
#### mo\_dotian

```python
mo_dotian(var: Any) -> Boolean
```

Determine whether or not the input var is a mo-dots type.

**Arguments**:

- `var`: Any

**Returns**:

Boolean

<a name="datafunc.apply_if"></a>
#### apply\_if

```python
apply_if(func_to_apply: Callable, var: Any, condition: Callable, else_func: Callable = do_nothing) -> Any
```

Apply func_to_apply() to var if condiction() else apply else_func()

**Arguments**:

- `func_to_apply`: Callable to pass var to if condition(var) return true
- `var`: Variable to test against condition and return through func_to_apply() or else_func()
- `condition`: Callable to test var against. Should return a Boolean.
- `else_func`: Callable to return var through if condition(var) returns False.

**Returns**:

func_to_apply(var) if condition(var) returns True, otherwise else_func(var)

<a name="datafunc.dictlike"></a>
#### dictlike

```python
dictlike(var: Any) -> Boolean
```

Determine whether or not var is dict-like (Can
contain dict-like items).

**Arguments**:

- `var`: Any variable to check

**Returns**:

Boolean

<a name="datafunc.nestable"></a>
#### nestable

```python
nestable(var: Any) -> Boolean
```

Will return True if input var is either list-like or
dict-like.

**Arguments**:

- `var`: Any input variable.

**Returns**:

Boolean

<a name="datafunc.jsonify_nestable_vals"></a>
#### jsonify\_nestable\_vals

```python
jsonify_nestable_vals(obj: object) -> Data
```

Convert any nestable (Dict-like or list-like) to a dict-like mo-dots
Data object of obj's values as JSON strings.

**Arguments**:

- `obj`: Any nestable variable.

**Returns**:

A dict-like mo-dots Data object of obj's values as JSON strings.

<a name="datafunc.compare"></a>
#### compare

```python
compare(d1: object, d2: object) -> Data
```

Compare dict-like variable d1 to dict-like variable d2
and return a dict-like mo-dots Data object of what's
been added, removed, modified, or remained equal in d2

**Arguments**:

- `d1`: Dict-like variable as the base variable.
- `d2`: Dict-like variable to compare/contrast to d1

**Returns**:

Dict-like mo-dots Data object of differences between d1 and d2.

<a name="datafunc.function_of"></a>
#### function\_of

```python
function_of(func: Callable, func_names: Tuple) -> Boolean
```

Determine whether or not a function's (func) name exists in tuple of strings
(func_names).

**Arguments**:

- `func`: The callable function to test.
- `func_names`: Tuple of function names as strings ("func1", "func2", "func3,)

**Returns**:

Boolean True (func is of func_names) or False (func is not of func_names)

<a name="datafunc.basevals"></a>
#### basevals

```python
basevals(var: object, *attrs) -> Any
```

This method receives a dict and list of attributes
to return the innermost value of the given dict-like
var. This function seems stupid and I don't recall
what it was for.

<a name="datafunc.vivify"></a>
#### vivify

```python
vivify(var: object, *attrs: str)
```

Adds the last attr variable passed to the dict-like "var"
in the hierarchy mentioned via the prior *attrs
For ex:
vivify(animals, "cat", "leg","fingers", 4) is equivalent to animals["cat"]["leg"]["fingers"]=4
This method creates necessary objects until it reaches the final depth
This behaviour is also known as autovivification and plenty of implementation are around
This implementation addresses the corner case of replacing existing primitives
https://gist.github.com/hrldcpr/2012250#gistcomment-1779319

<a name="datafunc.duplicate"></a>
#### duplicate

```python
duplicate(data: object) -> object
```

Convenience method for copy.deepcopy()

**Arguments**:

- `data`: Any dict, mo-dots, or dotty object.

**Returns**:

A deep copy of the data.

<a name="datafunc.add_sibling"></a>
#### add\_sibling

```python
add_sibling(data: object, node_path: List, new_key: str, new_data: Any, _i: int = 0)
```

Traversal-safe method to add a siblings data node.

**Arguments**:

- `data`: The data object you're traversing.
- `node_path`: List of path segments pointing to the node you're creating a
sibling of. Same as node_path of traverse()
- `new_key`: The sibling key to create.
- `new_data`: The new data to be stored at the key.
- `_i`: Depth of node_path iterator.