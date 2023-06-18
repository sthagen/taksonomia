# Usage

To use taksonomia in a project:

```python
import taksonomia.taksonomia as api
```

## Getting Help

For the commandline please call the app without arguments or add the help option (`-h` or `--help`).

```console
❯ taksonomia --help
Taxonomy (Finnish: taksonomia) of a folder tree, guided by conventions. version 2023.6.18+parent.a8561973
usage: taksonomia [-h] [--tree-root TREE_ROOT] [--excludes EXCLUDES] [--key-function KEY_FUNCTION]
                  [--out-path OUT_PATH] [--formats FORMAT_TYPE_CSL] [--base64-encode] [--xz-compress]
                  [--version]
                  [tree_root_pos]

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
                        key function (blake2, elf, md5) for branches and leaves
                        (default: blake2) use elf only for very small taxonomies
  --out-path OUT_PATH, -o OUT_PATH
                        output file path (stem) for taxonomy (default: STDOUT)
  --formats FORMAT_TYPE_CSL, -f FORMAT_TYPE_CSL
                        formats (json, xml, yaml) as comma separated list for taxonomy (default: json)
  --base64-encode, -e   encode taxonomy in base64 (default: False)
                        incompatible with option --xz-compress
  --xz-compress, -c     compress taxonomy per LZMA(xz) (default: False)
                        incompatible with option --base64-encode
  --version, -V         show version of the app and exit
```

## Example of Visiting a Folder

### Default Taxonomy Format (JSON)

Taxing a folder with a single empty file: 

```console
❯ taksonomia --tree-root test/fixtures/corner > file.json
2023-06-18T12:07:46.384571+00:00 INFO [TAKSONOMIA]: Assessing taxonomy of folder test/fixtures/corner
2023-06-18T12:07:46.385266+00:00 INFO [TAKSONOMIA]: Output channel is STDOUT
2023-06-18T12:07:46.453150+00:00 INFO [TAKSONOMIA]: Detected leaf test/fixtures/corner/empty.txt
2023-06-18T12:07:46.453213+00:00 INFO [TAKSONOMIA]: - Dumping taxonomy as json format
2023-06-18T12:07:46.453624+00:00 INFO [TAKSONOMIA]: Assessed taxonomy of folder test/fixtures/corner in 0.068191 secs
```

... results in something like (ommitted some parts of the hash values and context entries to avoid scrollbars):

```json
{
  "taxonomy": {
    "hash_algo_prefs": [
      "sha512",
      "sha256"
    ],
    "key_function": "blake2",
    "generator": {
      "name": "taksonomia",
      "version_info": [
        "2023",
        "6",
        "18",
        "a8561973"
      ],
      "source": "https://pypi.org/project/taksonomia/2023.6.18/",
      "sbom": "https://codes.dilettant.life/docs/taksonomia/third-party/"
    },
    "context": {
      "start_ts": "2023-06-18 12:07:46.385326 +00:00",
      "end_ts": "2023-06-18 12:07:46.453517 +00:00",
      "duration_secs": 0.068191,
      "...": "...",
      "boottime": "2023-06-18 07:15:12.000000 +00:00",
      "cpu_info": {
        "python_version": "3.10.9.final.0 (64 bit)",
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
          "create_time": "2023-06-18 12:07:46.185527 +00:00",
          "...": "...",
          "num_fds": 3,
          "num_ctx_switches": {
            "involuntary": 0,
            "voluntary": 291
          }
        },
        "post": {
          "...": "...",
          "num_ctx_switches": {
            "involuntary": 0,
            "voluntary": 302
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
      "45fae75...3c045662": {
        "path": "test/fixtures/corner/empty.txt",
        "branch": "9b311395...d917fb07",
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
2023-06-18T12:12:57.431188+00:00 INFO [TAKSONOMIA]: Assessing taxonomy of folder test/fixtures/corner
2023-06-18T12:12:57.431803+00:00 INFO [TAKSONOMIA]: Output channel is STDOUT
2023-06-18T12:12:57.499515+00:00 INFO [TAKSONOMIA]: Detected leaf test/fixtures/corner/empty.txt
2023-06-18T12:12:57.499581+00:00 INFO [TAKSONOMIA]: - Dumping taxonomy as yaml format
2023-06-18T12:12:57.506535+00:00 INFO [TAKSONOMIA]: Assessed taxonomy of folder test/fixtures/corner in 0.06803 secs
```

