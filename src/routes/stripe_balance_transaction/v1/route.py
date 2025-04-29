import json
from typing import Dict, Any, List

from flask import request as flask_request
from workflows_cdk import Response, Request, ManagedError
from main import router
from flask import stripe


@router.route("/content", methods=["POST"])



@router.route("/execute", methods=["GET", "POST"])
def execute():
    """
    Execute the operation using a single input field defined by the schema.
    """
    try:
        # Parse the request
        request = Request(flask_request)
        data = request.get_json()
        if not data:
            raise ManagedError("No data provided in the request")
        api_key = data.get("api_key")
        if not api_key:
            raise ManagedError("API key is required")
        
        stripe.api_key = api_key

        balance_transaction = stripe.BalanceTransaction.list()

        #let's ask a limit for the transactions to the user: 

        return Response(
            data=balance_transaction,
            metadata={"affected_rows": len(balance_transaction)},
            status_code=200,
        )
        
    except ManagedError as e:
        return Response.error(str(e))
    except Exception as e:
        return Response.error(str(e))