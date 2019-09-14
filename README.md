# AVR Flash

Flash multiple devices using `avrdude`.

## Installation

### Linux/macOS:

Preferably, use a virtualenv:
```bash
pip install virtualenv
virtualenv venv
. venv/bin/activate
```

Install all required python packages using pip
```bash
pip install -r requirements.txt
```

Also make sure that `avrdude` is installed.

## Run

```bash
python flash.py path_to_hex_file.hex
```
Make sure to **NOT** flash the version with the bootloader. This might brick your arduino. If so, you can recover it using a second Arduino as an ISP to reflash the bootloader.



## License

   Copyright 2019 Jonas Drotleff <j.drotleff@desk-lab.de>

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
