from pydantic import BaseModel, Field

class BuildRequest(BaseModel):
    user_request: str = Field(
        ..., 
        example="Monte um PC bom e barato para jogar Fortnite e que também sirva para estudar.",
        description="O pedido detalhado do cliente para a montagem do PC."
    )

class BuildResponse(BaseModel):
    build_details: str = Field(
        ..., 
        example="""### Análise do Pedido
Para um PC de bom custo-benefício para Fortnite e estudos, selecionei as seguintes peças...

**Peças Escolhidas:**
- ID: 12312 - Nome: Processador AM5 - Preço: R$0.00
...

**Preço Total: R$550.00**
"""
    )

class ErrorResponse(BaseModel):
    detail: str
