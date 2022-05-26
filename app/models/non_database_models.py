import json

from typing import Any, List, Optional, Type, Union
from pydantic import BaseModel


class AppModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    def to_json(self) -> str:
        return self.json()

    def to_dict(self) -> Any:
        return json.loads(self.to_json())


def convert_from_json(
    json_data: Union[Any, List[Any]], model_class: Type[AppModel], many=False
) -> Union[AppModel, List[AppModel]]:
    if many:
        return list(map(model_class.parse_obj, json_data))

    return model_class.parse_obj(json_data)
