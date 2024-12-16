import httpx
import pandas as pd

from app.config.config import DATA_DIR
from app.config.config import headers


async def response_data(report_type: int = 3, report_type_name: str = "Roster") -> str:

    url = f"https://fantasyhelper.net/Yahoo/431.l.12345/Data/ViewData?ReportType={report_type}&FileFormat=0"
    filename = (
        f"{report_type_name}_{pd.Timestamp.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    )

    response = httpx.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        new_df = df["data"]
        transposed_df = new_df.apply(pd.Series).T
        transposed_df.to_csv(
            f"{DATA_DIR}/{filename}",
            index=False,
        )
        return f" Data of file {filename} saved successfully "
    return f"Failed to fetch data status {response.status_code}"
