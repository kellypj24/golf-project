import os

from dataclasses import dataclass

@dataclass
class APIEndpoint:
    name: str
    url: str
    parameters: dict[str, str]

class APIConfig:
    API_TOKEN: str = os.environ.get("DATAGOLF_API_TOKEN")

    MATCHUPS = APIEndpoint(
        name="matchups",
        url="https://feeds.datagolf.com/betting-tools/matchups?tour={tour}&market={market}&odds_format={odds_format}&file_format={file_format}&key={API_TOKEN}",
        parameters={
            "tour": "pga",
            "market": "tournament_matchups",
            "odds_format": "decimal",
            "file_format": "csv",
        },
    )

    MATCHUPS_ALL_PAIRINGS = APIEndpoint(
        name="matchups_all_pairings",
        url="https://feeds.datagolf.com/betting-tools/matchups-all-pairings?tour={tour}&odds_format={odds_format}&file_format={file_format}&key={API_TOKEN}",
        parameters={
            "tour": "pga",
            "odds_format": "decimal",
            "file_format": "csv",
        },
    )

    OUTRIGHTS = APIEndpoint(
        name="outrights",
        url="https://feeds.datagolf.com/betting-tools/outrights?tour={tour}&market={market}&odds_format={odds_format}&file_format={file_format}&key={API_TOKEN}",
        parameters={
            "tour": "pga",
            "market": ["win", "top_5", "top_10", "top_20", "mc", "make_cut", "frl"],
            "odds_format": "decimal",
            "file_format": "csv",
        },
    )