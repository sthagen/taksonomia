# Usage

To use taksonomia in a project:

```python
import taksonomia.taksonomia as api
```

For the commandline (for now) please add the help option like so:

TBD

Example of visiting the test folder:
```python
>>> import pathlib
>>> import taksonomia.taksonomia as api
>>> api.main(pathlib.Path('test'))
{
  "sha512": "7e1df68a6f60a08c4de45971843659773e5d15ba9a7b3cdf9e0c170e2bed54e9f2d742966cefcd6b976a1006c213d748363cbf815de37a145677f09bc31ae544",
  "count_folders": 0,
  "count_files": 0,
  "branches": {
    "test": {
      "sha512": "7e1df68a6f60a08c4de45971843659773e5d15ba9a7b3cdf9e0c170e2bed54e9f2d742966cefcd6b976a1006c213d748363cbf815de37a145677f09bc31ae544",
      "count_folders": 8,
      "count_files": 18,
      "size_bytes": 2907,
      "mod_time": "2022-09-08 20:56:19.299842 +00:00"
    },
    "test/__pycache__": {
      "sha512": "f525617fd2791ea81458a46a735349213775170db689b9738ddc014e88c4e66f64b5635b7bcc571f92de98c1f4a804f1399552f79268c682120267e42f17a370",
      "count_folders": 1,
      "count_files": 4,
      "size_bytes": 1285,
      "mod_time": "2022-09-08 20:56:19.398944 +00:00"
    },
    "test/fixtures": {
      "sha512": "e7fa86618d038906abf957aad3c1cd42af5aecd37ce55f0e6da44c5e3d948b413fdaf022ef4009d06678c2031f06a76c6fffe7c1b137d4f4f1d8f2651779e373",
      "count_folders": 6,
      "count_files": 8,
      "size_bytes": 15,
      "mod_time": "2022-09-08 20:44:48.549390 +00:00"
    },
    "test/fixtures/basic": {
      "sha512": "e7fa86618d038906abf957aad3c1cd42af5aecd37ce55f0e6da44c5e3d948b413fdaf022ef4009d06678c2031f06a76c6fffe7c1b137d4f4f1d8f2651779e373",
      "count_folders": 5,
      "count_files": 8,
      "size_bytes": 15,
      "mod_time": "2022-09-08 20:44:52.598036 +00:00"
    },
    "test/fixtures/basic/a": {
      "sha512": "e7fa86618d038906abf957aad3c1cd42af5aecd37ce55f0e6da44c5e3d948b413fdaf022ef4009d06678c2031f06a76c6fffe7c1b137d4f4f1d8f2651779e373",
      "count_folders": 4,
      "count_files": 8,
      "size_bytes": 15,
      "mod_time": "2022-09-08 20:45:52.969032 +00:00"
    },
    "test/fixtures/basic/a/b": {
      "sha512": "9e77f7444afa40aced3ed4c6c3827298aa137fc3b08b6f8a550ffd4055559a809999f02643e0aadf6ea71cf32293686fefcd621220973c74b6b90f8e1edfadc6",
      "count_folders": 2,
      "count_files": 3,
      "size_bytes": 2,
      "mod_time": "2022-09-08 20:45:26.211349 +00:00"
    },
    "test/fixtures/basic/a/b/c": {
      "sha512": "500626a48b0b8d5d3407559b84fb6ddad2150d45a190329519ea9f6e0816db04eccfb72ea9fe28466d67916c65e6b6d2674dde2bacefd3902ffe409e4ca819e8",
      "count_folders": 1,
      "count_files": 2,
      "size_bytes": 2,
      "mod_time": "2022-09-08 20:45:47.041152 +00:00"
    },
    "test/fixtures/basic/a/d": {
      "sha512": "cbf9526d701e24a10e17b4468cc2874d09b7f37e4eaa93755dca277b4c76ed89d1ac0ccd6c16d4c41f450eec9e9b3d4993159287519fb1c27b0b52c511b37002",
      "count_folders": 1,
      "count_files": 3,
      "size_bytes": 11,
      "mod_time": "2022-09-08 20:46:21.049572 +00:00"
    }
  },
  "leaves": {
    "test/__init__.py": {
      "sha512": "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 0,
      "mod_time": "2022-09-08 14:54:21.347574 +00:00"
    },
    "test/__pycache__/__init__.cpython-310-pytest-7.1.3.pyc": {
      "sha512": "48a72371f4b450fc02e062c386ca07d5248bde98e9dfaae3f0558bc55046292b1902f58f49a93a945c90b625a86f7e1a437e7f634d80e018c1bcc49e710652b5",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 145,
      "mod_time": "2022-09-08 20:56:19.300946 +00:00"
    },
    "test/__pycache__/conftest.cpython-310-pytest-7.1.3.pyc": {
      "sha512": "2acf211deaf440c6bc1f2951376e0326ec566afa4de50d4dbeb26b4b12e1f5c8602ecb21b90ae199edf1a50bdc8ed348d0b61e4170d68f20eaf68482ef1f8f25",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 145,
      "mod_time": "2022-09-08 20:56:19.302114 +00:00"
    },
    "test/__pycache__/test_cli.cpython-310-pytest-7.1.3.pyc": {
      "sha512": "cddf11c1554b449aaa56a09372e6dfb0c72d420df4e5f75ef682c6d97f15521d13c265244c9e64422ebc56bd0b7e9234c8a6be8956b8e549f4198ae2caa28963",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 145,
      "mod_time": "2022-09-08 20:56:19.396567 +00:00"
    },
    "test/__pycache__/test_taksonomia.cpython-310-pytest-7.1.3.pyc": {
      "sha512": "7ad1c2a8ea501980877c4ade54a9920a7ff1229922dc21a54569f483ade87d62070525b740a2a43829a15053880b9fb59476be922e7a32f84357d46429c50e2b",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 850,
      "mod_time": "2022-09-08 20:56:19.398943 +00:00"
    },
    "test/conftest.py": {
      "sha512": "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 0,
      "mod_time": "2022-09-08 14:54:09.202926 +00:00"
    },
    "test/fixtures/basic/a/42.txt": {
      "sha512": "39ca7ce9ecc69f696bf7d20bb23dd1521b641f806cc7a6b724aaa6cdbffb3a023ff98ae73225156b2c6c9ceddbfc16f5453e8fa49fc10e5d96a3885546a46ef4",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 2,
      "mod_time": "2022-09-08 20:45:52.969439 +00:00"
    },
    "test/fixtures/basic/a/b/c/42.txt": {
      "sha512": "39ca7ce9ecc69f696bf7d20bb23dd1521b641f806cc7a6b724aaa6cdbffb3a023ff98ae73225156b2c6c9ceddbfc16f5453e8fa49fc10e5d96a3885546a46ef4",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 2,
      "mod_time": "2022-09-08 20:45:47.041546 +00:00"
    },
    "test/fixtures/basic/a/b/c/empty.txt": {
      "sha512": "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 0,
      "mod_time": "2022-09-08 20:45:29.541584 +00:00"
    },
    "test/fixtures/basic/a/b/empty.txt": {
      "sha512": "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 0,
      "mod_time": "2022-09-08 20:45:26.211311 +00:00"
    },
    "test/fixtures/basic/a/d/123456789.txt": {
      "sha512": "d9e6762dd1c8eaf6d61b3c6192fc408d4d6d5f1176d0c29169bc24e71c3f274ad27fcd5811b313d681f7e55ec02d73d499c95455b6b5bb503acf574fba8ffe85",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 9,
      "mod_time": "2022-09-08 20:46:21.051253 +00:00"
    },
    "test/fixtures/basic/a/d/42.txt": {
      "sha512": "39ca7ce9ecc69f696bf7d20bb23dd1521b641f806cc7a6b724aaa6cdbffb3a023ff98ae73225156b2c6c9ceddbfc16f5453e8fa49fc10e5d96a3885546a46ef4",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 2,
      "mod_time": "2022-09-08 20:45:57.760044 +00:00"
    },
    "test/fixtures/basic/a/d/empty.txt": {
      "sha512": "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 0,
      "mod_time": "2022-09-08 20:45:17.127698 +00:00"
    },
    "test/fixtures/basic/a/empty.txt": {
      "sha512": "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 0,
      "mod_time": "2022-09-08 20:45:20.678396 +00:00"
    },
    "test/requirements-dev.txt": {
      "sha512": "eb70be845667883c8e33f1f8ba3385e66380898db2762e557d6782112a14fbd859f01f55585d9e7e6e2f37853d90e499d01ca803316f28fccb544b538d2012ec",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 786,
      "mod_time": "2022-09-08 19:42:42.269179 +00:00"
    },
    "test/requirements.txt": {
      "sha512": "9f6da21571b2980e517dd63d724278df84a20f113a757082a52c21f41e4cbdfb6a2a23206b2602b339b28330c63cb6bd2efc6d3f4f2824df7be13ce41d66ac5d",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 724,
      "mod_time": "2022-09-08 14:33:21.830216 +00:00"
    },
    "test/test_cli.py": {
      "sha512": "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 0,
      "mod_time": "2022-09-08 14:54:02.972306 +00:00"
    },
    "test/test_taksonomia.py": {
      "sha512": "e22853aa7f33492a1f7efd4677c9a17904f4c07eab39f78124b8f94c838952c8b8bcc85e948eb217f05edbc7ebd5cc8a8207e7ba2c157d596f35895a6f755f67",
      "count_folders": 0,
      "count_files": 1,
      "size_bytes": 97,
      "mod_time": "2022-09-08 14:54:43.668836 +00:00"
    }
  }
}
```
