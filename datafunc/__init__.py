from mo_dots import Data, DataObject, FlatList, from_data, to_data, literal_field
from dotty_dict import Dotty, dotty
import json
from traversy import traverse
from typing import Dict, List, Literal, Tuple, Union, Any, Callable, Set
import copy

Boolean = Literal[True, False]


def do_nothing(var: Any) -> Any:
	"""
	Does nothing but return what it's given. Mainly for
	default callbacks.
	:param var: Any
	:return: Returns var that was given.
	"""
	return var


def flatten(var: object) -> Data:
	"""
	Traverse a dict-like object and return a new one with all
	the same values but only one layer deep.
	:param var: Dict-like variable to flatten.
	:return: A mo-dots dict-like Data object.
	"""
	result = Data()
	for v in traverse(var, output_formatter=to_data):
		result[literal_field(v.path_str)] = v.value
	return result


def iterable(var: Any) -> Boolean:
	"""
	Determine whether or not the input variable is iterable.
	:param var: Any
	:return: Boolean
	"""
	try:
		iter(var)
		return True
	except TypeError:
		return False


def listlike(var: Any) -> Boolean:
	"""
	Determine if the input variable is list-like
	(Not a str, not dict-like, but is iterable)
	:param var: Any
	:return: Boolean
	"""
	return not isinstance(var, str) and not dictlike(var) and iterable(var)


def mo_dotian(var: Any) -> Boolean:
	"""
	Determine whether or not the input var is a mo-dots type.
	:param var: Any
	:return: Boolean
	"""
	return isinstance(var, (Data, DataObject, FlatList))


def apply_if(func_to_apply: Callable, var: Any, condition: Callable, else_func=do_nothing) -> Any:
	"""
	Apply func_to_apply() to var if condiction() else apply else_func()
	:param func_to_apply: Callable to pass var to if condition(var) return true
	:param var: Variable to test against condition and return through func_to_apply() or else_func()
	:param condition: Callable to test var against. Should return a Boolean.
	:param else_func: Callable to return var through if condition(var) returns False.
	:return: func_to_apply(var) if condition(var) returns True, otherwise else_func(var)
	"""
	return func_to_apply(var) if condition(var) else else_func(var)


def dictlike(var: Any) -> Boolean:
	"""
	Determine whether or not var is dict-like (Can
	contain dict-like items).
	:param var: Any variable to check
	:return: Boolean
	"""
	try:
		var.items()
		return True
	except (TypeError, AttributeError):
		return False


def nestable(var: Any) -> Boolean:
	"""
	Will return True if input var is either list-like or
	dict-like.
	:param var: Any input variable.
	:return: Boolean
	"""
	return dictlike(var) or listlike(var)


def jsonify_nestable_vals(obj: object) -> Data:
	"""
	Convert any nestable (Dict-like or list-like) to a dict-like mo-dots
	Data object of obj's values as JSON strings.
	:param obj: Any nestable variable.
	:return: A dict-like mo-dots Data object of obj's values as JSON strings.
	"""
	return to_data({k: json.dumps(json.dumps(v, default=from_data)) if nestable(v) else v for k, v in obj.items()})


def compare(d1: object, d2: object) -> Data:
	"""
	Compare dict-like variable d1 to dict-like variable d2
	and return a dict-like mo-dots Data object of what's
	been added, removed, modified, or remained equal in d2
	:param d1: Dict-like variable as the base variable.
	:param d2: Dict-like variable to compare/contrast to d1
	:return: Dict-like mo-dots Data object of differences between d1 and d2.
	"""
	d1_keys: Set = set(d1.keys())
	d2_keys: Set = set(d2.keys())
	shared_keys: Set = d1_keys.intersection(d2_keys)
	added: Set = d1_keys - d2_keys
	removed: Set = d2_keys - d1_keys
	modified: Dict = {o: (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
	same: Set = set(o for o in shared_keys if d1[o] == d2[o])
	return to_data({'add': added, 'rm': removed, 'mod': modified, 'eq': same})


def function_of(func: Callable, func_names: Tuple) -> Boolean:
	"""
	Determine whether or not a function's (func) name exists in tuple of strings
	(func_names).
	:param func: The callable function to test.
	:param func_names: Tuple of function names as strings ("func1", "func2", "func3,)
	:return: Boolean True (func is of func_names) or False (func is not of func_names)
	"""
	return hasattr(func, '__call__') and func.__name__ in func_names


def basevals(var: object, *attrs) -> Any:
	"""
	This method receives a dict and list of attributes
	to return the innermost value of the given dict-like
	var. This function seems stupid and I don't recall
	what it was for.
	"""
	try:
		for at in attrs:
			var = var[at]
		return var
	except(KeyError, TypeError):
		return None


def vivify(var: object, *attrs: str):
	"""
	Adds the last attr variable passed to the dict-like "var"
	in the hierarchy mentioned via the prior *attrs
	For ex:
	vivify(animals, "cat", "leg","fingers", 4) is equivalent to animals["cat"]["leg"]["fingers"]=4
	This method creates necessary objects until it reaches the final depth
	This behaviour is also known as autovivification and plenty of implementation are around
	This implementation addresses the corner case of replacing existing primitives
	https://gist.github.com/hrldcpr/2012250#gistcomment-1779319
	"""
	for attr in basevals[:-2]:
		if type(var.get(attr)) not in (dict, Data, Dotty, DataObject):
			var[attr] = {}
		var = var[attr]
	var[attrs[-2]] = attrs[-1]


def duplicate(data: object) -> object:
	"""
	Convenience method for copy.deepcopy()
	:param data: Any dict, mo-dots, or dotty object.
	:return: A deep copy of the data.
	"""
	return copy.deepcopy(data)


def add_sibling(data: object, node_path: List, new_key: str, new_data: Any, _i: int = 0):
	"""
	Traversal-safe method to add a siblings data node.
	:param data: The data object you're traversing.
	:param node_path: List of path segments pointing to the node you're creating a
			sibling of. Same as node_path of traverse()
	:param new_key: The sibling key to create.
	:param new_data: The new data to be stored at the key.
	:param _i: Depth of node_path iterator.
	"""
	if _i < len(node_path) - 1:
		return add_sibling(data[node_path[_i]], node_path, new_key, new_data, _i + 1)
	else:
		data[new_key] = new_data


