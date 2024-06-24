from asyncflows import Action, BaseModel, Field

import aiohttp


class Inputs(BaseModel):
    input_string: str


class Outputs(BaseModel):
    reversed_string: str


class MyReverseStringAction(Action[Inputs, Outputs]):
    name = 'my_reverse_string'

    async def run(self, inputs: Inputs) -> Outputs:
        reversed_string = inputs.input_string[::-1]
        return Outputs(reversed_string=reversed_string)
