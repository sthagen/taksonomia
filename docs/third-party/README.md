# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([6521a12e ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:6521a12e6e40137626814292dcd74f51a8a639fa26ffb24758c0c0aabeba3bcd")).
<!--[[[end]]] (checksum: c6a930f45c8140ea682ad967b0d5ce79)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                  | Version                                             | License     | Author                | Description (from packaging data)                                                                |
|:------------------------------------------------------|:----------------------------------------------------|:------------|:----------------------|:-------------------------------------------------------------------------------------------------|
| [PyYAML](https://pyyaml.org/)                         | [6.0](https://pypi.org/project/PyYAML/6.0/)         | MIT License | Kirill Simonov        | YAML parser and emitter for Python                                                               |
| [lxml](https://lxml.de/)                              | [4.9.2](https://pypi.org/project/lxml/4.9.2/)       | BSD License | lxml dev team         | Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API. |
| [msgspec](https://jcristharif.com/msgspec/)           | [0.11.0](https://pypi.org/project/msgspec/0.11.0/)  | BSD License | Jim Crist-Harif       | A fast and friendly JSON/MessagePack library, with optional schema validation                    |
| [psutil](https://github.com/giampaolo/psutil)         | [5.9.4](https://pypi.org/project/psutil/5.9.4/)     | BSD License | Giampaolo Rodola      | Cross-platform lib for process and system monitoring in Python.                                  |
| [py-cpuinfo](https://github.com/workhorsy/py-cpuinfo) | [9.0.0](https://pypi.org/project/py-cpuinfo/9.0.0/) | MIT License | Matthew Brennan Jones | Get CPU info with pure Python                                                                    |
<!--[[[end]]] (checksum: 1b611c14bbf99e0b2207f6fb6b50f52a)-->

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
lxml==4.9.2
msgspec==0.11.0
psutil==5.9.4
py-cpuinfo==9.0.0
PyYAML==6.0
````
<!--[[[end]]] (checksum: da2c261aa848db801bdefc32b9884811)-->
