# python-json-tidier
json convert multiple lines to single line. 
<hr />

### Usage

> ### 1. place [json_compiler.py](https://github.com/Weilory/python-json-tidier/blob/main/main/json_compiler.py) into the folder containing multiple json files.

```txt
-----main ----- course.json
         |----- theme.json
         |----- timeline.json
         |_____ json_compiler.py
```

> ### 2. rename files that you want to be compiled with a new extension: `jsonpy`, which won't be edited by the compiler. 

```txt
-----main ----- course.jsonpy
         |----- theme.jsonpy
         |----- timeline.jsonpy
         |_____ json_compiler.py
```

> ### 3. run `json_compiler.py`, then

```txt
-----main ----- course.jsonpy
         |----- theme.jsonpy
         |----- timeline.jsonpy
         |----- json_compiler.py
         |
         |----- course.json
         |----- theme.json
         |_____ timeline.json
```

> ### 4. To make modification, edit `json.py` file and run compiler again. 



