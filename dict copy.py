OBJECT_TYPE = [
    {
        "object_type": "customer",
        "action": [
            {
                "create": {
                    "required_fields": [
                        # No required fields for basic customer creation
                    ],
                    "optional_fields": [
                        # Basic Information
                        "name",
                        "email",
                        "phone",
                        "description",
                        
                        # Address Information
                        "address",  # This is an object with:
                        "address.line1",
                        "address.line2",
                        "address.city",
                        "address.state",
                        "address.postal_code",
                        "address.country",
                        
                        # Invoice Settings
                        "invoice_settings",
                        "invoice_settings.custom_fields",
                        "invoice_settings.default_payment_method",
                        "invoice_settings.footer",
                        "invoice_settings.rendering_options",
                        
                        # Additional Information
                        "metadata",
                        "currency",
                        "balance",
                        
                        # Shipping Information
                        "shipping",
                        "shipping.name",
                        "shipping.phone",
                        "shipping.address",
                        
                        # Tax Information
                        "tax_exempt",
                        
                        # Localization
                        "preferred_locales"
                    ]
                }
            },
            {
                "update": {
                    "required_fields": [
                        "id"  # Customer ID is required for update
                    ],
                    "optional_fields": [
                        # Basic Information
                        "name",
                        "email",
                        "phone",
                        "description",
                        
                        # Address Information (Required if calculating taxes)
                        "address",  # Dictionary with:
                        "address.line1",
                        "address.line2",
                        "address.city",
                        "address.state",
                        "address.postal_code",
                        "address.country",
                        
                        # Invoice Settings
                        "invoice_settings",  # Dictionary with:
                        "invoice_settings.custom_fields",
                        "invoice_settings.default_payment_method",
                        "invoice_settings.footer",
                        "invoice_settings.rendering_options",
                        "invoice_prefix",  # 3-12 uppercase letters/numbers
                        
                        # Payment Information
                        "default_source",  # ID of existing payment source
                        "source",  # New payment source token
                        
                        # Balance Information
                        "balance",  # Integer in cents
                        "cash_balance",  # Dictionary with balance settings
                        
                        # Additional Information
                        "metadata",  # Dictionary of key-value pairs
                        "next_invoice_sequence",  # Integer, defaults to 1
                        
                        # Shipping Information
                        "shipping",  # Dictionary with:
                        "shipping.name",
                        "shipping.phone",
                        "shipping.address",
                        
                        # Tax Information
                        "tax",  # Dictionary with tax details
                        "tax_exempt",  # Enum: "none", "exempt", "reverse"
                        
                        # Localization
                        "preferred_locales"  # Array of strings
                    ],
                    "field_descriptions": {
                        "address": "Required if calculating taxes",
                        "description": "An arbitrary string displayed alongside the customer in the dashboard",
                        "email": "Customer's email address (up to 512 characters)",
                        "metadata": "Set of key-value pairs for additional information",
                        "name": "Customer's full name or business name",
                        "phone": "Customer's phone number",
                        "shipping": "Customer's shipping information for invoices",
                        "tax": "Recommended if calculating taxes",
                        "balance": "Integer amount in cents affecting future invoices",
                        "default_source": "ID of payment source to make default",
                        "source": "New payment source token",
                        "invoice_prefix": "3-12 uppercase letters or numbers",
                        "tax_exempt": "One of: none, exempt, reverse"
                    }
                }
            },
            {
                "retrieve":{
                    "required_fields":["customer"],
                    "optional_fields":[]
                }
            },
            {
                "list":{
                    "required_fields": ["limit"],
                    "optional_fields":[]
                }
            }
        ]
    },
    {
        "object_type": "charge",
        "action": [
            {
                "create": {
                    "required_fields": [
                        "amount",
                        "currency",
                        {
                            "name": "payment_source",
                            "type": "either",
                            "fields": ["source", "customer"],
                            "description": "Either source or customer must be provided"
                        }
                    ],
                    "optional_fields": [
                        # Basic Information
                        "description",
                        "metadata",
                        "receipt_email",
                        "receipt_number",
                        "statement_descriptor",
                        "statement_descriptor_suffix",
                        
                        # Billing Details
                        "billing_details",
                        "billing_details.address",
                        "billing_details.address.city",
                        "billing_details.address.country",
                        "billing_details.address.line1",
                        "billing_details.address.line2",
                        "billing_details.address.postal_code",
                        "billing_details.address.state",
                        "billing_details.email",
                        "billing_details.name",
                        "billing_details.phone",
                        
                        # Shipping Information
                        "shipping",
                        "shipping.address",
                        "shipping.name",
                        "shipping.phone",
                        
                        # Payment Information
                        "capture",
                        "application_fee_amount",
                        "on_behalf_of",
                        "transfer_data",
                        "transfer_group",
                        
                        # Additional Settings
                        "fraud_details",
                        "receipt_url",
                        "review",
                        "source_transfer",
                        "transfer",
                        "transfer_data",
                        "transfer_group"
                    ]
                }
            }
        ]
    }
]

CREATE_OBJECT_TYPE = []
UPDATE_OBJECT_TYPE = []
RETRIEVE_OBJECT_TYPE = []
LIST_OBJECT_TYPE = []
CUSTOME_OBJECT_TYPE = []



for obj in OBJECT_TYPE:
    object_type = obj.get("object_type")
    actions = obj.get("action")
    for action in actions:
        for key, fields in action.items():
            if key == "create":
                CREATE_OBJECT_TYPE.append(object_type)
            elif key == "update":
                UPDATE_OBJECT_TYPE.append(object_type)
            elif key == "retrieve":
                RETRIEVE_OBJECT_TYPE.append(object_type)
            elif key == "list":
                LIST_OBJECT_TYPE.append(object_type)
            else:
                CUSTOME_OBJECT_TYPE.append(object_type)

print(CREATE_OBJECT_TYPE)
print(UPDATE_OBJECT_TYPE)
print(RETRIEVE_OBJECT_TYPE)
print(LIST_OBJECT_TYPE)
print(CUSTOME_OBJECT_TYPE)




