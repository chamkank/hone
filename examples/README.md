### Input: `example_a.csv`
```
name,age (years),weight (kg),birth day,birth month,birth year,adopted,adopted_since
Tommy,5,3.6,11,April,2011,TRUE,2012
Clara,2,8.2,6,May,2015,FALSE,N/A
Catnip,6,3.3,21,August,2011,TRUE,2017
Ciel,3,3.1,18,January,2015,TRUE,2018
```
### Output: `example_a.json`
```
[
  {
    "adopted": "TRUE",
    "adopted_since": "2018",
    "age (years)": "3",
    "birth": {
      "day": "18",
      "month": "January",
      "year": "2015"
    },
    "name": "Ciel",
    "weight (kg)": "3.1"
  },
  {
    "adopted": "TRUE",
    "adopted_since": "2018",
    "age (years)": "3",
    "birth": {
      "day": "18",
      "month": "January",
      "year": "2015"
    },
    "name": "Ciel",
    "weight (kg)": "3.1"
  },
  {
    "adopted": "TRUE",
    "adopted_since": "2018",
    "age (years)": "3",
    "birth": {
      "day": "18",
      "month": "January",
      "year": "2015"
    },
    "name": "Ciel",
    "weight (kg)": "3.1"
  },
  {
    "adopted": "TRUE",
    "adopted_since": "2018",
    "age (years)": "3",
    "birth": {
      "day": "18",
      "month": "January",
      "year": "2015"
    },
    "name": "Ciel",
    "weight (kg)": "3.1"
  }
]
```
***
### Input: `example_b.csv`
```
a,a_b,b_c_d,b_c_e,b_d_e,b_d_f
1,2,3,4,5,6
7,8,9,10,11,12
```

### Output: `example_b.json`
```
[
  {
    "a": "7",
    "a_b": "8",
    "b": {
      "c": {
        "d": "9",
        "e": "10"
      },
      "d": {
        "e": "11",
        "f": "1"
      }
    }
  },
  {
    "a": "7",
    "a_b": "8",
    "b": {
      "c": {
        "d": "9",
        "e": "10"
      },
      "d": {
        "e": "11",
        "f": "1"
      }
    }
  }
]
```
***
### Input: `example_c.csv`
```
name,birth day,birth month,birth year,reference,reference name
Bob,7,May,1985,TRUE,Smith
Julia,21,January,1997,FALSE,N/A
Rick,12,June,1996,TRUE,Clara
```

### Output: `example_c.json`
```
[
  {
    "birth": {
      "day": "12",
      "month": "June",
      "year": "1996"
    },
    "name": "Rick",
    "reference": "TRUE",
    "reference name": "Clara"
  },
  {
    "birth": {
      "day": "12",
      "month": "June",
      "year": "1996"
    },
    "name": "Rick",
    "reference": "TRUE",
    "reference name": "Clara"
  },
  {
    "birth": {
      "day": "12",
      "month": "June",
      "year": "1996"
    },
    "name": "Rick",
    "reference": "TRUE",
    "reference name": "Clara"
  }
]
```
