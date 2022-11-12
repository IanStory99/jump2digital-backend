from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    def to_db_model(self, custom_schema):
        return custom_schema(**self.dict())

    class Config:
        orm_mode = True
