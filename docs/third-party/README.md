# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/taksonomia/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([7be58cff ...](https://git.sr.ht/~sthagen/taksonomia/blob/default/etc/sbom/cdx.json.sha256 "sha256:7be58cff3250c69fdb6b81307148aaf917d5f7c8a20149758b515719cfa51a58")).
<!--[[[end]]] (checksum: b3667cabdea04f0c9b02fc2ac401a7a9)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                  | Version                                             | License     | Author                | Description (from packaging data)                                                                        |
|:------------------------------------------------------|:----------------------------------------------------|:------------|:----------------------|:---------------------------------------------------------------------------------------------------------|
| [PyYAML](https://pyyaml.org/)                         | [6.0.1](https://pypi.org/project/PyYAML/6.0.1/)     | MIT License | Kirill Simonov        | YAML parser and emitter for Python                                                                       |
| [lxml](https://lxml.de/)                              | [4.9.3](https://pypi.org/project/lxml/4.9.3/)       | BSD License | lxml dev team         | Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.         |
| [msgspec](https://jcristharif.com/msgspec/)           | [0.18.4](https://pypi.org/project/msgspec/0.18.4/)  | BSD License | Jim Crist-Harif       | A fast serialization and validation library, with builtin support for JSON, MessagePack, YAML, and TOML. |
| [psutil](https://github.com/giampaolo/psutil)         | [5.9.6](https://pypi.org/project/psutil/5.9.6/)     | BSD License | Giampaolo Rodola      | Cross-platform lib for process and system monitoring in Python.                                          |
| [py-cpuinfo](https://github.com/workhorsy/py-cpuinfo) | [9.0.0](https://pypi.org/project/py-cpuinfo/9.0.0/) | MIT License | Matthew Brennan Jones | Get CPU info with pure Python                                                                            |
<!--[[[end]]] (checksum: d81b1d251cc52255cc6f771eea0e6171)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name | Version | License | Author | Description (from packaging data) |
|:-----|:--------|:--------|:-------|:----------------------------------|
<!--[[[end]]] (checksum: 8a87b89207db0be2864af66f9266660c)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
lxml==4.9.3
msgspec==0.18.4
psutil==5.9.6
py-cpuinfo==9.0.0
PyYAML==6.0.1
````
<!--[[[end]]] (checksum: 7e852bac1adf0887382d1f62825dc48a)-->
