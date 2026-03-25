from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_status import FileStatus

@dataclass
class File(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The created_at property
    created_at: Optional[str] = None
    # The format property
    format: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The project_id property
    project_id: Optional[str] = None
    # The size property
    size: Optional[int] = None
    # The status property
    status: Optional[FileStatus] = None
    # The updated_at property
    updated_at: Optional[str] = None
    # The url property
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> File:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: File
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return File()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .file_status import FileStatus

        from .file_status import FileStatus

        fields: dict[str, Callable[[Any], None]] = {
            "created_at": lambda n : setattr(self, 'created_at', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "project_id": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(FileStatus)),
            "updated_at": lambda n : setattr(self, 'updated_at', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("created_at", self.created_at)
        writer.write_str_value("format", self.format)
        writer.write_str_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("project_id", self.project_id)
        writer.write_int_value("size", self.size)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("updated_at", self.updated_at)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

