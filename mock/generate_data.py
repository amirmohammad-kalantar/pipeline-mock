import requests
from typing import Dict


def get_data(url: str = "https://randomuser.me/api/",
             num_data: int = 1) -> Dict[str, str]:
    return requests.get(f"{url}?results={num_data}").json()
