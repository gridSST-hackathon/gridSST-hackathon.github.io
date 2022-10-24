# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Grid SST Hackathon'
copyright = '2022, Grid SST Hackathon'
author = 'gridsst hackathon contributors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    #"myst_parser", # enable sphinx to render markdown files
    "myst_nb", # render jupyter notebook tutorials
    "sphinx.ext.autosectionlabel", # automatically make markdown headers referencable 
    "sphinx_design",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Grid SST Hackathon"
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_theme_options = {
    "search_bar_text": "Search this site...",
    "navbar_end": ["search-field.html", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/gridSST-hackathon",
            "icon": "fab fa-github-square",
        }
    ]
}
html_sidebars = {
    "index": [
        "logo.html"
    ],
    "**": [
        "logo.html",
        "sidebar-nav-bs.html"
    ]
}


# linkcheck_allowed_redirects = {
#     # All HTTP redirections from the source URI to the canonical URI will be treated as "working".
#     r'https://sphinx-doc\.org/.*': r'https://sphinx-doc\.org/en/master/.*'
# }