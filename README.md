# Installation

Download `shorten` somewhere in your PATH.
For example, if ~/.local/bin/ is in your PATH:

```sh
$ wget https://raw.githubusercontent.com/sbivol/shorten/master/shorten --directory-prefix="$HOME/.local/bin/"
$ chmod a+x ~/.local/bin/shorten
```

# Usage

This program can be used directly on the command line:

```
$ shorten [[DIRECTION][LENGTH]] STRING
```

Optional parameters:

  * DIRECTION can be **`-`** (cut from the right) or **`+`** (cut from the left)
  * LENGTH must be an integer (defaults to the current terminal width)

It can also be imported and used as a Python module:

```py
>>> from shorten import shorten
>>> print(shorten("loooooong_teeeeeeeext 123123123123a", "-10"))
loooooong…
```

## Shortening strings from standard input

Cut the middle of log lines so that they fit in the current terminal width (for example, 50 characters):

```sh
$ tail -n3 /var/log/syslog | shorten
Jun 15 00:17:01 srv CRON…-report /etc/cron.hourly)
Jun 15 00:17:39 srv kern…, remount, noatime, bind"
Jun 15 00:17:39 srv kern…, remount, noatime, bind"
```

Cut the middle part of lines so they fit within 11 characters:

```sh
$ echo -e "loooooong_teeeeeeeext 123123123123a\nloooooong_teeeeeeeext 123123123123a" | shorten 11
loooo…3123a
loooo…3123a
```

Cut the tails of long lines:

```sh
$ echo -e "loooooong_teeeeeeeext 123123123123a\nloooooong_teeeeeeeext 123123123123a" | shorten -11
loooooong_…
loooooong_…
```

Cut the heads of long lines so that they fit within the current terminal width:

```sh
$ echo -e "loooooong_teeeeeeeext 123123123123a\nloooooong_teeeeeeeext 123123123123a" | shorten +
…ong_teeeeeeeext 123123123123a
…ong_teeeeeeeext 123123123123a
```

## Shortening strings passed as arguments:

Shorten to 20 characters:

```sh
$ shorten -20 "loooooong_teeeeeeeext 123123123123a teeeeeeeext 456456456456b"
loooooong_teeeeeeee…
```

Cut string from the beginning so that it fits on a terminal line (for example, 50 characters):

```sh
$ shorten + "loooooong_teeeeeeeext 123123123123a teeeeeeeext 456456456456b"
…eeeeeeext 123123123123a teeeeeeeext 456456456456b
```
