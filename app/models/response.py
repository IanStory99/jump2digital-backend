from __future__ import annotations
from pydantic.generics import GenericModel
from typing import TypeVar, Generic


T = TypeVar("T")

class Response(GenericModel, Generic[T]):
    success: bool
    message: str
    item: T
