# API

Use the python help command to learn about the API.

Something like:

```python
>>> import pathlib
>>> import sys
>>> from taksonomia.taksonomia import Taxonomy
>>> tree_root = pathlib.Path('/some/example/here')
>>> taxonomy = Taxonomy(tree_root, excludes = '', key_function='md5')
>>> for path in sorted(tree_root.rglob('*')):
...     taxonomy.add_branch(path) if path.is_dir() else taxonomy.add_leaf(path)
...
>>> taxonomy.dump(sink=sys.stdout, format_type='json')
{
  "taxonomy": {
    "hash_algo_prefs": [
      "sha512",
      "sha256"
    ],
    "key_function": "md5",
    "generator": {
      "name": "taksonomia",
      "version_info": [
        "2023",
        "6",
        "18",
        "a8561973"
      ],
# ...
```
