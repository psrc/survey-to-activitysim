import pandera as pa


class PersonSchema(pa.DataFrameModel):
    person_id: int = pa.Field()
    age: int = pa.Field(ge=0, le=85)
    student: int = pa.Field(ge=0, le=2)
    ptype: int = pa.Field(ge=0, le=10)
    sex: int = pa.Field(isin=[1, 2, 9])

    class Config:
        strict = True
