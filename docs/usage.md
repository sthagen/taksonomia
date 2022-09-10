# Usage

To use taksonomia in a project:

```python
import taksonomia.taksonomia as api
```

## Getting Help

For the commandline please add the help option `-h` or `--help` like so:

```console
❯ taksonomia -h
usage: taksonomia [-h] [--tree-root TREE_ROOT] [--out-path OUT_PATH] [tree_root_pos]

Taxonomy (Finnish: taksonomia) guided by conventions of a folder tree.

positional arguments:
  tree_root_pos         Root of the tree to visit. Optional (default: PWD)

options:
  -h, --help            show this help message and exit
  --tree-root TREE_ROOT, -t TREE_ROOT
                        Root of the tree to visit. Optional (default: positional tree root value)
  --out-path OUT_PATH, -o OUT_PATH
                        output file path for taxonomy (default: STDOUT)
```

## Example of Visiting a Folder

Using a folder with a single empty file results in something like
(ommitted some parts of the hash values and context entries to avoid scrollbars):

```console
❯ taksonomia --tree-root test/fixtures/corner
{
  "hash_algo_prefs": [
    "sha512",
    "sha256"
  ],
  "context": {
    "start_ts": "2022-09-10 12:14:02.229878 +00:00",
    "end_ts": "2022-09-10 12:14:02.305927 +00:00",
    "duration_usecs": 76049,
    "...": "...",
    "boottime": "2022-09-10 05:56:16.000000 +00:00",
    "cpu_info": {
      "python_version": "3.10.6.final.0 (64 bit)",
      "...": "..."
    },
    "memory": {
      "swap": "...",
      "virtual": {"...": "..."}
    },
    "disks": {
      "counters_combined": {"...": "..."},
      "partitions": ["..."],
      "path_selector": "test/fixtures/corner",
      "usage": {"...": "..."}
    },
    "pwd": "/some/where",
    "tree_root": "test/fixtures/corner",
    "machine_perf": {
      "pre": {
        "...": "...",
        "create_time": "2022-09-10 12:14:02.029446 +00:00",
        "...": "...",
        "num_fds": 3,
        "num_ctx_switches": {
          "voluntary": 199,
          "involuntary": 0
        }
      },
      "post": {
        "...": "...",
        "num_ctx_switches": {
          "voluntary": 210,
          "involuntary": 0
        }
      }
    }
  },
  "summary": {
    "hash_hexdigest": {
      "sha512": "8fb29448...be77f166",
      "sha256": "cd372fb85148700fa88095e3492d3f9f5beb43e555e5ff26d95f5a6adc36f8e6"
    },
    "count_branches": 0,
    "count_leaves": 1,
    "size_bytes": 0
  },
  "branches": {},
  "leaves": {
    "test/fixtures/corner/empty.txt": {
      "hash_hexdigest": {
        "sha512": "cf83e135...f927da3e",
        "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
      },
      "size_bytes": 0,
      "mod_time": "2022-09-09 19:59:01.121278 +00:00"
    }
  }
}
```
