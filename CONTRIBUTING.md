<!-- omit in toc -->
# Contributing to mendeleev

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Share it over social media
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues
> - Cite the project in academic papers if you've used it in your research

<!-- omit in toc -->
## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
  - [I Want To Contribute](#i-want-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
  - [Commit Messages](#commit-messages)


## Code of Conduct

This project and everyone participating in it is governed by the
[mendeleev Code of Conduct](https://github.com/lmmentel/mendeleev/blob/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable behavior
to @lmmentel.


## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation](https://mendeleev.readthedocs.io/).

Before you ask a question, it is best to search for existing [Discussions](https://github.com/lmmentel/mendeleev/discussions) that might help you. In case you have found a suitable thread and still need clarification, you can write your question in this thread. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Discussion](https://github.com/lmmentel/mendeleev/discussions/new/choose).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (operating system, python version, mendeleev version), depending on what seems relevant.

We will then contribute to the discussion as soon as possible.


## I Want To Contribute

> ### Legal Notice <!-- omit in toc -->
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project licence.

### Reporting Bugs

<!-- omit in toc -->
#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](https://mendeleev.readthedocs.io/). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/lmmentel/mendeleev/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the interpreter, package manager, depending on what seems relevant.
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?

<!-- omit in toc -->
#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to [mendeleev-python@pm.me](mailto:mendeleev-python@pm.me).
<!-- You may add a PGP key to allow the messages to be sent encrypted as well. -->

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/lmmentel/mendeleev/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=). 
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).

<!-- You might want to create an issue template for bugs and errors that can be used as a guide and that defines the structure of the information to be included. If you do so, reference it here in the description. -->


### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for mendeleev, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<!-- omit in toc -->
#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://mendeleev.readthedocs.io/) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/lmmentel/mendeleev/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

<!-- omit in toc -->
#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/lmmentel/mendeleev/issues). Open a [Feature Request](https://github.com/lmmentel/mendeleev/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots or screen recordings** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [LICEcap](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and the built-in [screen recorder in GNOME](https://help.gnome.org/users/gnome-help/stable/screen-shot-record.html.en) or [SimpleScreenRecorder](https://github.com/MaartenBaert/ssr) on Linux. <!-- this should only be included if the project has a GUI -->
- **Explain why this enhancement would be useful** to most mendeleev users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

<!-- You might want to create an issue template for enhancement suggestions that can be used as a guide and that defines the structure of the information to be included. If you do so, reference it here in the description. -->

### Your First Code Contribution
<!-- TODO
include Setup of env, IDE and typical getting started instructions?

-->

#### Prerequsites

- [git](https://git-scm.com/) version control
- [poetry](https://python-poetry.org/) for dependency and environment management

#### Local setup

1. Fork the repository 

Start by forking the [mendeleev](https://github.com/lmmentel/mendeleev) repository on GitHub to your account. This will create your copy of the project where you can make changes.

2. Clone the Repository

Clone your forked repository to your local machine:

```bash
git clone https://github.com/lmmentel/mendeleev.git
```

Navigate to the project directory:

```
cd mendeleev
```

3. Development installation

```bash
poetry install
```

#### Adding new or extending existing models

Mendeleev uses [SQLAlechmy](https://www.sqlalchemy.org/) for the data models and schema management. Adding a new model or adding/changing a property
of an existing model requires a data migration. Migration are handled by [alembic](https://alembic.sqlalchemy.org/en/latest/), to create a new migration (called revision in alembic lingo):

```bash
alembic revision -m "[your summary of changes here]"
```

This will generate a revision file that you'll need to populate with desired logic. As a reference please look at previous migratons in ``alembic/versions``.

Once your migration code is ready run:

```bash
alembic migrate head
```

which should apply the changes to the ``mendeleev/elements.db`` database.

### Improving The Documentation

Documentation is build with [Sphinx](https://www.sphinx-doc.org/en/master/) and [reStructuredText](https://docutils.sourceforge.io/rst.html). Once you [setup your local environment](#local-setup) you can build the documentation locally with:

```bash
cd docs
make html
```

Results and placed in ``build/_html`` and you can open ``build/_html/index.html`` with your favorite browser to see the results.

Documentation of available [data points](https://mendeleev.readthedocs.io/en/stable/data.html) are require an extra step where metadata from
the [PropertyMetadata](https://mendeleev.readthedocs.io/en/stable/api/models.html#propertymetadata) model is rendered into rst format  as ``docs/source/data.rst`` file. To generate an upadted version of ``data.rst`` after updating ``PropertyMetadata`` run:

```bash
inv render-data-docs
```

Inspect the ``data.rst`` file before committing to check that everyting looks correct.

## Styleguides
### Commit Messages
<!-- TODO

-->


<!-- omit in toc -->
## Attribution
This guide is based on the [contributing.md](https://contributing.md/generator)!
