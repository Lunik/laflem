# LaFlem

## Description

LaFlem is a simple, easy to use, and lightweight Python binary for creating and managing recuring task in the life of an IT guy. It is designed to be easy to use and easy to understand. It is also designed to be lightweight and fast. It is not designed to be a full fledged task manager, but rather a simple tool to help you manage your day to day tasks.

## Installation

To install LaFlem, simply run the following command:

```bash
pip install --user laflem
```

or with an isolated environment:

```bash
python -m venv ~/bin/laflem_venv
~/bin/laflem_venv/bin/pip install laflem

ln -s ~/bin/laflem_venv/bin/laflem ~/bin/laflem
ln -s ~/bin/laflem_venv/bin/lf ~/bin/lf
```

## Usage

To use LaFlem, simply run the following command :

```bash
laflem --help
```

or with the alias :

```bash
lf --help
```

## Contributing

To contribute to LaFlem, simply fork the repository and create a pull request. Please make sure to include a detailed description of your changes. Here are the things I will check during the review :

- Is CHANGELOG.md have been updated (**required**)
- Is the lint score did not decrease (**required**)
- Is the test coverage did not decrease (**required**)
- Is the documentation have been updated (**if required**)
- If tests have been added (**optional**)

### Development

This repository uses [Taskfile](https://taskfile.dev) to manage the development tasks. To see the available tasks, run the following command:

```bash
task --list
```