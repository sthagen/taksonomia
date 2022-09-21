# Usage

To use taksonomia in a project:

```python
import taksonomia.taksonomia as api
```

## Getting Help

For the commandline please call the app without arguments or add the help option (`-h` or `--help`).

```console
❯ taksonomia --help
usage: taksonomia [-h] [--tree-root TREE_ROOT] [--excludes EXCLUDES] [--key-function KEY_FUNCTION]
                  [--out-path OUT_PATH] [--formats FORMAT_TYPE_CSL] [--base64-encode]
                  [--xz-compress] [tree_root_pos]

Taxonomy (Finnish: taksonomia) of a folder tree, guided by conventions.

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
  --key-function KEY_FUNCTION, -k KEY_FUNCTION
                        key function (elf, md5) for branches and leaves
                        (default: elf) use md5 for larger taxonomies
  --out-path OUT_PATH, -o OUT_PATH
                        output file path (stem) for taxonomy (default: STDOUT)
  --formats FORMAT_TYPE_CSL, -f FORMAT_TYPE_CSL
                        formats (json, xml, yaml) as comma separated list for taxonomy (default: json)
  --base64-encode, -e   encode taxonomy in base64 (default: False)
                        incompatible with option --xz-compress
  --xz-compress, -c     compress taxonomy per LZMA(xz) (default: False)
                        incompatible with option --base64-encode
```

## Example of Visiting a Folder

### Default Taxonomy Format (JSON)

Taxing a folder with a single empty file: 

```console
❯ taksonomia --tree-root test/fixtures/corner > file.json
2022-09-12T21:30:01.144294+00:00 INFO [TAKSONOMIA]: Assessing taxonomy of folder test/fixtures/corner
2022-09-12T21:30:01.144863+00:00 INFO [TAKSONOMIA]: Output channel is STDOUT
2022-09-12T21:30:01.229016+00:00 INFO [TAKSONOMIA]: Detected leaf test/fixtures/corner/empty.txt
2022-09-12T21:30:01.229016+00:00 INFO [TAKSONOMIA]: - Dumping taxonomy as json format
2022-09-12T21:30:01.229690+00:00 INFO [TAKSONOMIA]: Assessed taxonomy of folder test/fixtures/corner in 0.084431 secs
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
    "key_function": "elf",
    "generator": {
      "name": "taksonomia",
      "version_info": [
        "2022",
        "9",
        "13",
        "e5cceb14"
      ],
      "source": "https://pypi.or/project/taksonomia/2022.9.11/",
      "sbom": "https://codes.dilettant.life/docs/taksonomia/third-party/"
    },
    "context": {
      "start_ts": "2022-09-10 12:14:02.229878 +00:00",
      "end_ts": "2022-09-10 12:14:02.305927 +00:00",
      "duration_secs": 0.084431,
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
      "41524436": {
        "path": "test/fixtures/corner/empty.txt",
        "branch": "110978498",
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
❯ taksonomia  --tree-root test/fixtures/corner --format yaml > file.yml
2022-09-12T21:29:10.595129+00:00 INFO [TAKSONOMIA]: Assessing taxonomy of folder test/fixtures/corner
2022-09-12T21:29:10.595660+00:00 INFO [TAKSONOMIA]: Output channel is STDOUT
2022-09-12T21:29:10.676206+00:00 INFO [TAKSONOMIA]: Detected leaf test/fixtures/corner/empty.txt
2022-09-12T21:29:10.676206+00:00 INFO [TAKSONOMIA]: - Dumping taxonomy as yaml format
2022-09-12T21:29:10.683559+00:00 INFO [TAKSONOMIA]: Assessed taxonomy of folder test/fixtures/corner in 0.080705 secs
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
    duration_secs: 0.080705
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
    - '13'
    - e5cceb14
  hash_algo_prefs:
  - sha512
  - sha256
  key_function: elf
  leaves:
    '41524436':
      branch: '110978498'
      hash_hexdigest:
        sha256: e3b0...b855
        sha512: cf83e135...f927da3e
      mod_time: '2022-09-09 19:59:01.121278 +00:00'
      path: test/fixtures/corner/empty.txt
      size_bytes: 0
  summary:
    count_branches: 0
    count_leaves: 1
    hash_hexdigest:
      sha256: cd37...f8e6
      sha512: 8fb29448...be77f166
    size_bytes: 0
```
### XML Format

