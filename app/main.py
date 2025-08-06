from fastapi import FastAPI, HTTPException, Body
import data_loader
import agents 
import schemas

app = FastAPI(
    title="Montador de PC com IA",
    description="Uma API que usa o Gemini para montar um PC a partir de uma lista de componentes disponíveis.",
    version="2.0.0"
)

@app.post(
    "/build-pc",
    response_model=schemas.BuildResponse,
    responses={
        500: {"model": schemas.ErrorResponse},
        503: {"model": schemas.ErrorResponse} 
    },
    summary="Monta um PC baseado no pedido do cliente",
    tags=["Montagem de PC"]
)
def build_pc_endpoint(
    request: schemas.BuildRequest = Body(...)
):
    available_components = data_loader.get_available_components_as_text()

    if available_components is None:
        raise HTTPException(
            status_code=500, 
            detail="Erro interno: Não foi possível carregar a lista de componentes."
        )
    
    if not available_components:
        raise HTTPException(
            status_code=500,
            detail="Erro interno: A lista de componentes disponíveis está vazia."
        )

    try:
        build_result = agents.build_pc_from_components(
            user_request=request.user_request,
            available_components=available_components
        )
        
        return schemas.BuildResponse(build_details=build_result)
        
    except ConnectionError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        print(f"Erro inesperado no endpoint /build-pc: {e}")
        raise HTTPException(status_code=500, detail="Ocorreu um erro inesperado no servidor.")


