# ============================================================================
# IMPORTS
# ============================================================================
# Core Flask and request handling
from flask import request as flask_request
from workflows_cdk import Response, Request
from main import router

# Application specific imports
from dict import *  # TODO: Consider importing specific constants instead of *
import stripe

# ============================================================================
# CONSTANTS & CONFIGURATION
# ============================================================================
# Module identifier for route handling and logging
module = "list"

# ============================================================================
# SCHEMA DEFINITIONS
# ============================================================================
# Base schema for initial form state (no object type selected)
# Contains two essential fields:
# 1. api_key: For Stripe API authentication
# 2. object_type: Dynamic selector for available Stripe objects
base_schema = {
    "metadata": {},
    "fields": [
        # API Key field - Required for all Stripe API calls
        {
            "id": "api_key",
            "label": "api_key",
            "type": "string",
            "validation": {
                "required": True
            }
        },
        # Object Type selector - Dynamic field that triggers schema updates
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
                    {"value": obj_type} for obj_type in LIST_OBJECT_TYPE
                ]
            },
            "validation": {
                "required": True
            }
        }
    ]
}

# ============================================================================
# ROUTE HANDLERS
# ============================================================================

@router.route("/schema", methods=["POST"])
def schema():
    """
    Dynamic schema generation endpoint.
    
    This endpoint:
    1. Receives the current form state
    2. Determines the appropriate schema based on selected object type
    3. Returns a schema with relevant fields for the selected object type
    
    Returns:
        Response: Contains the generated schema for the form
    """
    # Parse and validate incoming request
    request = Request(flask_request)
    data = request.data or {}
    form_data = data.get("form_data", {})
    object_type = form_data.get("object_type")

    # Return base schema if no object type selected
    if not object_type:
        return Response(data={"schema": base_schema})

    # Find the selected object type configuration
    index = 0
    for obj in OBJECT_TYPE:
        if obj.get("object_type") == object_type:
            index = OBJECT_TYPE.index(obj)

    # Extract available actions for the selected object type
    object_type_actions = OBJECT_TYPE[index].get("action")

    # Initialize field lists
    required_fields = []
    optional_fields = []

    # Extract required and optional fields for the current module (list)
    for action in object_type_actions:
        for action_key, action_value in action.items():
            if action_key == module:
                required_fields = action_value.get("required_fields")
                optional_fields = action_value.get("optional_fields")

    # Build base fields (always present)
    fields = [
        # API Key field (required for all requests)
        {
            "id": "api_key",
            "label": "api_key",
            "type": "string",
            "validation": {
                "required": True
            }
        },
        # Object Type selector (required for all requests)
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
                    {"value": obj_type} for obj_type in LIST_OBJECT_TYPE
                ]
            },
            "validation": {
                "required": True
            }
        }
    ]

    # Add required fields to schema
    for field in required_fields:
        fields.append({
            "id": f"{field.get('id')}",
            "label": f"{field.get('label')}",
            "type": "string",
            "validation": {
                "required": True
            }
        })

    # Process optional fields with special handling for specific object types
    for field in optional_fields:
        # Special handling for event type field
        if field.get("id") == "type" and object_type == "event":
            fields.append({
                "id": f"{field.get('id')}",
                "label": f"{field.get('label')}",
                "type": "array",
                "items":{
                    "type":"object",
                    "fields":[
                        {
                            "id":"types",
                            "type":"string",
                            "label":"Type"
                        }
                    ]
                }
            })
        
        # Special handling for product IDs field
        elif field.get("id") == "ids" and object_type == "product":
            fields.append({
                "id": f"{field.get('id')}",
                "label": f"{field.get('label')}",
                "type": "array",
                "items":{
                    "type":"object",
                    "fields":[
                        {
                            "id":"ids",
                            "type":"string",
                            "label":"ID"
                        }
                    ]
                }
            })

        # Special handling for invoice fields (collection_method and status)
        elif field.get("id") in ["collection_method", "status"] and object_type == "invoice":
            invoice_fields_choice = {
                "collection_method": ["charge_automatically", "send_invoice", "None"],
                "status": ["draft", "open", "paid", "uncollectible", "void", "None"]
            }
            if field.get("id") in invoice_fields_choice:
                fields.append({
                    "id": f"{field.get('id')}",
                    "label": f"{field.get('label')}",
                    "type": "string",
                    "ui_options": {
                        "ui_widget": "SelectWidget"
                    },
                    "choices": {
                        "values": [
                            {"value": choice} for choice in invoice_fields_choice[field.get("id")]
                        ]
                    }
                })

        # Default field handling
        else:                    
            fields.append({
                "id": f"{field.get('id')}",
                "label": f"{field.get('label')}",
                "type": "string"
            })

    # Construct and return final schema
    new_schema = {
        "metadata": {},
        "fields": fields
    }

    return Response(data={"schema": new_schema})

@router.route("/execute", methods=["POST", "GET"])
def execute():
    """
    Execute Stripe API calls based on form submission.
    
    This endpoint:
    1. Processes the form submission
    2. Makes appropriate Stripe API calls
    3. Returns the API response
    
    Returns:
        Response: Contains the Stripe API response or error message
    """
    # Parse and validate request
    request = Request(flask_request)
    data = request.data or {}

    # Extract and remove non-API parameters
    object_type = data.get("object_type")
    api_key = data.get("api_key")
    del data["object_type"]
    del data["api_key"]

    # Configure Stripe API
    stripe.api_key = api_key

    # Route to appropriate Stripe API call based on object type
    if object_type == "customer":
        customers = stripe.Customer.list(**data)
        return Response(data=customers)
    
    if object_type == "charge":
        charges = stripe.Charge.list(**data)
        return Response(data=charges)
    
    if object_type == "payment_intent":
        payment_intents = stripe.PaymentIntent.list(**data)
        return Response(data=payment_intents)
    
    if object_type == "balance_transaction":
        balance_transactions = stripe.BalanceTransaction.list(**data)
        return Response(data=balance_transactions)

    # Special handling for event type parameter
    if object_type == "event":
        if bool(data.get("type")):
            types = data.get("type")
            final_types = []
            for typee in types:
                final_types.append(typee.get("types"))
            del data["type"]
            data["types"] = final_types
        events = stripe.Event.list(**data)
        return Response(data=events)
    
    # Special handling for product IDs parameter
    if object_type == "product":
        if bool(data.get("ids")):
            ids = data.get("ids")
            final_ids = []
            for id in ids:
                final_ids.append(id.get("ids"))
            del data["ids"]
            data["ids"] = final_ids
        products = stripe.Product.list(**data)
        return Response(data=products)
    
    # Special handling for invoice parameters
    if object_type == "invoice":
        # Remove None values from optional parameters
        if data.get("status") == "None":
            del data["status"]
        if data.get("collection_method") == "None":
            del data["collection_method"]
        invoices = stripe.Invoice.list(**data)
        return Response(data=invoices)

    # Handle invalid object type
    return Response(data="Please select an Object type")
   
