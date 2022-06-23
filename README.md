# Search song

Search song is a Python tool for searching music via Yousician.

## Installation

Use the package manager pip to install Search song.

```bash
cd search-songs
pip install .
```

## Usage

Run tool via cli.
```bash
search-songs yourText
```
Use quotes if you text includes spaces
```bash
search-songs 'Richard Wagner'
```

## Tests

All test located in test directory.
Before running tests set test requirements.
```bash
pip install -r requirements-test.txt
```
And run test

```commandline
pytest
```