yields (edited):

```yaml
taxonomy:
  branches: {}
  context:
    boottime: '2023-06-18 07:15:12.000000 +00:00'
    cpu_info:
      ...
      python_version: 3.10.9.final.0 (64 bit)
    disks:
      ...
      path_selector: test/fixtures/corner
      usage:
        ...
    duration_secs: 0.06803
    end_ts: '2023-06-18 12:12:57.499890 +00:00'
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
    start_ts: '2023-06-18 12:12:57.431860 +00:00'
    tree_root: test/fixtures/corner
  generator:
    name: taksonomia
    sbom: https://codes.dilettant.life/docs/taksonomia/third-party/
    source: https://pypi.org/project/taksonomia/2023.6.18/
    version_info:
    - '2023'
    - '6'
    - '18'
    - a8561973
  hash_algo_prefs:
  - sha512
  - sha256
  key_function: blake2
  leaves:
    ? 45fae756...a53c045662
    : branch: 9b311395...d917fb07
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
2023-06-18T12:16:39.569156+00:00 INFO [TAKSONOMIA]: Assessing taxonomy of folder test/fixtures/corner
2023-06-18T12:16:39.569612+00:00 INFO [TAKSONOMIA]: Output channel is STDOUT
2023-06-18T12:16:39.639475+00:00 INFO [TAKSONOMIA]: Detected leaf test/fixtures/corner/empty.txt
2023-06-18T12:16:39.639544+00:00 INFO [TAKSONOMIA]: - Dumping taxonomy as xml format
2023-06-18T12:16:39.646266+00:00 INFO [TAKSONOMIA]: Assessed taxonomy of folder test/fixtures/corner in 0.07016 secs
```

yields (edited):

```xml
<?xml version="1.0" encoding="utf-8" ?>
<taxonomy>
  <hash_algo_prefs>
    <item>sha512</item>
    <item>sha256</item>
  </hash_algo_prefs>
  <key_function>blake2</key_function>
  <generator>
    <name>taksonomia</name>
    <version_info>
      <item>2023</item>
      <item>6</item>
      <item>18</item>
      <item>a8561973</item>
    </version_info>
    <source>https://pypi.org/project/taksonomia/2023.6.18/</source>
    <sbom>https://codes.dilettant.life/docs/taksonomia/third-party/</sbom>
  </generator>
  <context>
    <start_ts>2023-06-18 12:16:39.569676 +00:00</start_ts>
    <end_ts>2023-06-18 12:16:39.639836 +00:00</end_ts>
    <duration_secs>0.07016</duration_secs>
    <!-- ... -->
    <cpu_info>
      <python_version>3.10.9.final.0 (64 bit)</python_version>
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
    <key id="45fae756...3c045662">
      <path>test/fixtures/corner/empty.txt</path>
      <branch>9b311395...d917fb07</branch>
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
2023-06-18T12:19:25.849420+00:00 INFO [TAKSONOMIA]: Assessing taxonomy of folder test/fixtures/corner
2023-06-18T12:19:25.850021+00:00 INFO [TAKSONOMIA]: Output channel is inventory
2023-06-18T12:19:25.916580+00:00 INFO [TAKSONOMIA]: Detected leaf test/fixtures/corner/empty.txt
2023-06-18T12:19:25.916657+00:00 INFO [TAKSONOMIA]: - Dumping taxonomy as json format
2023-06-18T12:19:25.917342+00:00 INFO [TAKSONOMIA]: - Dumping taxonomy as yaml format
2023-06-18T12:19:25.924094+00:00 INFO [TAKSONOMIA]: Assessed taxonomy of folder test/fixtures/corner in 0.066893 secs
```
