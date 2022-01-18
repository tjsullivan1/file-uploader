# from datetime import datetime
from typing import Optional
from azure.storage.blob import BlobServiceClient


conenction_string: Optional[str] = None


async def add_file(blob_name, file_contents):
    # now = datetime.now()
    blob_service_client = BlobServiceClient.from_connection_string(conenction_string)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container="test", blob=blob_name)

    return blob_client.upload_blob(file_contents)
