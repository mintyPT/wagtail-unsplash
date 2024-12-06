# [Wagtail Unsplash](https://pypi.org/project/wagtail-unsplash/) [![PyPI](https://img.shields.io/pypi/v/wagtail-unsplash.svg)](https://pypi.org/project/wagtail-unsplash/)

[![Release](https://img.shields.io/github/v/release/mintyPT/wagtail-unsplash)](https://img.shields.io/github/v/release/mintyPT/wagtail-unsplash)
[![Build status](https://img.shields.io/github/actions/workflow/status/mintyPT/wagtail-unsplash/main.yml?branch=main)](https://github.com/mintyPT/wagtail-unsplash/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/mintyPT/wagtail-unsplash/branch/main/graph/badge.svg)](https://codecov.io/gh/mintyPT/wagtail-unsplash)
[![Commit activity](https://img.shields.io/github/commit-activity/m/mintyPT/wagtail-unsplash)](https://img.shields.io/github/commit-activity/m/mintyPT/wagtail-unsplash)
[![License](https://img.shields.io/github/license/mintyPT/wagtail-unsplash)](https://img.shields.io/github/license/mintyPT/wagtail-unsplash)

![Screenshot showing wagtail-unsplash search results](https://i.imgur.com/Va0kCys.png)

Search for Unsplash images and upload to the Wagtail image library.

This package uses the [python-unsplash](https://github.com/yakupadakli/python-unsplash) API wrapper

- **Github repository**: <https://github.com/mintyPT/wagtail-unsplash/>
- **Documentation** <https://mintyPT.github.io/wagtail-unsplash/>

## Getting started

Install using pip:

```sh
pip install wagtail-unsplashed
```

After installing the package, add `wagtail_unsplashed` to installed apps in your settings file:

```python
# settings.py

INSTALLED_APPS = [
    ...
    'wagtail_unsplashed',
    ...
]
```

and add the API credentials:

```python
# settings.py
WAGTAIL_UNSPLASHED = {
    "CLIENT_ID": "",
    "CLIENT_SECRET": ""
}
```

You can get the needed information by creating an application at https://unsplash.com/developers

## Getting started (development)

### Pull the repo

```bash
git clone git@github.com:mintyPT/wagtail-unsplash.git
```

### Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### After pushing

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/codecov/).

## Releasing a new version

- Create an API Token on [PyPI](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/mintyPT/wagtail-unsplash/settings/secrets/actions/new).
- Create a [new release](https://github.com/mintyPT/wagtail-unsplash/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-uv/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv).
