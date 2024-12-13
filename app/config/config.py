import os

cookies = {
    ".AspNetCore.Antiforgery.cdV5uW_Ejgc": "CfDJ8Ji7jaY6pqNFso92eRC0rJsDTNREiJ13ssLr6GhksHBD-YpDcGZfY_64Q6xkC76hkCeGxFMgvJzdwaSfwmgn4vkViZ_wjGwPX4JNtHijyQOqHw-g1gSM8oKfis4zVDuX0_SVWakYYs44l6TTxtRlwTc",
    "ARRAffinity": "807d29c96a7efebf0b23cccfe199cb8686534d1ce2ef9afd6232622472f3338e",
    "ARRAffinitySameSite": "807d29c96a7efebf0b23cccfe199cb8686534d1ce2ef9afd6232622472f3338e",
    "_ga_64C2MJKXLE": "GS1.1.1733825950.1.1.1733826299.0.0.0",
    "_ga": "GA1.1.2024589146.1733825951",
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://fantasyhelper.net/Yahoo/431.l.12345/Data",
    "Cookie": ".AspNetCore.Antiforgery.cdV5uW_Ejgc=CfDJ8Ji7jaY6pqNFso92eRC0rJsDTNREiJ13ssLr6GhksHBD-YpDcGZfY_64Q6xkC76hkCeGxFMgvJzdwaSfwmgn4vkViZ_wjGwPX4JNtHijyQOqHw-g1gSM8oKfis4zVDuX0_SVWakYYs44l6TTxtRlwTc; ARRAffinity=807d29c96a7efebf0b23cccfe199cb8686534d1ce2ef9afd6232622472f3338e; ARRAffinitySameSite=807d29c96a7efebf0b23cccfe199cb8686534d1ce2ef9afd6232622472f3338e; _ga_64C2MJKXLE=GS1.1.1733825950.1.1.1733826299.0.0.0; _ga=GA1.1.2024589146.1733825951",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0",
}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
