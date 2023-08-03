from openff.models.models import DefaultModel
from openff.models.types import FloatQuantity
from openff.units import Quantity, unit


class Model(DefaultModel):
    x: int
    y: str
    z: FloatQuantity["angstrom"] = Quantity(2.5, unit.angstrom)


model = Model(x=1, y="a", z=Quantity(3.5, unit.angstrom))

assert model.x == 1
assert model.y == "a"
assert model.z.m_as(unit.nanometer) == 0.35
