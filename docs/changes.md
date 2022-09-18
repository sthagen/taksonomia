# Change History

## 2022.9.18

* Amended leaves with branch info to boost navigation

## 2022.9.14

* Completed the move to orjson
* Added XML format option

## 2022.9.13

* Added base64-encode command line option to ease embedding of taxonomies
* Added key-function command line option (elf|md5) for branches and leaves (default elf)
* Added LZMA xz-compression option (mutually exclusive to encoding) for output files
* Added logging to support taxing larger trees and document parameters during execution
* Added more short options in the hope these are useful and do not mislead users
* Belt and braces process info gathering to fix https://todo.sr.ht/~sthagen/taksonomia/2

## 2022.9.12

* Adapted and extended tests to cover new behaviors, options, and again achieve full (screening) test coverage
* Added format option and additional YAML format
* Moved all tree elements under the single taxonomy root to simplify injection of tree and prepare possible future XML format
* Migrated path keys to md5 and added path key to records (branches and leaves)

## 2022.9.11

* Added excludes option to exempt paths containing zero or more of the comma separated strings
* Added generator information and the excludes to the taxonomy report
* Fixed failed CPSR coding for branch hash digest slots
* Less naive context info gathering to fix https://todo.sr.ht/~sthagen/taksonomia/1

## 2022.9.10

* Changed the tree root parameter to optional (and added positional optional alternative) parameter defaulting to current working dir to ease use in automation within build processes
* Extended the taxonomy with context and performance data
* Optimized away the pre pass for folder gathering
* Simplified the reporting by directly returning the serializable tree from the new report method

## 2022.9.9

* Achieved complete (screening) test coverage
* Added command line interface and changed signature and behavior of main implementation interface
* Changed default output to stdout, extended collector, and fixed aggregations not propagated
* Decided on hash avalanches based on hexdigest hashing
* Transformed non-existing tree-root as well as non-folder tree-root into error cases
* Updated baseline, SBOM, third-party docs, and usage docs

## 2022.9.8

* Initial release on PyPI
