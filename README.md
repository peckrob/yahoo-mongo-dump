# yahoo-mongo-dump

This is a quick script that dumps data archived from [yahoo-groups-backup](https://github.com/hrenfroe/yahoo-groups-backup)
in MongoDB and dumps it into individual files. It dumps a JSON file containing
the full record as well as a plain text file containing the original email.

## Why?

Long term stability. Will you be able to read
that data out of MongoDB in 20 years? I have some files that are younger than
that I can no longer read. Either the program doesn't work anymore, or isn't
supported, or can't even be found. But text files? I can read 40 year old text
files just fine. Pretty good bet text files will be readable in another 40
years as well.

## How To Use

```
$ python3 dump.py --list <list name> --output <output_dir>
```

It will create a year-based directory structure of all messages. Each message is
named in the format `<list>/<year>/<month>-<day>-<id>-<email>.(json|txt)`.

## License

MIT
