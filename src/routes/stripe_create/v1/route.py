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

    options = []
    
    
    # Define options based on category
    if object_type == "Customer":
        options = [
        {"value": "name", "label":"Name"},
        {"value":"email", "label":"Email"},
        {"value":"description", "label":"Description"},

        ]
    elif object_type == "Charge":
        options = [
            {"value":"customer", "label": "Customer_id"},
            {"value": "amount", "label": "Amount"},
            {"value": "currency", "label": "Currency"},
            {"value": "source", "label": "Source"},
            {"value": "description", "label": "Description"}
            

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
    
    object_type = data.get("object_type")
    print("---------")
    print(object_type)
    print("---------")

    fields = data.get("fields")

    print("---------------")
    print(fields)
    print("---------------")


    api_key = data.get("api_key")

    print("---------------")
    print(api_key)
    print("---------------")

    stripe.api_key = api_key
    
    

    field_value = {}

    for field in fields:
        name = field.get("field_name")
        value = field.get("field_value")
        field_value[name]= value

    if object_type == "Customer":
    
        customer = stripe.Customer.create(**field_value)
        return Response(data=customer)


    if object_type == "Charge":
        charge = stripe.Charge.create(**field_value)
        return Response(data=charge)





    




    
  
    return Response(data="") 