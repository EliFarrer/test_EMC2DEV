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
    "repository_url": "https://github.com/EliFarrer/test_EMC2DEV",  # where your docs live
    "binderhub_url": "https://mybinder.org",
    "branch": "main",
    "kernel_name": "python3",
    "selector": "div.cell",  # This matches jupyter-sphinx cells
}
