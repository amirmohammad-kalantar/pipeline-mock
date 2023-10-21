import requests
from typing import Dict
import json


def get_data(url: str = "https://randomuser.me/api/",
             num_data: int = 1) -> Dict[str, str]:
    return requests.get(f"{url}?results={num_data}").json()


if __name__ == "__main__":
    data = get_data(num_data=5)
    with open('user-data.json', 'w') as f:
        json.dump(data, f)



