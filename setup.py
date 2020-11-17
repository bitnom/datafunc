# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datafunc']

package_data = \
{'': ['*']}

install_requires = \
['dotty-dict', 'mo-dots', 'traversy>=0.1.2']

setup_kwargs = {
    'name': 'datafunc',
    'version': '0.0.3',
    'description': 'Python functions for various dict, list, and other data structures.',
    'long_description': '# datafunc\n\nPython package of various functions for dict, list, and other data structures.\n\n**License: MIT**\n\n### Changelog\n- **11/17/2020 - 0.0.3** : Added `duplicate()` and `add_sibling()` methods. Added some missing type declarations.\n- **11/15/2020 - 0.0.2** : Type annotations & minor refactors.\n- **11/15/2020 - 0.0.1** : Initial methods.',
    'author': 'Tom A.',
    'author_email': '14287229+TensorTom@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tensortom/datafunc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
