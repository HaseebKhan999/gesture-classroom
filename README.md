# Gesture-Based Classroom Control

CS-337 HCI group project (NUST SEECS). Control a PowerPoint slideshow
with hand gestures and voice commands.

Team: Laiba Murtaza, Ali Irtaza, Haseeb Iqbal

## Python version

**Python 3.11** on all three laptops.

## Setup (Windows)

    git clone https://github.com/HaseebKhan999/gesture-classroom.git
    cd gesture-classroom
    py -3.11 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python scripts/scaffold.py
    pip install -r requirements/core.txt -r requirements/<your-module>.txt -r requirements/dev.txt
    python -m pytest -q

Install only your own module's requirements file. `scaffold.py` is safe to
rerun and creates the local `data/` folders (not tracked by git).

## Working rules

- One maintainer per folder (see `.github/CODEOWNERS`).
- Modules talk only through the event bus and `core/contracts.py`. No module imports another.
- Branch names: `person/module`, for example `haseeb/actions`.
- Every morning: `git fetch origin && git rebase origin/main`.
- Open small PRs into `main`. Run `python -m pytest -q` before merging.
- `main` must always run. If you break it, fix it first.
- To change `core/`, open a PR that touches only `core/`, label it `contract-change`, and get both others to approve.