"""
Homebrew module constants
"""
HOMEBREW_INSTALL_SCRIPT_URL = (
    "https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh"
)
HOMEBREW_BIN_PATH = "/opt/homebrew/bin/brew"

HOMEBREW_CASK_PACKAGES = [
    ("arduino", None, True),
    ("bricklink-studio", None, True),
    ("digikam", None, True),
    ("drawio", None, True),
    ("macpass", None, True),
    ("sublime-text", None, True),
    ("vlc", None, True),
    ("daisydisk", None, True),
    ("docker", None, True),
    ("google-chrome", None, True),
    ("raspberry-pi-imager", None, True),
    ("visual-studio-code", None, True),
]
HOMEBREW_PACKAGES = [
    ("ansible", None, False),
    ("ansible-lint", None, False),
    ("awscli", None, False),
    ("azcopy", None, False),
    ("azure-cli", None, False),
    ("git-lfs", None, False),
    ("gitleaks", None, False),
    ("gnupg", None, False),
    ("go-task", "go-task/tap", False),
    ("helm", None, False),
    ("htop", None, False),
    ("jinja2-cli", None, False),
    ("jq", None, False),
    ("k9s", None, False),
    ("kwok", None, False),
    ("nmap", None, False),
    ("node", None, False),
    ("pinentry", None, False),
    ("pinentry-mac", None, False),
    ("poetry", None, False),
    ("postgresql@15", None, False),
    ("python@3.10", None, False),
    ("python@3.11", None, False),
    ("scw", None, False),
    ("skopeo", None, False),
    ("sqlite", None, False),
    ("terraform", None, False),
    ("terraform-docs", None, False),
    ("tmux", None, False),
    ("vault", "hashicorp/tap", False),
    ("virtualenv", None, False),
    ("watch", None, False),
    ("webp", None, False),
    ("wget", None, False),
    ("yq", None, False),
]
