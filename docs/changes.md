# Change History


# 2022.9.10

* Changed the tree root parameter to optional (and added positional optional alternative) parameter defaulting to current working dir to ease use in automation within build processes

## 2022.9.9

* Achieved complete (screening) test coverage
* Added command line interface and changed signature and behavior of main implementation interface
* Changed default output to stdout, extended collector, and fixed aggregations not propagated
* Decided on hash avalanches based on hexdigest hashing
* Transformed non-existing tree-root as well as non-folder tree-root into error cases
* Updated baseline, SBOM, third-party docs, and usage docs

## 2022.9.8

* Initial release on PyPI
