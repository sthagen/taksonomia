# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([dcbedfed ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:dcbedfededcd63bae3bf9b2534bbcd7657c27836a2883e08b959965a173abde0")).
<!--[[[end]]] (checksum: 5ded2b7009d4ac57335b1b0670609f55)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                  | Version                                             | License                              | Author                | Description (from packaging data)                                              |
|:------------------------------------------------------|:----------------------------------------------------|:-------------------------------------|:----------------------|:-------------------------------------------------------------------------------|
| [PyYAML](https://pyyaml.org/)                         | [6.0](https://pypi.org/project/PyYAML/6.0/)         | MIT License                          | Kirill Simonov        | YAML parser and emitter for Python                                             |
| [orjson](https://github.com/ijl/orjson)               | [3.8.0](https://pypi.org/project/orjson/3.8.0/)     | Apache Software License; MIT License | ijl <ijl@mailbox.org> | Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy |
| [psutil](https://github.com/giampaolo/psutil)         | [5.9.2](https://pypi.org/project/psutil/5.9.2/)     | BSD License                          | Giampaolo Rodola      | Cross-platform lib for process and system monitoring in Python.                |
| [py-cpuinfo](https://github.com/workhorsy/py-cpuinfo) | [8.0.0](https://pypi.org/project/py-cpuinfo/8.0.0/) | MIT License                          | Matthew Brennan Jones | Get CPU info with pure Python 2 & 3                                            |
<!--[[[end]]] (checksum: b099228aa537f5c5d09c42dd706ec1e4)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/) | BSD License | Armin Ronacher | Composable command line interface toolkit |
<!--[[[end]]] (checksum: dc3a866a7aa3332404bde3da87727cb9)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="https://raw.githubusercontent.com/sthagen/pilli/default/docs/third-party/package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
orjson==3.8.0
psutil==5.9.2
py-cpuinfo==8.0.0
PyYAML==6.0
````
<!--[[[end]]] (checksum: 112f7a12cddd9bf86bd3160bdc3f6c91)-->
