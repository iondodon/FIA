## Tourist type Expert System detector


### Environment
Python 3.8.5

### Run
```shell
$ python main.py
```

### Execution result example

```shell
has a map? (y/n): n
has a backpack? (y/n): n
wears a hat? (y/n): n
has a camera? (y/n): n
likes Trump? (y/n): n
likes Biden? (y/n): n
fast walk? (y/n): n
has expensive clothes? (y/n): n
has simple clothes? (y/n): n
No tourist type found, probably a loonie
```

```shell
has a map? (y/n): n
has a backpack? (y/n): y

HAS A BACKPACK
HAS TRAVEL STUFF WITH HIM, because has a backpack
wears a hat? (y/n): n
has a camera? (y/n): y

HAS A CAMERA
HAS TRAVEL STUFF WITH HIM, because has a camera
looks around a lot? (y/n): y

LOOKS AROUND A LOT
EXCITED, because looks around a lot
smiles? (y/n): n

TOURIST
PERSON, because tourist
likes Trump? (y/n): y

REPUBLICAN TOURIST
PERSON, because republican tourist
likes Biden? (y/n): n
fast walk? (y/n): n
has expensive clothes? (y/n): y

RICH TOURIST
PERSON, because rich tourist
has simple clothes? (y/n): y

MODEST TOURIST
PERSON, because modest tourist
Tourist types printed above

```
