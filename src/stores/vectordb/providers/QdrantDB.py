from qdrant_client import models, QdrantClient
from ..VectorDBInterface import VectorDBInterface
from ..VectorDBEnums import DistanceMethodEnums
import logging


class QdrantDB(VectorDBInterface):
    def __init__(self, db_path: str, distance_method: str):

        self.client = None
        self.db_path = db_path
        self.distance_method = None

        if distance_method == DistanceMethodEnums.COSINE.value:
            self.distance_method = models.Distance.COSINE
        elif distance_method == DistanceMethodEnums.DOT.value:
            self.distance_method = models.Distance.DOT

        self.logger = logging.getLogger(__name__)

    def connect(self):
        self.client = QdrantClient(path=self.db_path)

    def disconnect(self):
        self.client = None

    def insert_one(self, collection_name, text, vector, metadata=None, record_ids=None):
        if not self.is_collection_existed(collection_name):
            self.logger.error(
                f"Can not insert new record to non-exist collection: {collection_name}"
            )
            return False
        try:
            _ = self.client.upload_records(
                collection_name=collection_name,
                records=[
                    models.Record(
                        vector=vector, payload={"text": text, "metadata": metadata}
                    )
                ],
            )
        except Exception as e:
            self.logger.error(f"Error while inserting batch: {e}")
            return False
        return True

    def insert_many(
        self,
        collection_name,
        texts,
        vectors,
        metadata=None,
        record_ids=None,
        batch_size=50,
    ):

        if metadata is None:
            metadata = [None] + len(texts)

        if record_ids is None:
            record_ids = [None] + len(texts)

        for i in range(0, len(texts), batch_size):
            batch_end = i + batch_size

            batch_texts = texts[i:batch_end]
            batch_vectors = vectors[i:batch_end]
            batch_metadata = metadata[i:batch_end]

            batch_records = [
                models.Record(
                    vector=batch_vectors[x],
                    payload={"text": batch_texts[x], "metadata": batch_metadata[x]},
                )
                for x in range(len(batch_texts))
            ]

            try:
                _ = self.client.upload_records(
                    collection_name=collection_name,
                    records=batch_records,
                )

            except Exception as e:
                self.logger.error(f"Error while inserting batch: {e}")
                return False

        return True

    def search_by_vector(self, collection_name, vector, limit: int = 5 ):
        return self.client.search(
            collection_name=collection_name, query_vector=vector, limit=limit
        )
