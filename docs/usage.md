# Usage

To use taksonomia in a project:

```python
import taksonomia.taksonomia as api
```

## Getting Help

For the commandline please add the help option `-h` or `--help` like so:

```console
❯ taksonomia -h
usage: taksonomia [-h] [--tree-root TREE_ROOT] [--excludes EXCLUDES] [--out-path OUT_PATH] [--format FORMAT] [tree_root_pos]

Taxonomy (Finnish: taksonomia) guided by conventions of a folder tree.

positional arguments:
  tree_root_pos         Root of the tree to visit. Optional (default: PWD)

options:
  -h, --help            show this help message and exit
  --tree-root TREE_ROOT, -t TREE_ROOT
                        Root of the tree to visit. Optional
                        (default: positional tree root value)
  --excludes EXCLUDES, -x EXCLUDES
                        comma separated list of values to exclude paths
                        containing the substring (default: empty string)
  --out-path OUT_PATH, -o OUT_PATH
                        output file path for taxonomy (default: STDOUT)
  --format FORMAT       format (json, yaml) for taxonomy (default: json)
```

## Example of Visiting a Folder

### Default Taxonomy Format (JSON)

Taxing a folder with a single empty file: 

```console
❯ taksonomia --tree-root test/fixtures/corner
```

... results in something like (ommitted some parts of the hash values and context entries to avoid scrollbars):

```json
{
  "taxonomy": {
  {
    "hash_algo_prefs": [
      "sha512",
      "sha256"
    ],
    "generator": {
      "name": "taksonomia",
      "version_info": [
        "2022",
        "9",
        "11",
        "fadecafe"
      ],
      "source": "https://pypi.or/project/taksonomia/2022.9.11/",
      "sbom": "https://codes.dilettant.life/docs/taksonomia/third-party/"
    },
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
      "excludes": [],
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
        "sha256": "cd37...f8e6"
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
          "sha256": "e3b0...b855"
        },
        "size_bytes": 0,
        "mod_time": "2022-09-09 19:59:01.121278 +00:00"
      }
    }
  }
}
```

### YAML Format

Similarly for YAML:

```console
❯ python -m taksonomia  --tree-root test/fixtures/corner --format yaml
```

yields (edited):

```yaml
taxonomy:
  branches: {}
  context:
    boottime: '2022-09-11 07:13:04.000000 +00:00'
    cpu_info:
      ...
      python_version: 3.10.6.final.0 (64 bit)
    disks:
      ...
      path_selector: test/fixtures/corner
      usage:
        ...
    duration_usecs: 81618
    end_ts: '2022-09-11 14:44:50.953556 +00:00'
    excludes: []
    machine_perf:
      post:
        ...
      pre:
        ...
    memory:
      ...
    ...
    pwd: /some/where
    start_ts: '2022-09-11 14:44:50.871938 +00:00'
    tree_root: test/fixtures/corner
  generator:
    name: taksonomia
    sbom: https://codes.dilettant.life/docs/taksonomia/third-party/
    source: https://pypi.or/project/taksonomia/2022.9.11/
    version_info:
    - '2022'
    - '9'
    - '11'
    - fadecafe
  hash_algo_prefs:
  - sha512
  - sha256
  leaves:
    test/fixtures/corner/empty.txt:
      hash_hexdigest:
        sha256: e3b0...b855
        sha512: cf83e135...f927da3e
      mod_time: '2022-09-09 19:59:01.121278 +00:00'
      size_bytes: 0
  summary:
    count_branches: 0
    count_leaves: 1
    hash_hexdigest:
      sha256: cd37...f8e6
      sha512: 8fb29448...be77f166
    size_bytes: 0
```
