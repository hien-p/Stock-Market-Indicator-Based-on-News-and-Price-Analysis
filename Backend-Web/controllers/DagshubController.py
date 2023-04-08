import os
import pandas as pd
from dagshub.streaming import DagsHubFilesystem

dagshubConfig = {
    "REPO_NAME": "Stock-Indicator-News",
    "REPO_OWNER": "H4438",
    "USER_NAME": "H4438",
    "EMAIL": "www.hao2912@gmail.com",
    "TOKEN": "7d5a95fcb968cb2697edf3cc170dcc576e29a6d2"
}

fs = DagsHubFilesystem()

