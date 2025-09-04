# -- Project info -----------------------------------------------------
project = 'Thebe Demo'
extensions = [
    "jupyter_sphinx",
    "sphinx_thebe",
]

# Basic HTML theme
html_theme = "alabaster"

# Enable Thebe
thebe_config = {
    "repository_url": "https://github.com/EliFarrer/sphinx_thebe",  # where your docs live
    "binderhub_url": "https://mybinder.org",
    "branch": "main",
    "kernel_name": "python3",
    "selector": "div.jupyter_cell",  # This matches jupyter-sphinx cells
}

thebe_default_button = True
thebe_activate = True
thebe_enable = True