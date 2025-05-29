# ============================================================================
# IMPORTS
# ============================================================================
# Core Flask and request handling
from dict import EVENT_TYPES_LIST
from flask import request as flask_request
from workflows_cdk import Response, Request
from main import router
from datetime import datetime

# Application specific imports
from dict import *
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
            },
            

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
                ui_options = action_value.get("ui_options")
    print(ui_options)

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
            },
            "description": f"{field.get('description')}"

        })

    # Process optional fields with special handling for specific object types
    for field in optional_fields:
        # Special handling for event type field
        if field.get("id").startswith("created"):
            fields.append({
            "id": f"{field.get('id')}",
            "label": f"{field.get('label')}",
            "type": "string",
            "validation": {
                "pattern":  "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"
            },
            "description": f"{field.get('description')}",
            "ui_options":{
                "ui_widget": "DateTimeWidget",
                "format": "YYYY-MM-DDTHH:mm:ss.SSSZ"
            },
            



        })


        elif field.get("id") == "type" and object_type == "event":
            fields.append({
                "id": f"{field.get('id')}",
                "label": f"{field.get('label')}",
                "type": "array",
                "items":{
                    "type":"object",
                    "fields":[
                        {
                            "id":"Object_type",
                            "type":"string",
                            "label":"Type",
                            "ui_options": {
                                "ui_widget": "SelectWidget"
                            },
                            "choices": {
                                "values": [
                                                {"value":choice } for choice in EVENT_TYPES_LIST
                                    ]
                            }
                        }
                       
                    ]
                },
                "description": f"{field.get('description')}"
            })
        elif field.get("id") == "delivery_success" and object_type == "event":
            fields.append({
                "id":f"{field.get('id')}",
                "label": f"{field.get('label')}",
                "type": "string",
                "ui_options": {
                    "ui_widget": "SelectWidget"
                },
                "choices": {
                    "values": [
                        {"value" : choice} for choice in ["Default", "True", "False"]
                    ]
                },
                "description": f"{field.get('description')}"

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
                },
                "description": f"{field.get('description')}"
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
                    },
                    "description": f"{field.get('description')}"
                })
        elif field.get("id") == "type" and object_type == "balance_transaction":
            doc = {"Default": "Default", "adjustment": "Adjustment", "advance": "Advance", "advance_funding": "Advance Funding", "anticipation_repayment": "Anticipation Repayment", "application_fee": "Application Fee", "application_fee_refund": "Application Fee Refund", "charge": "Charge", "climate_order_purchase": "Climate Order Purchase", "climate_order_refund": "Climate Order Refund", "connect_collection_transfer": "Connect Collection Transfer", "contribution": "Contribution", "issuing_authorization_hold": "Issuing Authorization Hold", "issuing_authorization_release": "Issuing Authorization Release", "issuing_dispute": "Issuing Dispute", "issuing_transaction": "Issuing Transaction", "obligation_outbound": "Obligation Outbound", "obligation_reversal_inbound": "Obligation Reversal Inbound", "payment": "Payment", "payment_failure_refund": "Payment Failure Refund", "payment_network_reserve_hold": "Payment Network Reserve Hold", "payment_network_reserve_release": "Payment Network Reserve Release", "payment_refund": "Payment Refund", "payment_reversal": "Payment Reversal", "payment_unreconciled": "Payment Unreconciled", "payout": "Payout", "payout_cancel": "Payout Cancel", "payout_failure": "Payout Failure", "payout_minimum_balance_hold": "Payout Minimum Balance Hold", "payout_minimum_balance_release": "Payout Minimum Balance Release", "refund": "Refund", "refund_failure": "Refund Failure", "reserve_transaction": "Reserve Transaction", "reserved_funds": "Reserved Funds", "stripe_fee": "Stripe Fee", "stripe_fx_fee": "Stripe FX Fee", "stripe_balance_payment_debit": "Stripe Balance Payment Debit", "stripe_balance_payment_debit_reversal": "Stripe Balance Payment Debit Reversal", "tax_fee": "Tax Fee", "topup": "Top Up", "topup_reversal": "Top Up Reversal", "transfer": "Transfer", "transfer_cancel": "Transfer Cancel", "transfer_failure": "Transfer Failure", "transfer_refund": "Transfer Refund"}
            fields.append({
                "id": f"{field.get('id')}",
                "label": f"{field.get('label')}",
                "type": "string",
                "ui_options": {
                    "ui_widget": "SelectWidget"
                },
                "choices": {
                    "values": [
                        {"value": choice, "label ": label} for choice, label in doc.items()
                    ]
                },
                "description": f"{field.get('description')}"
            })
        elif field.get("id") == "currency" and object_type == "balance_transaction":
            fields.append({
                "id":f"{field.get('id')}",
                "label": f"{field.get('label')}",
                "type": "string",
                "ui_options": {
                    "ui_widget": "SelectWidget"
                },
                "choices": {
                    "values": [
                        {"value" : choice } for choice in [ "Default",
                            "usd", "aed", "afn", "all", "amd", "ang", "aoa", "ars", "aud", "awg", "azn", 
                            "bam", "bbd", "bdt", "bgn", "bif", "bmd", "bnd", "bob", "brl", "bsd", "bwp", 
                            "byn", "bzd", "cad", "cdf", "chf", "clp", "cny", "cop", "crc", "cve", "czk", 
                            "djf", "dkk", "dop", "dzd", "egp", "etb", "eur", "fjd", "fkp", "gbp", "gel", 
                            "gip", "gmd", "gnf", "gtq", "gyd", "hkd", "hnl", "htg", "huf", "idr", "ils", 
                            "inr", "isk", "jmd", "jpy", "kes", "kgs", "khr", "kmf", "krw", "kyd", "kzt", 
                            "lak", "lbp", "lkr", "lrd", "lsl", "mad", "mdl", "mga", "mkd", "mmk", "mnt", 
                            "mop", "mur", "mvr", "mwk", "mxn", "myr", "mzn", "nad", "ngn", "nio", "nok", 
                            "npr", "nzd", "pab", "pen", "pgk", "php", "pkr", "pln", "pyg", "qar", "ron", 
                            "rsd", "rub", "rwf", "sar", "sbd", "scr", "sek", "sgd", "shp", "sle", "sos", 
                            "srd", "std", "szl", "thb", "tjs", "top", "try", "ttd", "twd", "tzs", "uah", 
                            "ugx", "uyu", "uzs", "vnd", "vuv", "wst", "xaf", "xcd", "xcg", "xof", "xpf", 
                            "yer", "zar", "zmw"
                        ]
                    ]
                },
                "description": f"{field.get('description')}"

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
                        {"value" : choice } for choice in ["Default", "True", "False"]
                    ]
                },
                "description": f"{field.get('description')}"

            })
        
        # Default field handling
        else:                    
            fields.append({
                "id": f"{field.get('id')}",
                "label": f"{field.get('label')}",
                "type": "string",
                "description": f"{field.get('description')}"
            })

    # Construct and return final schema
    new_schema = {
        "metadata": {},
        "fields": fields,
         "ui_options" : {
             "ui_order": [
                 "created[gt]",
                 "created[gte]",
                 "created[lt]",
                 "created[lte]",
                 "delivery_success",
                 "starting_after",
                 "ending_before",
                 "limit"
             ]
         }
    }

    # print(new_schema)

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

    # convert the date into UNIX Time stamp if needed:
    for field in data:
        if field.startswith("created"):
            date = data.get(field)
            dt = datetime.fromisoformat(date.replace("Z","+00:00"))
            unix_timestamp = int(dt.timestamp())
            data[field] = unix_timestamp
    
    # ===================================================================
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
            if data.get("type") == "Default":
                del data["type"]
        if bool(data.get("currency")):
            if data.get("currency") == "Default":
                del data["currency"]
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

        if bool(data.get("delivery_success")):
            delivery_sucess = data.get("delivery_success")
            if delivery_sucess == "Default":
                del data["delivery_success"]
        
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
        if data.get("status", "") == "Default":
            del data["status"]
        if data.get("shippable", "") == "Default":
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
        if data.get("status") == "Default":
            del data["status"]
        if data.get("collection_method") == "Default":
            del data["collection_method"]
        invoices = stripe.Invoice.list(**data)
        return Response(data=invoices)

    # ============================================================================
    # ERROR HANDLING
    # ============================================================================
    # Return error message for invalid object type
    return Response(data="Please select an Object type")
   
