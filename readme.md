<p align="center">
  <a><img src="https://img.shields.io/badge/Discord-gray.svg" alt="Discord"></a>
  <a><img src="https://img.shields.io/badge/Language-Python3.7+-blue.svg" alt="Python3.7"></a>
  <a><img src="https://img.shields.io/badge/State-Finished-green.svg" alt="Finished"></a>
  <p align="center"><img src="2020-11-18-153742_212x201_scrot.png"></p>
</p>

:warning: Although the risk is low, using a selfbot in discord is against the terms of service and your account *could* be banned, although its highly unlikely from past experience :warning:

A python script that automatically changes your discord status every x seconds

## How to get your token
This video showcases [how to get your token](https://www.youtube.com/watch?v=YEgFvgg7ZPI)

## How to use
```
git clone https://github.com/seksea/auto-status
cd auto-status
pip install -r requirements.txt
vim statuses.txt # Use any text editor
python3 auto-status.py <token> <other args>
```

## Args

| Arg         | Description                            |
| ----------- | -------------------------------------- |
| -d \<time\> | Delay between status change (sec)      |
| -g \<days\> | Have a custom game activity            |
| -s          | Have a custom rickroll stream activity |
| -c \<comp\> | Have a custom 'competing in' activity  |
| -w \<film>  | Have a custom 'watching' activity      |
| -r          | Pick randomly                          |


## Found a bug/want to add something?
- [Create a pull request](https://github.com/seksea/auto-status/issues/new) ([tutorial](https://github.com/yangsu/pull-request-tutorial))
- [Report a bug](https://github.com/seksea/auto-status/issues/new)

