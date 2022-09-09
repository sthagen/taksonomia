# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([4f00be01 ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:4f00be01711b390195290abc661ac18a4d165df2fa13c386c9de1cedd371dfa9")).
<!--[[[end]]] (checksum: 02f4049bc441a829aef51c4c7d1b8478)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                    | Version                                         | License                              | Author                | Description (from packaging data)                                              |
|:----------------------------------------|:------------------------------------------------|:-------------------------------------|:----------------------|:-------------------------------------------------------------------------------|
| [orjson](https://github.com/ijl/orjson) | [3.8.0](https://pypi.org/project/orjson/3.8.0/) | Apache Software License; MIT License | ijl <ijl@mailbox.org> | Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy |
<!--[[[end]]] (checksum: 5bdbbace01e33add822ef5e47b1faa18)-->

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
````
<!--[[[end]]] (checksum: 956d60ee33d79a2532a94c82b6097753)-->
