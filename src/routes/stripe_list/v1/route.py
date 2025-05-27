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
        elif field.get("id") == "type" and object_type == "balance_transaction":
            fields.append({
                "id":f"{field.get('id')}",
                "label": f"{field.get('label')}",
                "type": "string",
                "ui_options": {
                    "ui_widget": "SelectWidget"
                },
                "choices": {
                    "values": [
                        {"value" : choice } for choice in ["None","adjustment", "advance", "advance_funding", "anticipation_repayment", "application_fee", "application_fee_refund", "charge", "climate_order_purchase", "climate_order_refund", "connect_collection_transfer", "contribution", "issuing_authorization_hold", "issuing_authorization_release", "issuing_dispute", "issuing_transaction", "obligation_outbound", "obligation_reversal_inbound", "payment", "payment_failure_refund", "payment_network_reserve_hold", "payment_network_reserve_release", "payment_refund", "payment_reversal", "payment_unreconciled", "payout", "payout_cancel", "payout_failure", "payout_minimum_balance_hold", "payout_minimum_balance_release", "refund", "refund_failure", "reserve_transaction", "reserved_funds", "stripe_fee", "stripe_fx_fee", "stripe_balance_payment_debit", "stripe_balance_payment_debit_reversal", "tax_fee", "topup", "topup_reversal", "transfer", "transfer_cancel", "transfer_failure", "transfer_refund"]
                    ]
                }

            })
        elif field.get("id") in ["shippable", "active"] and object_type == "product":
            fields.append({
                "id":f"{field.get('id')}",
                "label": f"{field.get('label')}",
                "type": "string",
                "ui_options": {
                    "ui_widget": "SelectWidget"
                },
                "choices": {
                    "values": [
                        {"value" : choice } for choice in ["None", "True", "False"]
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
    
    This endpoint handles all Stripe API list operations for different object types.
    It processes form data, makes appropriate API calls, and returns the response.
    
    Flow:
    1. Parse and validate incoming request data
    2. Extract and configure API credentials
    3. Route to appropriate Stripe API call based on object_type
    4. Handle special cases for each object type
    5. Return standardized response
    
    Special Handling:
    - balance_transaction: Handles type filter with None value removal
    - event: Transforms type array into Stripe API format
    - product: Handles IDs array and optional filters (status, shippable)
    - invoice: Removes None values from optional filters
    
    Returns:
        Response: Contains either:
            - Stripe API response data
            - Error message for invalid object type
    """
    # Parse and validate incoming request data
    request = Request(flask_request)
    data = request.data or {}

    # Extract and remove non-API parameters
    # These are used for routing but not sent to Stripe API
    object_type = data.get("object_type")
    api_key = data.get("api_key")
    del data["object_type"]
    del data["api_key"]

    # Configure Stripe API with provided credentials
    stripe.api_key = api_key

    # ============================================================================
    # OBJECT TYPE ROUTING
    # ============================================================================
    # Each object type has its own handling logic
    
    # Customer List
    if object_type == "customer":
        customers = stripe.Customer.list(**data)
        return Response(data=customers)
    
    # Charge List
    if object_type == "charge":
        charges = stripe.Charge.list(**data)
        return Response(data=charges)
    
    # Payment Intent List
    if object_type == "payment_intent":
        payment_intents = stripe.PaymentIntent.list(**data)
        return Response(data=payment_intents)
    
    # ============================================================================
    # BALANCE TRANSACTION HANDLING
    # ============================================================================
    # Special handling for balance transaction type filter
    if object_type == "balance_transaction":
        # Remove type filter if it's set to "None"
        # This prevents sending invalid filter to Stripe API
        if bool(data.get("type")):
            if data.get("type") == "None":
                del data["type"]
            # else: keep the type filter as is
        
        # Execute balance transaction list API call
        balance_transactions = stripe.BalanceTransaction.list(**data)
        return Response(data=balance_transactions)

    # ============================================================================
    # EVENT HANDLING
    # ============================================================================
    # Special handling for event type parameter
    # Transforms array of type objects into Stripe API format
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
    
    # ============================================================================
    # PRODUCT HANDLING
    # ============================================================================
    # Special handling for product parameters
    # 1. Transforms IDs array into Stripe API format
    # 2. Handles optional filters (status, shippable)
    if object_type == "product":
        # Handle IDs array transformation
        if bool(data.get("ids")):
            ids = data.get("ids")
            final_ids = []
            for id in ids:
                final_ids.append(id.get("ids"))
            del data["ids"]
            data["ids"] = final_ids
        
        # Handle optional filters
        # Remove filters if they're set to "None"
        if data.get("status", "") == "None":
            del data["status"]
        if data.get("shippable", "") == "None":
            del data["shippable"]

        products = stripe.Product.list(**data)
        return Response(data=products)
    
    # ============================================================================
    # INVOICE HANDLING
    # ============================================================================
    # Special handling for invoice parameters
    # Removes None values from optional filters to prevent invalid API calls
    if object_type == "invoice":
        # Remove None values from optional parameters
        if data.get("status") == "None":
            del data["status"]
        if data.get("collection_method") == "None":
            del data["collection_method"]
        invoices = stripe.Invoice.list(**data)
        return Response(data=invoices)

    # ============================================================================
    # ERROR HANDLING
    # ============================================================================
    # Return error message for invalid object type
    return Response(data="Please select an Object type")
   
