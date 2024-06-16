from dataclasses import dataclass

@dataclass
class APIEndpoint:
    name: str
    url: str
    parameters: dict[str, str]

class APIConfig:
    API_TOKEN: str = "your_api_token"

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