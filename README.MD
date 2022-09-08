# Challenge Texo IT

This project is an implementation of features to provide:

- Read some CSV file and populate a database at application start
- Obtain a producer with the longest interval between two consecutive awards, and what
got two awards faster

The CSV file MUST HAVE this structure example:

```txt
year;title;studios;producers;winner
1980;Movie - 1980 - 1;Studio - 1980 - 1;Producer 1;no
1980;Movie - 1980 - 2;Studio - 1980 - 2;Producer 6;no
1980;Movie - 1980 - 3;Studio - 1980 - 3;Producer 8;yes
```

## To Use this project

### Required Technologies

- Python 3.8 or 3.9 versions

### Setup to execute

**First, is mandatory it is mandatory to have it installed Python and Git**

Clone the project:

`git clone https://github.com/armandodelcol-coder/challenge-texoit`

Install the dependencies, in the root folder of project cloned run:

windows: `pip install -r .\requirements.txt`

linux: `pip install -r requirements.txt`

*Have a port 5000 cleared*

Running the project:

`python -m flask run`

With the server up and running, visit the URL on REST client or browser: 

http://localhost:5000/winnersinterval

You should see this result with the default settings:

```json
{
    "max": [
        {
            "followingWin": 2022,
            "interval": 25,
            "previousWin": 1997,
            "producer": "Producer 5"
        }
    ],
    "min": [
        {
            "followingWin": 2013,
            "interval": 1,
            "previousWin": 2012,
            "producer": "Producer 3"
        },
        {
            "followingWin": 2008,
            "interval": 1,
            "previousWin": 2007,
            "producer": "Producer 10"
        }
    ]
}
```

#### Test

This project has a simple integration test that checks through an http request the default results according to the test CSV file.

To run tests, be in root directory and run:

`python -m pytest`

### Instructions to use another CSV file

The CSV file MUST HAVE the default structure example.

You can create a CSV file by execute the `script_create_csv.py` in the resources folder

or

You can use the csv file with custom  Golden Raspberry Awards data.

*I suggest putting the file in the resources' folder to make it easier*

**In the app.py file (located in the root folder), change de variable default_csv_file_path**

Ex:

Default: `default_csv_file_path = Path("resources/goldenraspawardslist.csv")`

Custom: `default_csv_file_path = Path("resources/yourcscfile.csv")`

### Conclusion

This project is a basic code to solve the proposed problem, but there are N other ways to solve it and, of course, better ways too.

That way, is my initial proposal with 12 hours of work.

Thank You.