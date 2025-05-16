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
                        {"value": "name", "label": "Full Name or Business Name"},
                        {"value": "email", "label": "Email Address"},
                        {"value": "phone", "label": "Phone Number"},
                        {"value": "description", "label": "Description"},
                        {"value": "metadata", "label": "Metadata"},
                        
                        # Address Information
                        {"value": "address", "label": "Address"},
                        {"value": "address.line1", "label": "Address Line 1"},
                        {"value": "address.line2", "label": "Address Line 2"},
                        {"value": "address.city", "label": "City"},
                        {"value": "address.state", "label": "State"},
                        {"value": "address.postal_code", "label": "Postal Code"},
                        {"value": "address.country", "label": "Country"},
                        
                        # Payment Information
                        {"value": "payment_method", "label": "Payment Method"},
                        {"value": "source", "label": "Source"},
                        
                        # Balance Information
                        {"value": "balance", "label": "Balance"},
                        {"value": "cash_balance", "label": "Cash Balance"},
                        
                        # Invoice Settings
                        {"value": "invoice_prefix", "label": "Invoice Prefix"},
                        {"value": "invoice_settings", "label": "Invoice Settings"},
                        {"value": "invoice_settings.custom_fields", "label": "Custom Fields"},
                        {"value": "invoice_settings.default_payment_method", "label": "Default Payment Method"},
                        {"value": "invoice_settings.footer", "label": "Invoice Footer"},
                        {"value": "invoice_settings.rendering_options", "label": "Rendering Options"},
                        {"value": "next_invoice_sequence", "label": "Next Invoice Sequence"},
                        
                        # Shipping Information
                        {"value": "shipping", "label": "Shipping Information"},
                        {"value": "shipping.name", "label": "Shipping Name"},
                        {"value": "shipping.phone", "label": "Shipping Phone"},
                        {"value": "shipping.address", "label": "Shipping Address"},
                        {"value": "shipping.address.line1", "label": "Shipping Address Line 1"},
                        {"value": "shipping.address.line2", "label": "Shipping Address Line 2"},
                        {"value": "shipping.address.city", "label": "Shipping City"},
                        {"value": "shipping.address.state", "label": "Shipping State"},
                        {"value": "shipping.address.postal_code", "label": "Shipping Postal Code"},
                        {"value": "shipping.address.country", "label": "Shipping Country"},
                        
                        # Tax Information
                        {"value": "tax", "label": "Tax Information"},
                        {"value": "tax.ip_address", "label": "Tax IP Address"},
                        {"value": "tax.validate_location", "label": "Tax Location Validation"},
                        {"value": "tax_exempt", "label": "Tax Exempt Status"},
                        {"value": "tax_id_data", "label": "Tax IDs"},
                        {"value": "tax_id_data.type", "label": "Tax ID Type"},
                        {"value": "tax_id_data.value", "label": "Tax ID Value"},
                        
                        # Additional Information
                        {"value": "preferred_locales", "label": "Preferred Languages"},
                        {"value": "test_clock", "label": "Test Clock"}
                    ]
                }
            },
            {
                "update": {
                    "required_fields": [
                        {"value": "id", "label": "Customer ID"}
                    ],
                    "optional_fields": [
                        # Basic Information
                        {"value": "name", "label": "Full Name or Business Name"},
                        {"value": "email", "label": "Email Address"},
                        {"value": "phone", "label": "Phone Number"},
                        {"value": "description", "label": "Description"},
                        {"value": "metadata", "label": "Metadata"},
                        
                        # Address Information
                        {"value": "address", "label": "Address"},
                        {"value": "address.line1", "label": "Address Line 1"},
                        {"value": "address.line2", "label": "Address Line 2"},
                        {"value": "address.city", "label": "City"},
                        {"value": "address.state", "label": "State"},
                        {"value": "address.postal_code", "label": "Postal Code"},
                        {"value": "address.country", "label": "Country"},
                        
                        # Payment Information
                        {"value": "default_source", "label": "Default Payment Source"},
                        {"value": "source", "label": "Payment Source"},
                        
                        # Balance Information
                        {"value": "balance", "label": "Balance"},
                        {"value": "cash_balance", "label": "Cash Balance"},
                        
                        # Invoice Settings
                        {"value": "invoice_prefix", "label": "Invoice Prefix"},
                        {"value": "invoice_settings", "label": "Invoice Settings"},
                        {"value": "invoice_settings.custom_fields", "label": "Custom Fields"},
                        {"value": "invoice_settings.default_payment_method", "label": "Default Payment Method"},
                        {"value": "invoice_settings.footer", "label": "Invoice Footer"},
                        {"value": "invoice_settings.rendering_options", "label": "Rendering Options"},
                        {"value": "next_invoice_sequence", "label": "Next Invoice Sequence"},
                        
                        # Shipping Information
                        {"value": "shipping", "label": "Shipping Information"},
                        {"value": "shipping.name", "label": "Shipping Name"},
                        {"value": "shipping.phone", "label": "Shipping Phone"},
                        {"value": "shipping.address", "label": "Shipping Address"},
                        {"value": "shipping.address.line1", "label": "Shipping Address Line 1"},
                        {"value": "shipping.address.line2", "label": "Shipping Address Line 2"},
                        {"value": "shipping.address.city", "label": "Shipping City"},
                        {"value": "shipping.address.state", "label": "Shipping State"},
                        {"value": "shipping.address.postal_code", "label": "Shipping Postal Code"},
                        {"value": "shipping.address.country", "label": "Shipping Country"},
                        
                        # Tax Information
                        {"value": "tax", "label": "Tax Information"},
                        {"value": "tax_exempt", "label": "Tax Exempt Status"},
                        
                        # Additional Information
                        {"value": "preferred_locales", "label": "Preferred Languages"}
                    ]
                }
            },
            {
                "retrieve": {
                    "required_fields": [
                        {"value": "customer", "label": "Customer ID"}
                    ],
                    "optional_fields": []
                }
            },
            {
                "list": {
                    "required_fields": [
                        {"value": "limit", "label": "Limit"}
                    ],
                    "optional_fields": [
                        # Pagination
                        {"value": "starting_after", "label": "Starting After"},
                        {"value": "ending_before", "label": "Ending Before"},
                        
                        # Date Filters
                        {"value": "created.gt", "label": "Created After"},
                        {"value": "created.gte", "label": "Created On or After"},
                        {"value": "created.lt", "label": "Created Before"},
                        {"value": "created.lte", "label": "Created On or Before"},
                        
                        # Other Filters
                        {"value": "email", "label": "Email Filter"},
                        {"value": "test_clock", "label": "Test Clock"}
                    ]
                }
            },
            {
                "delete": {
                    "required_fields": [
                        {"value": "id", "label": "Customer ID"}
                    ],
                    "optional_fields": []
                }
            },
            {
                "search": {
                    "required_fields": [
                        {"value": "query", "label": "Search Query"},
                        {"value": "limit", "label": "Result Limit"}
                    ],
                    "optional_fields": [
                        {"value": "page", "label": "Page Number"}
                    ]
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
                        {"value": "amount", "label": "Amount"},
                        {"value": "currency", "label": "Currency"}
                    ],
                    "optional_fields": [
                        # Basic Information
                        {"value": "customer", "label": "Customer ID"},
                        {"value": "description", "label": "Description"},
                        {"value": "metadata", "label": "Metadata"},
                        {"value": "receipt_email", "label": "Receipt Email"},
                        
                        # Payment Source
                        {"value": "source", "label": "Payment Source"},
                        
                        # Statement Information
                        {"value": "statement_descriptor", "label": "Statement Descriptor"},
                        {"value": "statement_descriptor_suffix", "label": "Statement Descriptor Suffix"},
                        
                        # Shipping Information
                        {"value": "shipping", "label": "Shipping Information"},
                        {"value": "shipping.name", "label": "Recipient Name"},
                        {"value": "shipping.phone", "label": "Recipient Phone"},
                        {"value": "shipping.carrier", "label": "Shipping Carrier"},
                        {"value": "shipping.tracking_number", "label": "Tracking Number"},
                        {"value": "shipping.address", "label": "Shipping Address"},
                        {"value": "shipping.address.line1", "label": "Shipping Address Line 1"},
                        {"value": "shipping.address.line2", "label": "Shipping Address Line 2"},
                        {"value": "shipping.address.city", "label": "Shipping City"},
                        {"value": "shipping.address.state", "label": "Shipping State"},
                        {"value": "shipping.address.postal_code", "label": "Shipping Postal Code"},
                        {"value": "shipping.address.country", "label": "Shipping Country"},
                        
                        # Payment Settings
                        {"value": "capture", "label": "Capture"},
                        {"value": "application_fee_amount", "label": "Application Fee Amount"},
                        {"value": "on_behalf_of", "label": "On Behalf Of"},
                        
                        # Connect Specific
                        {"value": "transfer_data", "label": "Transfer Data"},
                        {"value": "transfer_group", "label": "Transfer Group"},
                        
                        # Radar Options
                        {"value": "radar_options", "label": "Radar Options"}
                    ]
                }
            },
            {
                "update": {
                    "required_fields": [
                        {"value": "id", "label": "Charge ID"}
                    ],
                    "optional_fields": [
                        # Basic Information
                        {"value": "customer", "label": "Customer ID"},
                        {"value": "description", "label": "Description"},
                        {"value": "metadata", "label": "Metadata"},
                        {"value": "receipt_email", "label": "Receipt Email"},
                        
                        # Shipping Information
                        {"value": "shipping", "label": "Shipping Information"},
                        {"value": "shipping.name", "label": "Recipient Name"},
                        {"value": "shipping.phone", "label": "Recipient Phone"},
                        {"value": "shipping.carrier", "label": "Shipping Carrier"},
                        {"value": "shipping.tracking_number", "label": "Tracking Number"},
                        {"value": "shipping.address", "label": "Shipping Address"},
                        {"value": "shipping.address.line1", "label": "Shipping Address Line 1"},
                        {"value": "shipping.address.line2", "label": "Shipping Address Line 2"},
                        {"value": "shipping.address.city", "label": "Shipping City"},
                        {"value": "shipping.address.state", "label": "Shipping State"},
                        {"value": "shipping.address.postal_code", "label": "Shipping Postal Code"},
                        {"value": "shipping.address.country", "label": "Shipping Country"},
                        
                        # Fraud Details
                        {"value": "fraud_details", "label": "Fraud Details"},
                        
                        # Connect Specific
                        {"value": "transfer_group", "label": "Transfer Group"}
                    ]
                }
            },
            {
                "retrieve": {
                    "required_fields": [
                        {"value": "charge", "label": "Charge ID"}
                    ],
                    "optional_fields": []
                }
            },
            {
                "list": {
                    "required_fields": [
                        {"value": "limit", "label": "Limit"}
                    ],
                    "optional_fields": [
                        # Pagination
                        {"value": "starting_after", "label": "Starting After"},
                        {"value": "ending_before", "label": "Ending Before"},
                        
                        # Date Filters
                        {"value": "created.gt", "label": "Created After"},
                        {"value": "created.gte", "label": "Created On or After"},
                        {"value": "created.lt", "label": "Created Before"},
                        {"value": "created.lte", "label": "Created On or Before"},
                        
                        # Other Filters
                        {"value": "email", "label": "Email Filter"},
                        {"value": "test_clock", "label": "Test Clock"}
                    ]
                }
            },
            {
                "delete": {
                    "required_fields": [
                        {"value": "id", "label": "Charge ID"}
                    ],
                    "optional_fields": []
                }
            },
            {
                "search": {
                    "required_fields": [
                        {"value": "query", "label": "Search Query"},
                        {"value": "limit", "label": "Result Limit"}
                    ],
                    "optional_fields": [
                        {"value": "page", "label": "Page Number"}
                    ]
                }
            }
        ]
    },
    {
        "object_type": "payment_intent",
        "action": [
            {
                "create": {
                    "required_fields": [
                        {"value": "amount", "label": "Amount in cents/smallest currency unit"},
                        {"value": "currency", "label": "Three-letter ISO currency code"}
                    ],
                    "optional_fields": [
                        # Basic Information
                        {"value": "description", "label": "Description of the payment"},
                        {"value": "metadata", "label": "Additional metadata"},
                        {"value": "receipt_email", "label": "Email for receipt"},
                        {"value": "statement_descriptor", "label": "Statement descriptor (max 22 chars)"},
                        {"value": "statement_descriptor_suffix", "label": "Statement descriptor suffix"},
                        
                        # Payment Method Configuration
                        {"value": "payment_method_types", "label": "List of payment method types to accept"},
                        {"value": "payment_method", "label": "Specific payment method to use"},
                        {"value": "payment_method_data", "label": "Payment method data for new payment methods"},
                        {"value": "payment_method_options", "label": "Payment method specific options"},
                        {"value": "payment_method_options.card", "label": "Card payment method options"},
                        {"value": "payment_method_options.card.installments", "label": "Card installments configuration"},
                        {"value": "payment_method_options.card.mandate_options", "label": "Card mandate options"},
                        {"value": "payment_method_options.card.network", "label": "Specific card network"},
                        {"value": "payment_method_options.card.request_three_d_secure", "label": "3D Secure request type"},
                        {"value": "payment_method_options.card.setup_future_usage", "label": "Setup future usage for card"},
                        {"value": "payment_method_options.card.capture_method", "label": "Capture method for card"},
                        {"value": "payment_method_options.card.verification_method", "label": "Verification method for card"},
                        
                        # Automatic Payment Methods
                        {"value": "automatic_payment_methods", "label": "Automatic payment methods configuration"},
                        {"value": "automatic_payment_methods.enabled", "label": "Enable automatic payment methods"},
                        {"value": "automatic_payment_methods.allow_redirects", "label": "Allow redirect-based payment methods"},
                        
                        # Customer and Future Usage
                        {"value": "customer", "label": "Customer ID"},
                        {"value": "setup_future_usage", "label": "Setup future usage type"},
                        {"value": "off_session", "label": "Off-session payment configuration"},
                        
                        # Confirmation Settings
                        {"value": "confirm", "label": "Whether to confirm the payment immediately"},
                        {"value": "confirmation_method", "label": "Confirmation method type"},
                        {"value": "capture_method", "label": "Capture method type"},
                        {"value": "confirmation_token", "label": "Confirmation token"},
                        {"value": "error_on_requires_action", "label": "Error on requires action"},
                        {"value": "mandate", "label": "Mandate ID for recurring payments"},
                        {"value": "mandate_data", "label": "Mandate data for new mandates"},
                        
                        # Shipping Information
                        {"value": "shipping", "label": "Shipping information"},
                        {"value": "shipping.name", "label": "Shipping recipient name"},
                        {"value": "shipping.phone", "label": "Shipping phone number"},
                        {"value": "shipping.address", "label": "Shipping address object"},
                        {"value": "shipping.address.line1", "label": "Shipping address line 1"},
                        {"value": "shipping.address.line2", "label": "Shipping address line 2"},
                        {"value": "shipping.address.city", "label": "Shipping city"},
                        {"value": "shipping.address.state", "label": "Shipping state/province"},
                        {"value": "shipping.address.postal_code", "label": "Shipping postal code"},
                        {"value": "shipping.address.country", "label": "Shipping country code"},
                        
                        # Connect Specific
                        {"value": "application_fee_amount", "label": "Application fee amount"},
                        {"value": "on_behalf_of", "label": "Connected account ID"},
                        {"value": "transfer_data", "label": "Transfer data configuration"},
                        {"value": "transfer_data.destination", "label": "Transfer destination account"},
                        {"value": "transfer_data.amount", "label": "Transfer amount"},
                        {"value": "transfer_group", "label": "Transfer group identifier"},
                        
                        # Amount Details
                        {"value": "amount_details", "label": "Amount details object"},
                        {"value": "amount_details.tip", "label": "Tip amount details"},
                        {"value": "amount_details.tip.amount", "label": "Tip amount value"},
                        {"value": "amount_details.tip.amount_off_session", "label": "Off-session tip amount"},
                        {"value": "amount_details.tip.amount_on_session", "label": "On-session tip amount"},
                        
                        # Additional Settings
                        {"value": "radar_options", "label": "Radar options configuration"},
                        {"value": "radar_options.session", "label": "Radar session ID"},
                        {"value": "return_url", "label": "Return URL after payment"},
                        {"value": "use_stripe_sdk", "label": "Use Stripe SDK flag"},
                        {"value": "processing", "label": "Processing configuration"},
                        {"value": "processing.type", "label": "Processing type"},
                        {"value": "processing.card_present", "label": "Card present processing options"},
                        {"value": "processing.card_present.request_extended_authorization", "label": "Request extended authorization"},
                        {"value": "processing.card_present.request_incremental_authorization_support", "label": "Request incremental authorization support"},
                        {"value": "processing.card_present.request_incremental_authorization", "label": "Request incremental authorization"},
                        {"value": "processing.card_present.request_incremental_authorization.amount", "label": "Incremental authorization amount"},
                        {"value": "processing.card_present.request_incremental_authorization.currency", "label": "Incremental authorization currency"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_off_session", "label": "Off-session incremental authorization amount"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_on_session", "label": "On-session incremental authorization amount"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_automatic", "label": "Automatic incremental authorization amount"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_suggested", "label": "Suggested incremental authorization amount"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_manual", "label": "Manual incremental authorization amount"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_manual.amount", "label": "Manual incremental authorization amount value"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_manual.currency", "label": "Manual incremental authorization amount currency"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_manual.amount_off_session", "label": "Manual off-session incremental authorization amount"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_manual.amount_on_session", "label": "Manual on-session incremental authorization amount"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_manual.amount_automatic", "label": "Manual automatic incremental authorization amount"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_manual.amount_suggested", "label": "Manual suggested incremental authorization amount"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_manual.amount_manual", "label": "Manual manual incremental authorization amount"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_manual.amount_manual.amount", "label": "Manual manual incremental authorization amount value"},
                        {"value": "processing.card_present.request_incremental_authorization.amount_manual.amount_manual.currency", "label": "Manual manual incremental authorization amount currency"}
                    ]
                }
            },
            {
                "retrieve": {
                    "required_fields": [
                        {"value": "payment_intent", "label": "Payment Intent ID"}
                    ],
                    "optional_fields": [
                        {"value": "client_secret", "label": "Client secret for client-side retrieval"},
                        {"value": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "list": {
                    "required_fields": [
                        {"value": "limit", "label": "Maximum number of objects to return"}
                    ],
                    "optional_fields": [
                        # Pagination
                        {"value": "starting_after", "label": "Cursor for pagination (start after)"},
                        {"value": "ending_before", "label": "Cursor for pagination (end before)"},
                        
                        # Date Filters
                        {"value": "created", "label": "Creation date filter"},
                        {"value": "created.gt", "label": "Created after timestamp"},
                        {"value": "created.gte", "label": "Created on or after timestamp"},
                        {"value": "created.lt", "label": "Created before timestamp"},
                        {"value": "created.lte", "label": "Created on or before timestamp"},
                        
                        # Other Filters
                        {"value": "customer", "label": "Filter by customer ID"},
                        {"value": "payment_method", "label": "Filter by payment method ID"},
                        {"value": "transfer_data.destination", "label": "Filter by transfer destination"},
                        {"value": "transfer_group", "label": "Filter by transfer group"},
                        {"value": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "cancel": {
                    "required_fields": [
                        {"value": "id", "label": "Payment Intent ID"}
                    ],
                    "optional_fields": [
                        {"value": "cancellation_reason", "label": "Reason for cancellation"},
                        {"value": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "capture": {
                    "required_fields": [
                        {"value": "id", "label": "Payment Intent ID"}
                    ],
                    "optional_fields": [
                        {"value": "amount_to_capture", "label": "Amount to capture"},
                        {"value": "application_fee_amount", "label": "Application fee amount"},
                        {"value": "statement_descriptor", "label": "Statement descriptor"},
                        {"value": "statement_descriptor_suffix", "label": "Statement descriptor suffix"},
                        {"value": "transfer_data", "label": "Transfer data configuration"},
                        {"value": "transfer_data.destination", "label": "Transfer destination account"},
                        {"value": "transfer_data.amount", "label": "Transfer amount"},
                        {"value": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "confirm": {
                    "required_fields": [
                        {"value": "id", "label": "Payment Intent ID"}
                    ],
                    "optional_fields": [
                        {"value": "payment_method", "label": "Payment method ID"},
                        {"value": "payment_method_data", "label": "Payment method data"},
                        {"value": "payment_method_options", "label": "Payment method options"},
                        {"value": "receipt_email", "label": "Receipt email"},
                        {"value": "return_url", "label": "Return URL"},
                        {"value": "setup_future_usage", "label": "Setup future usage"},
                        {"value": "shipping", "label": "Shipping information"},
                        {"value": "use_stripe_sdk", "label": "Use Stripe SDK"},
                        {"value": "mandate", "label": "Mandate ID"},
                        {"value": "mandate_data", "label": "Mandate data"},
                        {"value": "off_session", "label": "Off-session configuration"},
                        {"value": "error_on_requires_action", "label": "Error on requires action"},
                        {"value": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "increment_authorization": {
                    "required_fields": [
                        {"value": "id", "label": "Payment Intent ID"},
                        {"value": "amount", "label": "Amount to increment authorization by"}
                    ],
                    "optional_fields": [
                        {"value": "description", "label": "Description of the increment"},
                        {"value": "statement_descriptor", "label": "Statement descriptor"},
                        {"value": "statement_descriptor_suffix", "label": "Statement descriptor suffix"},
                        {"value": "metadata", "label": "Additional metadata"},
                        {"value": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "verify_microdeposits": {
                    "required_fields": [
                        {"value": "id", "label": "Payment Intent ID"}
                    ],
                    "optional_fields": [
                        {"value": "amounts", "label": "Microdeposit amounts"},
                        {"value": "descriptor_code", "label": "Descriptor code"},
                        {"value": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "search": {
                    "required_fields": [
                        {"value": "query", "label": "Search query"},
                        {"value": "limit", "label": "Maximum number of objects to return"}
                    ],
                    "optional_fields": [
                        {"value": "page", "label": "Page number for pagination"},
                        {"value": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            }
        ]
    },
    {
        "object_type": "balance",
        "action": [
            {
                "retrieve": {
                    "required_fields": [],
                    "optional_fields": []
                    
                }
            }
        ]
    },
    {
        "object_type": "balance_transaction",
        "action": [
            {
                "retrieve": {
                    "required_fields": [],
                    "optional_fields": []
                }
            },
            {
                "list": {
                    "required_fields": [
                        {"value": "limit", "label": "Maximum number of objects to return"}
                    ],
                    "optional_fields": [
                        # Pagination
                        {"value": "starting_after", "label": "Cursor for pagination (start after)"},
                        {"value": "ending_before", "label": "Cursor for pagination (end before)"},
                        
                        # Filters
                        {"value": "payout", "label": "Filter by payout ID"},
                        {"value": "type", "label": "Filter by transaction type"},
                        {"value": "currency", "label": "Filter by currency"},
                        {"value": "source", "label": "Filter by source object"},
                        
                        # Date Filters
                        {"value": "created", "label": "Filter by creation date"},
                        {"value": "created.gt", "label": "Created after timestamp"},
                        {"value": "created.gte", "label": "Created on or after timestamp"},
                        {"value": "created.lt", "label": "Created before timestamp"},
                        {"value": "created.lte", "label": "Created on or before timestamp"}
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


__all__ = ["OBJECT_TYPE", "CREATE_OBJECT_TYPE", "UPDATE_OBJECT_TYPE", "RETRIEVE_OBJECT_TYPE", "LIST_OBJECT_TYPE", "CUSTOME_OBJECT_TYPE"]













