# :knife: hone
Convert CSV to automatically nested JSON.`

## Getting Started
Available as both a [Python module](#usage-python-module) and a [command line tool](#usage-command-line).

### Installation
```
pip install hone
```

### Usage: Command Line
To convert a CSV file located at `path/to/input.csv` to JSON (written to file at `path/to/output.json`):

```
hone "path/to/input.csv" "path/to/output.json"
```

### Usage: Python Module
```
import hone

Hone = hone.Hone()
schema = Hone.get_schema('path/to/input.csv')   # returns nested JSON schema for input.csv
result = Hone.convert('path/to/input.csv')      # returns converted JSON as Python dictionary
```

## Examples

You can view examples of conversions done with Hone in the [examples](/examples) directory.
### CSV
| name  | birth day | birth month | birth year | reference | reference name | 
|-------|-----------|-------------|------------|-----------|----------------| 
| Bob   | 7         | May         | 1985       | TRUE      | Smith          | 
| Julia | 21        | January     | 1997       | FALSE     | N/A            | 
| Rick  | 12        | June        | 1996       | TRUE      | Clara          | 
### Nested JSON
```
[{
	"reference name": "Clara",
	"reference": "TRUE",
	"birth": {
		"year": "1996",
		"month": "June",
		"day": "12"
	},
	"name": "Rick"
}, {
	"reference name": "Clara",
	"reference": "TRUE",
	"birth": {
		"year": "1996",
		"month": "June",
		"day": "12"
	},
	"name": "Rick"
}, {
	"reference name": "Clara",
	"reference": "TRUE",
	"birth": {
		"year": "1996",
		"month": "June",
		"day": "12"
	},
	"name": "Rick"
}]
``
