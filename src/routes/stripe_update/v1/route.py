# Import necessary libraries
# Flask for handling HTTP requests
# Response and Request from workflows_cdk for standardized request/response handling
# Router from main for route management
# All constants from dict.py (OBJECT_TYPE, GET_OBJECT_TYPE, etc.)
# Stripe SDK for interacting with Stripe API
from flask import request as flask_request
from workflows_cdk import Response, Request
from main import router
from dict import *
import stripe

# Module identifier for this route handler
module = "update"

# Base schema definition for the initial form
# This schema is used when no object type is selected
# It contains two fields:
# 1. api_key - Required string field for Stripe API authentication
# 2. object_type - Required select field that dynamically loads available object types
base_schema = {
    "metadata": {},
    "fields": [
        # API Key field definition
        {
            "id": "api_key",
            "label": "api_key",
            "type": "string",
            "validation": {
                "required": True
            }
        },
        # Object Type selector field definition
        {
            "type": "string",
            "label": "Select object type",
            "id": "object_type",
            "ui_options": {
                "uiwidget": "SelectWidget"
            },
            "on_action": {
                "load_schema": True
            },
            "choices": {
                "values": [
                    {"value": obj_type} for obj_type in UPDATE_OBJECT_TYPE
                ]
            },
            "validation": {
                "required": True
            }
        }
    ]
}

# Route handler for schema generation
# This endpoint is called when the form needs to be dynamically updated
# It returns different schemas based on the selected object type
@router.route("/schema", methods=["POST"])
def schema():
    # Parse the incoming request
    request = Request(flask_request)
    data = request.data or {}
    form_data = data.get("form_data", {})
    object_type = form_data.get("object_type")

    # If no object type is selected, return the base schema
    if not object_type:
        return Response(data={"schema": base_schema})

    # Debug logging
    print("Data:", data)
    print(object_type, "--------------------------")

    # Find the index of the selected object type in OBJECT_TYPE list
    index = 0
    for obj in OBJECT_TYPE:
        if obj.get("object_type") == object_type:
            index = OBJECT_TYPE.index(obj)

    # Get the actions available for the selected object type
    object_type_actions = OBJECT_TYPE[index].get("action")

    # Initialize lists for required and optional fields
    required_fields = []
    optional_fields = []

    # Extract required and optional fields for the 'get' action
    for action in object_type_actions:
        for action_key, action_value in action.items():
            if action_key == module:
                required_fields = action_value.get("required_fields")
                optional_fields = action_value.get("optional_fields")

    # Start building the dynamic schema with base fields
    fields = [
        # API Key field (always required)
        {
            "id": "api_key",
            "label": "api_key",
            "type": "string",
            "validation": {
                "required": True
            }
        },
        # Object Type selector (always required)
        {
            "type": "string",
            "label": "Select object type",
            "id": "object_type",
            "ui_options": {
                "uiwidget": "SelectWidget"
            },
            "on_action": {
                "load_schema": True
            },
            "choices": {
                "values": [
                    {"value": obj_type} for obj_type in UPDATE_OBJECT_TYPE
                ]
            },
            "validation": {
                "required": True
            }
        }
    ]

    # Add required fields to the schema
    for field in required_fields:
        fields.append({
            "id": f"{field.get('id')}",
            "label": f"{field.get('label')}",
            "type": "string",
            "validation": {
                "required": True
            }
        })

    # Add optional fields to the schema
    for field in optional_fields:
        fields.append({
            "id": f"{field.get('id')}",
            "label": f"{field.get('label')}",
            "type": "string"
        })

    # Construct the final schema
    new_schema = {
        "metadata": {},
        "fields": fields
    }

    return Response(data={"schema": new_schema})

# Route handler for executing Stripe API calls
# This endpoint processes the form submission and makes the actual API calls
@router.route("/execute", methods=["POST", "GET"])
def execute():
    # Parse the incoming request
    request = Request(flask_request)
    data = request.data or {}

    # Extract object type and API key from the request
    object_type = data.get("object_type")
    api_key = data.get("api_key")

    # Remove object_type and api_key from data as they're not part of the API call
    del data["object_type"]
    del data["api_key"]

    # Set the Stripe API key
    stripe.api_key = api_key

    # Handle different object types
    # Each object type has its own specific retrieval logic
    if object_type == "customer":
        customer = stripe.Customer.modify(**data)
        return Response(data=customer)
    
    if object_type == "charge":
        charge = stripe.Charge.modify(**data)
        return Response(data=charge)
    
    if object_type == "payment_intent":
        payment_intent = stripe.PaymentIntent.modify(**data)
        return Response(data=payment_intent)
    
    
    
    
        
        
    else:
        # Handle invalid object type
        return Response(data="Please select an Object type")
   
