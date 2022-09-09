# Usage

To use taksonomia in a project:

```python
import taksonomia.taksonomia as api
```

## Getting Help

For the commandline please add the help option `-h` or `--help` like so:

```console
❯ taksonomia -h
usage: __main__.py [-h] --tree-root TREE_ROOT [--out-path OUT_PATH]

taksonomia

options:
  -h, --help            show this help message and exit
  --tree-root TREE_ROOT, -t TREE_ROOT
                        tree root
  --out-path OUT_PATH, -o OUT_PATH
                        output file path for taxonomy (default: STDOUT)
```

## Example of Visiting a Folder

Using a folder with a single empty file results in something like
(ommitted some parts of the sha512 hashes to avoid horizontal scrollbars):

```console
❯ taksonomia --tree-root test/fixtures/corner
{
  "sha512": "8fb29448faee18 ... de1715aa6badede8ddc801c739777be77f166",
  "count_folders": 1,
  "count_files": 1,
  "size_bytes": 0,
  "branches": {
    "test/fixtures/corner": {
      "sha512": "8fb29448f ... e7bde1715aa6badede8ddc801c739777be77f166",
      "count_folders": 1,
      "count_files": 1,
      "size_bytes": 0,
      "mod_time": "2022-09-09 19:59:01.121310 +00:00"
    }
  },
  "leaves": {
    "test/fixtures/corner/empty.txt": {
      "sha512": "cf83e1357eef ... 877eec2f63b931bd47417a81a538327af927da3e",
      "size_bytes": 0,
      "mod_time": "2022-09-09 19:59:01.121278 +00:00"
    }
  }
}
```
