# generated by datamodel-codegen:
#   filename:  ResultEvent.yaml
#   timestamp: 2024-11-22T20:54:00+00:00

from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, RootModel
from typing_extensions import Annotated


class RecordUnknown(RootModel[Optional[Dict[str, Any]]]):
    root: Optional[Dict[str, Any]] = None


class ResultEvent(BaseModel):
    kind: str
    queryId: Annotated[
        str, Field(description='The ID of the query that the event originated from')
    ]
    sequence: Annotated[int, Field(description='The sequence number of the event')]
    sourceTimeMs: Annotated[
        int, Field(description='The time at which the source change was recorded')
    ]
    metadata: Optional[RecordUnknown] = None
