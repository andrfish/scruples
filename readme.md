Scruples
========
A corpus and code for understanding norms and subjectivity.

This repository is for the paper: [*Scruples: A Corpus of Community Ethical
Judgments on 32,000 Real-life Anecdotes*][paper]. Scruples provides datasets for
studying _norm understanding_ in anecdotes and language. This repo contains
code for building and analyzing the Scruples datasets, running the baselines,
demoing the models and the BEST estimator, and using the BEST estimator
directly to estimate the best possible performance on classification datasets.

Jump to a section of this readme to accomplish different goals:

  - [Data](#data): Download the Scruples data.
  - [Demos](#demos): View or run demos for the BEST estimator or the model
    trained to predict people's ethical judgments on anecdotes and moral
    dilemmas.
  - [Setup](#setup): Install the code in this repository.
  - [Quickstart](#quickstart): Get started running the code in this repo.
  - [Citation](#citation): Cite the Scruples project.
  - [Contact](#contact): Reach out with questions or comments.
  - [Disclaimer](#disclaimer): Understand the intended purpose of this work as
    well as it's limitations.

In addition, the following documents dive deep into particular topics:

  - [Annotation Guidelines](./docs/annotation-guidelines.md): Learn how we
    annotated data for Scruples to validate the extraction performance.
  - [Demos](./docs/demos.md): Set up and run the demos on your own machine.

**Note: This repository is intended for research purposes only.** It is
NOT intended for use in production environments, and there is no
intention for ongoing maintenance. See the [Disclaimer](#disclaimer)
for more information.


Data
----
Scruples has two primary datasets: the Anecdotes and the Dilemmas.

### Anecdotes

The Anecdotes provide 32,000 anecdotes of real-life situations with
ethical judgments collected from community members about who was in the
wrong. See [Scruples: A Corpus of Community Ethical Judgments on
32,000 Real-life Anecdotes][paper] for more information.

You can download the Anecdotes [here][anecdotes].

### Dilemmas

The Scruples Dilemmas provide 10,000 ethical dilemmas in the form of
paired actions, where the model must identify which one was considered
less ethical by crowd workers on Mechanical Turk. See [Scruples: A
Corpus of Community Ethical Judgments on 32,000 Real-life
Anecdotes][paper] for more information.

You can download the Dilemmas [here][dilemmas].


Demos
-----
Scruples has two demos associated with it.

### Scoracle

Visit [scoracle][scoracle] to compute the BEST (Bayesian Estimated Score
Terminus) performance for a classification dataset. BEST uses the annotations
to estimate the upper bound for how well models can possibly do on a dataset
under various metrics (accuracy, cross entropy, etc.). See [the paper][paper]
for details.

### Norms

The [norms][norms] demo shows how current neural models can learn to predict
basic ethical judgments using the Scruples data. It let's you run anecdotes and
dilemmas through a model to view its predictions. In addition, it visualizes
how Dirichlet-multinomial layers allow models to separate intrinsic from model
uncertainty. [The paper][paper] elaborates on these techniques.

### Running the Demos

Running the demos yourself is quite easy! If you want to run these demos on
your own hardware, check out the [demo documentation](./docs/demos.md).


Setup
-----
This project requires Python 3.7, and was tested with Python 3.7.6
specifically. To setup the project:
    1. Install Ubuntu 18.04.5 LTS from the Microsoft Store (some of the oldest code in this repo is from 2019 so they likely used this version in development)
    2. Once you've set it up, do all updates and install the MySQL as well as C++ compilation packages with:
        sudo apt update && sudo apt upgrade -y && sudo apt install libmysqlclient-dev build-essential manpages-dev -y
    3. Download the Anaconda installer with:
        cd /tmp && curl -O https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
    4. Install Anaconda (make sure to get the installer to initialize it at the end when it prompts you) with:
        bash Anaconda3-2022.10-Linux-x86_64.sh
    5. Relaunch the shell by closing the window and re-opening it, then make a new environment with the version of Python the authors use with:
        conda create -n scruples python=3.7.6
    6. Activate the new environment, update pip, and install PyTorch (the repo will overwrite some of this installation but that's fine) as well as G++ compilation tools with:
        conda activate scruples && pip install --upgrade pip && conda install pytorch torchvision torchaudio -c pytorch && conda install -c conda-forge gxx
    7. Clone the GitHub repository and install it (the period at the end needs to be there, this will take a bit):
        cd ~/ && git clone https://github.com/allenai/scruples.git && cd scruples && pip install --editable .
    8. Install statsmodels (don't worry about any errors/warnings) and downgrade the versions of "transformers", "xgboost", as well as "scipy" (this will overwrite the statsmodels install but that's fine) that was automatically installed with:
        pip install statsmodels transformers==2.1.1 xgboost==1.5.0 scipy==1.2.3
    9. Download the "omw-1.4" dataset with the following sequence of commands (don't worry about any deprecation warnings):
        python -i
        import nltk
        nltk.download('omw-1.4')
        exit()
    10. Install remaining requirements, download the english model for spacy, and install pytest:
        sed --in-place '/regex/d' requirements.txt && pip install -r requirements.txt && python -m spacy download en && pip install pytest


Quickstart
----------
Once you've [installed the package](#setup), you'll have the Scruples
CLI available. It's a hierarchical, self-documenting CLI that contains
all the commands necessary to build and analyze Scruples:

    $ scruples --help
    Usage: scruples [OPTIONS] COMMAND [ARGS]...

      The command line interface for scruples.

    Options:
      --verbose  Set the log level to DEBUG.
      --help     Show this message and exit.

    Commands:
      analyze   Run an analysis.
      demo      Run a demo's server.
      evaluate  Evaluate models on scruples.
      make      Make different components of scruples.

To build the dataset, you'll need to download the reddit
[posts][reddit-posts] and [comments][reddit-comments]. The initial
version of Scruples used November 2018 through April 2019.

Also, Scruples comes with demos that you can run and view locally in the
browser:

    $ scruples demo --help
    Usage: scruples demo [OPTIONS] COMMAND [ARGS]...

      Run a demo's server.

    Options:
      --help  Show this message and exit.

    Commands:
      norms     Serve the norms demo.
      scoracle  Serve the scoracle demo.


Citation
--------
If you build off of this code, data, or work, please cite [the paper][paper] as
follows:

    @article{Lourie2020Scruples,
        author = {Nicholas Lourie and Ronan Le Bras and Yejin Choi},
        title = {Scruples: A Corpus of Community Ethical Judgments on 32,000 Real-Life Anecdotes},
        journal = {arXiv e-prints},
        year = {2020},
        archivePrefix = {arXiv},
        eprint = {2008.09094},
    }


Contact
-------
For public, non-sensitive questions and concerns, please file an issue
on this repository.

For private or sensitive inquiries email mosaic on the allenai.org
website.


Disclaimer
----------
**This code and corpus is intended for research purposes only**.

As AI agents become more autonomous, they must understand and apply
human ethics, values, and norms. One step towards better _norm
understanding_ is to reproduce normative judgments drawn from various
communities. This skill would enable computers to anticipate people's
reactions and understand deeper situational context.

Scruples encourages progress on this research problem by providing a
corpus of real-world ethical situations with community sourced normative
judgments. The norms expressed by this corpus represent those of the
community from which they're drawn&mdash;and thus they are neither
representative of other communities nor necessarily the right norms to use in
any particular application scenario.

Any organization looking to incorporate normative understanding into a
product or service should carefully consider, investigate, and evaluate
which norms are correct for their particular application.


[anecdotes]: https://storage.googleapis.com/ai2-mosaic-public/projects/scruples/v1.0/data/anecdotes.tar.gz
[dilemmas]: https://storage.googleapis.com/ai2-mosaic-public/projects/scruples/v1.0/data/dilemmas.tar.gz
[norms]: https://norms.apps.allenai.org/
[paper]: https://arxiv.org/abs/2008.09094
[pytorch]: https://pytorch.org/
[reddit-comments]: http://files.pushshift.io/reddit/comments/
[reddit-posts]: http://files.pushshift.io/reddit/submissions/
[scoracle]: https://scoracle.apps.allenai.org/
