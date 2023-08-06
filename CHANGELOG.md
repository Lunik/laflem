# CHANGELOG

## v0.2.0

### Features

- Upgrade the `git.setup` module :
 - Add new aliases for `git` commands : `plr`, `rh`, `t`
- Add a new `lf` alias binary
- Display binary & module versions when printing the help message

### Changes

- Move the `laflem` script to a package "entry point"
- Move `git` collection constants outside of module files

### Fixes

- Add lint on `setup.py` file


## v0.1.2

### Fixes

- Fix error message interpolation when CLI parsing fails
- Fix extra packages during module requirements installation


## v0.1.1

### Fixes

- Update package version to prevent Pypi conflict error during upload


## v0.1.0

### Features

- Initial release
- Added `base` collection with `helloworld` and `ask` modules
- Added `git` collection with `setup` module
