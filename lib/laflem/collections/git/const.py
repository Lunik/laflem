"""
Git module constants
"""

GIT_DEFAULT_CONFIG_PARAMS = [
    ("user", "name", "str", None),
    ("user", "email", "str", None),
    ("core", "editor", "str", "vim"),
    ("core", "pager", "str", "less"),
    ("core", "autocrlf", "str", "input"),
    ("init", "defaultBranch", "str", "master"),
    ("fetch", "prune", "bool", True),
    ("pull", "rebase", "bool", True),
    ("merge", "ff", "bool", True),
    ("push", "autoSetupRemote", "bool", True),
    ("push", "rebase", "str", "preserve"),
]

GIT_GPP_CONFIG_PARAMS = [
    ("user", "signingkey", "str", None),
    ("commit", "gpgsign", "bool", True),
    ("tag", "gpgsign", "bool", True),
    ("push", "gpgsign", "bool", False),
    ("log", "showSignature", "bool", False),
    ("gpg", "program", "str", "gpg2"),
]

GIT_ALIASES_PARAMS = [
    ("alias", "co", "str", "commit --signoff"),
    ("alias", "lo", "str", "log"),
    ("alias", "st", "str", "status"),
    ("alias", "ph", "str", "push"),
    ("alias", "pl", "str", "pull"),
    ("alias", "a", "str", "add"),
    ("alias", "df", "str", "diff"),
    ("alias", "ck", "str", "checkout"),
    ("alias", "mr", "str", "merge --signoff"),
    ("alias", "cp", "str", "cherry-pick --signoff"),
    ("alias", "br", "str", "branch"),
    ("alias", "sh", "str", "stash"),
    ("alias", "plh", "str", "!git pull --rebase && git push"),
    ("alias", "dp", "str", "!git add . && git commit --signoff -m 'Dev' && git push"),
    ("alias", "plr", "str", "!git pull --rebase origin master"),
    ("alias", "rh", "str", "!git reset --hard"),
    ("alias", "t", "str", "tag"),
]
