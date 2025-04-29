from workflows_cdk import Response, Request
from flask import request as flask_request
from flask import stripe 
from main import router



@router.route("/execute", methods=["GET"])
def execute():
    try:
        request = Request(flask_request)
        data = request.get_json()
        api_key = data.get("api_key")

        stripe.api_key = api_key
        balance = stripe.Balance.retrieve() 
        
    except Exception as e:
        return Response(data={"error": str(e)}, status_code=500)
    



    # Your logic here
    # Here you can add your logic to execute the action which may consist of, for example:
    # - calling an API
    # - doing some calculations
    # - doing some data transformations
    # - validating data
    

    output = [balance]

    return Response(data=output, metadata={"affected_rows": len(output)}, status_code=200
                    )



