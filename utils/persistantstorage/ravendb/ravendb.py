import socket

from pyravendb.store import document_store


class ravendb:
    def __init__(self, database_name: str, database_urls: list = None):
        if database_urls is None:
            database_urls = ["http://localhost:8080"]

        self.database_urls = database_urls
        self.db = document_store.DocumentStore(urls=database_urls, database=database_name)
        self.db.initialize()

    def get_server_info(self):
        info = {"servers": self.database_urls}
        server_ip = []
        for url in self.database_urls:
            url = url.split(":")
            url = url[1].split("//")
            ip_address = socket.gethostbyname(url[1])
            server_ip.append(ip_address)
        info["server_ip"] = server_ip
        return info

    def get_one(self, document_name: str, obj_type: object = None):
        with self.db.open_session() as doc:
            if obj_type is None:
                return doc.load(document_name)
            else:
                return doc.load(document_name, object_type=obj_type)

    def get_lots(self, document_name: list, obj_type: object):
        with self.db.open_session() as doc:
            return doc.load(document_name, object_type=obj_type)

    def delete_one(self, document_name: str):
        with self.db.open_session() as doc:
            return doc.delete(document_name)

    def delete_lots(self, document_name: list):
        with self.db.open_session() as doc:
            return doc.delete(document_name)

    def insert_one(self, obj_document: object):
        with self.db.open_session() as doc:
            doc.store(obj_document)
            doc.save_changes()

    def query_object_type(self, document_obj: object):
        with self.db.open_session() as session:
            return list(session.query(object_type=document_obj))

    def query_key_value(self, key: str, value):
        with self.db.open_session() as session:
            return list(
                session.query().where_equals(
                    key,
                    value
                )
            )

    def query_object_type_key_value(self, document_obj: object, key: str, value):
        with self.db.open_session() as session:
            return list(
                session.query(object_type=document_obj).where_equals(
                    field_name=key,
                    value=value
                )
            )
