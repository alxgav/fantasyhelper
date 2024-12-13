from enum import Enum

from fastapi import FastAPI

from app.parser.parser import response_data

import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()


class ReportType(str, Enum):
    TEAM = "Team"
    MATCHUP = "Matchup"
    TRANSACTION = "Transaction"
    ROSTER = "Roster"
    DRAFT = "Draft"
    PLAYERS = "Players"


report_type_index = {
    ReportType.TEAM: 0,
    ReportType.MATCHUP: 1,
    ReportType.TRANSACTION: 2,
    ReportType.ROSTER: 3,
    ReportType.DRAFT: 4,
    ReportType.PLAYERS: 5,
}


@app.get("/data/{report_type}")
async def get_data(report_type: ReportType):

    # logging.info(f"Received report_type: {report_type}")
    #
    index = report_type_index[report_type]
    # logging.info(f"Received index: {index}")

    return {
        "message": await response_data(
            report_type=index, report_type_name=report_type.value
        )
    }


@app.get("/")
async def root():

    return {"message": "app of get data"}