Similarly for XML:

```console
❯ taksonomia  --tree-root test/fixtures/corner --format xml > file.xml
2022-09-18T20:39:13.509378+00:00 INFO [TAKSONOMIA]: Assessing taxonomy of folder test/fixtures/corner
2022-09-18T20:39:13.510101+00:00 INFO [TAKSONOMIA]: Output channel is STDOUT
2022-09-18T20:39:13.611015+00:00 INFO [TAKSONOMIA]: Detected leaf test/fixtures/corner/empty.txt
2022-09-18T20:39:13.621416+00:00 INFO [TAKSONOMIA]: - Dumping taxonomy as xml format
2022-09-18T20:39:13.621416+00:00 INFO [TAKSONOMIA]: Assessed taxonomy of folder test/fixtures/corner in 0.101208 secs
```

yields (edited):

```xml
<?xml version="1.0" encoding="utf-8" ?>
<taxonomy>
  <hash_algo_prefs>
    <item>sha512</item>
    <item>sha256</item>
  </hash_algo_prefs>
  <key_function>elf</key_function>
  <generator>
    <name>taksonomia</name>
    <version_info>
      <item>2022</item>
      <item>9</item>
      <item>18</item>
      <item>abadcafe</item>
    </version_info>
    <source>https://pypi.or/project/taksonomia/2022.9.18/</source>
    <sbom>https://codes.dilettant.life/docs/taksonomia/third-party/</sbom>
  </generator>
  <context>
    <start_ts>2022-09-18 20:39:13.510180 +00:00</start_ts>
    <end_ts>2022-09-18 20:39:13.611388 +00:00</end_ts>
    <duration_secs>0.080705</duration_secs>
    <!-- ... -->
    <cpu_info>
      <python_version>3.10.6.final.0 (64 bit)</python_version>
      <!-- ... -->
    </cpu_info>
    <memory>
      <!-- ... -->
    </memory>
    <disks>
      <!-- ... -->
    </disks>
    <pwd>/some/where</pwd>
    <tree_root>test/fixtures/corner</tree_root>
    <excludes />
    <machine_perf>
      <pre>
        <!-- ... -->
      </pre>
      <post>
        <!-- ... -->
      </post>
    </machine_perf>
  </context>
  <summary>
    <hash_hexdigest>
      <sha512>8fb29448...be77f166</sha512>
      <sha256>cd37...f8e6</sha256>
    </hash_hexdigest>
    <count_branches>0</count_branches>
    <count_leaves>1</count_leaves>
    <size_bytes>0</size_bytes>
  </summary>
  <branches />
  <leaves>
    <key id="41524436">
      <path>test/fixtures/corner/empty.txt</path>
      <branch>110978498</branch>
      <hash_hexdigest>
        <sha512>cf83e135...f927da3e</sha512>
        <sha256>e3b0...b855</sha256>
      </hash_hexdigest>
      <size_bytes>0</size_bytes>
      <mod_time>2022-09-09 19:59:01.121278 +00:00</mod_time>
    </key>
  </leaves>
</taxonomy>
```

### Multiple Formats at once

```console
❯ taksonomia --tree-root test/fixtures/corner -o inventory -f json,yaml
2022-09-21T15:49:36.073212+00:00 INFO [TAKSONOMIA]: Assessing taxonomy of folder test/fixtures/corner
2022-09-21T15:49:36.074322+00:00 INFO [TAKSONOMIA]: Output channel is inventory
2022-09-21T15:49:36.175694+00:00 INFO [TAKSONOMIA]: Detected leaf test/fixtures/corner/empty.txt
2022-09-21T15:49:36.175771+00:00 INFO [TAKSONOMIA]: - Dumping taxonomy as json format
2022-09-21T15:49:36.176401+00:00 INFO [TAKSONOMIA]: - Dumping taxonomy as yaml format
2022-09-21T15:49:36.183656+00:00 INFO [TAKSONOMIA]: Assessed taxonomy of folder test/fixtures/corner in 0.101696 secs
```
