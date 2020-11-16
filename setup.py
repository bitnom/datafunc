# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datafunc']

package_data = \
{'': ['*']}

install_requires = \
['dotty-dict>=1.3.0', 'mo-dots>=3.135.20303', 'traversy>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'datafunc',
    'version': '0.0.1',
    'description': 'Python functions for various dict, list, and other data structures.',
    'long_description': '# datafunc\n\nPython package of various functions for dict, list, and other data structures.\n\n**License: MIT**\n\n### Changelog\n\n- **11/15/2020 - 0.0.1** : Initial methods.',
    'author': 'Tom A.',
    'author_email': '14287229+TensorTom@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tensortom/datafunc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
