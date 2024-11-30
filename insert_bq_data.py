import os
from typing import Dict

from google.cloud import bigquery
from dotenv import load_dotenv # type: ignore
from google.oauth2 import service_account # type: ignore

load_dotenv("/app/.env")
credentials = service_account.Credentials.from_service_account_file(
    os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))


def insert_data(data: Dict) -> None:
    table_id = os.getenv("TABLE_ID")
    client = bigquery.Client(
        project=os.getenv("PROJECT"),
        credentials=credentials
        )
    # Insert rows
    errors = client.insert_rows_json(
        table_id, data
    )
    if errors != []:
        print("Encountered errors while inserting rows: {}".format(errors))
