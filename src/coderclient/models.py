import pydantic

class LlamaRequest(pydantic.BaseModel):
    prompt: str
    
class PossibleValue(pydantic.BaseModel):
    description: str

class Field(pydantic.BaseModel):
    description: str
    possible_values: dict[str, PossibleValue] | None

    @property
    def jsonschema(self):
        schema: dict[str,str | list[str]] = {"type": "string"}
        if self.possible_values:
            schema["enum"] = [*self.possible_values.keys()]
        return schema

class Codebook(pydantic.BaseModel):
    fields: dict[str, Field]

    @property
    def jsonschema(self):
        return {
            "type": "object",
            "properties": {
                field_name: field.jsonschema for field_name,field in self.fields.items()
            }
        }


