from mo_dots import Data, DataObject, FlatList, from_data, to_data, literal_field
from dotty_dict import Dotty, dotty
import json
from traversy import traverse


def flatten(var):
	result = Data()
	for v in traverse(var, output_formatter=to_data):
		result[literal_field(v.path_str)] = v.value
	return result


def iterable(var):
	try:
		iter(var)
		return True
	except TypeError:
		return False


def listlike(var):
	return not isinstance(var, str) and not dictlike(var) and iterable(var)


def mo_dotian(var):
	return isinstance(var, (Data, DataObject, FlatList))


def from_data_if(var, cond):
	return from_data(var) if cond(var) else var


def dictlike(var):
	try:
		var.items()
		return True
	except (TypeError, AttributeError):
		return False


def nestable(var):
	return dictlike(var) or listlike(var)


def jsonify_dictlike_vals(obj):
	return {k: json.dumps(json.dumps(v, default=from_data)) if nestable(v) else v for k, v in obj.items()}


def compare(d1, d2):
	d1_keys = set(d1.keys())
	d2_keys = set(d2.keys())
	shared_keys = d1_keys.intersection(d2_keys)
	added = d1_keys - d2_keys
	removed = d2_keys - d1_keys
	modified = {o: (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
	same = set(o for o in shared_keys if d1[o] == d2[o])
	return to_data({'add': added, 'rm': removed, 'mod': modified, 'eq': same})


def function_of(func, func_names):
	"""
	Determine whether or not a function's (func) name exists in tuple of strings
	(func_names).
	:param func: The callable function to test.
	:param func_names: Tuple of function names as strings ("func1", "func2", "func3,)
	:return: Boolean True (func is of func_names) or False (func is not of func_names)
	"""
	return hasattr(func, '__call__') and func.__name__ in func_names


def basevals(d, *attrs):
	"""
	This method receives a dict and list of attributes to return the innermost value of the give dict
	"""
	try:
		for at in attrs:
			d = d[at]
		return d
	except(KeyError, TypeError):
		return None


def vivify(d, *attrs):
	"""
	Adds "val" to dict in the hierarchy mentioned via *attrs
	For ex:
	vivify(animals, "cat", "leg","fingers", 4) is equivalent to animals["cat"]["leg"]["fingers"]=4
	This method creates necessary objects until it reaches the final depth
	This behaviour is also known as autovivification and plenty of implementation are around
	This implementation addresses the corner case of replacing existing primitives
	https://gist.github.com/hrldcpr/2012250#gistcomment-1779319
	"""
	for attr in basevals[:-2]:
		if type(d.get(attr)) not in (dict, Data, Dotty, DataObject):
			d[attr] = {}
		d = d[attr]
	d[attrs[-2]] = attrs[-1]
