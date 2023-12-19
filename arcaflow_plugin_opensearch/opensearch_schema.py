from dataclasses import dataclass
import enum
import typing
from arcaflow_plugin_sdk import schema, validation, plugin


class OperationType(enum.Enum):
    CREATE = "create"
    DELETE = "delete"
    INDEX = "index"
    UPDATE = "update"


@dataclass
class OperationMeta:
    _index: typing.Annotated[
        typing.Optional[str],
        schema.name("index"),
        schema.description(
            "Optional name of the index that will receive the data. "
            "If none is provided, the default index will be used."
        ),
    ] = None
    _id: typing.Annotated[
        typing.Optional[str],
        schema.name("ID"),
        schema.description("Optional ID for the data document."),
    ] = None


@dataclass
class Operation:
    operation: typing.Annotated[
        # typing.Dict[OperationType, BulkUploadOperationMeta],
        # Temporarily changing the key to a string in order to work
        # around a workflow validation failure for the enum as a key
        typing.Dict[str, OperationMeta],
        schema.name("operation"),
        schema.description("The operation type and associated operation metadata."),
    ]


@dataclass
class BulkUploadObject(Operation):
    data: typing.Annotated[
        typing.Dict[str, typing.Any],
        schema.name("data"),
        schema.description("The JSON data document to upload to your index."),
    ]


bulk_upload_object_schema = plugin.build_object_schema(BulkUploadObject)


@dataclass
class BulkUploadList:
    bulk_upload_list: typing.Annotated[
        typing.List[BulkUploadObject],
        schema.name("bulk upload list"),
        schema.description("The list of objects for the bulk upload operation."),
    ]


@dataclass
class DocumentRequest(BulkUploadList):
    url: typing.Annotated[
        str,
        schema.name("url"),
        schema.description("The URL for the Opensearch-compatible instance."),
    ]
    default_index: typing.Annotated[
        str,
        validation.min(1),
        schema.name("index"),
        schema.description("Name of the default index that will receive the data."),
    ]
    metadata: typing.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        schema.name("metadata"),
        schema.description(
            "Optional global metadata object that will be added " "to every document."
        ),
    ] = None
    username: typing.Annotated[
        typing.Optional[str],
        validation.min(1),
        schema.name("username"),
        schema.description(
            "A username for an authorized user for the given "
            "Opensearch-compatible instance."
        ),
    ] = None
    password: typing.Annotated[
        typing.Optional[str],
        schema.name("password"),
        schema.description("The password for the given user."),
    ] = None
    tls_verify: typing.Annotated[
        typing.Optional[bool],
        schema.name("TLS verify"),
        schema.description(
            "For development and testing purposes, this can be set to False to disable "
            "TLS verification for connections to Opensearch-compatible services."
        ),
    ] = True


@dataclass
class DataList(Operation):
    data_list: typing.Annotated[
        typing.List[typing.Any],
        schema.name("data list"),
        schema.description("List of data object to process into the bulk_upload_list."),
    ]


@dataclass
class SuccessOutput:
    message: str
    document_ids: typing.List[str]


@dataclass
class ErrorOutput:
    error: str
