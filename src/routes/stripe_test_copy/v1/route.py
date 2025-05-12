from flask import request as flask_request
from workflows_cdk import Response, Request
from main import router
import stripe


@router.route("/content", methods=["POST"])
def content():
    request = Request(flask_request)
    data = request.data
    
    form_data = data.get("form_data")
    
    object_type = form_data.get("object_type")
    

    print("---------------------")

    print(str(object_type))
    print("---------------------")
    
    # Define options based on category
    if object_type == "Customer":
        options = [
        {"value": "name", "label":"Name"},
        {"value":"email", "label":"Email"}
        ]
    elif object_type == "Charge":
        options = [
            {"value":"customer_id", "label": "Customer_id"},
            {"value": "amount", "label": "Amount"},
            {"value": "currency", "label": "Currency"}
        ]
    # Return the options
    return Response(data={
        "content_objects": [{
            "content_object_name": "fields",
            "data": options
        }]
    })

@router.route("/execute", methods=["POST", "GET"])
def execute():
    request = Request(flask_request)
    data = request.data
    form_data = data.get("form_data",{})
    object_type = form_data.get("object_type")

    print("halahfla")

    
  
    return Response(data="ljasdf") 