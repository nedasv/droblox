# Roblox API Wrapper

This package lets easily use the full range of Roblox api's in a simple way, this is great for beginners.

## Installation

Run the following to install:

```python
pip install droblox
```

## Usage

```python
from droblox import Dget

# Generate a User ID from a string username
Dget.username_to_id("ROBLOX")

# Generate a Users last online date
Dget.last_online_date("mrflimflam") 

# Returns None if no previous usernames or a List of previous usernames
Dget.previous_usernames(username="ROBLOX") or Dget.previous_usernames(id=1)
```

# Developing droblox

```bash
$ pip install -e .[dev]
```
