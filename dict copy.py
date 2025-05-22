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
                        {"id": "name", "label": "Full Name or Business Name"},
                        {"id": "email", "label": "Email Address"},
                        {"id": "phone", "label": "Phone Number"},
                        {"id": "description", "label": "Description"},
                        {"id": "metadata", "label": "Metadata"},
                        
                        # Address Information
                        {"id": "address", "label": "Address"},
                        {"id": "address.line1", "label": "Address Line 1"},
                        {"id": "address.line2", "label": "Address Line 2"},
                        {"id": "address.city", "label": "City"},
                        {"id": "address.state", "label": "State"},
                        {"id": "address.postal_code", "label": "Postal Code"},
                        {"id": "address.country", "label": "Country"},
                        
                        
                        # Payment Information
                        {"id": "payment_method", "label": "Payment Method"},
                        {"id": "source", "label": "Source"},
                        
                        # Balance Information
                        {"id": "balance", "label": "Balance"},
                        {"id": "cash_balance", "label": "Cash Balance"},
                        
                        # Invoice Settings
                        {"id": "invoice_prefix", "label": "Invoice Prefix"},
                        {"id": "invoice_settings", "label": "Invoice Settings"},
                        {"id": "invoice_settings_custom_fields", "label": "Custom Fields"},
                        {"id": "invoice_settings_default_payment_method", "label": "Default Payment Method"},
                        {"id": "invoice_settings_footer", "label": "Invoice Footer"},
                        {"id": "invoice_settings_rendering_options", "label": "Rendering Options"},
                        {"id": "next_invoice_sequence", "label": "Next Invoice Sequence"},
                        
                        # Shipping Information
                        {"id": "shipping", "label": "Shipping Information"},
                        {"id": "shipping.name", "label": "Shipping Recipient Name"},
                        {"id": "shipping.phone", "label": "Shipping Phone Number"},
                        {"id": "shipping.address", "label": "Shipping Address"},
                        {"id": "shipping.address.line1", "label": "Shipping Address Line 1"},
                        {"id": "shipping.address.line2", "label": "Shipping Address Line 2"},
                        {"id": "shipping.address.city", "label": "Shipping City"},
                        {"id": "shipping.address.state", "label": "Shipping State or Province"},
                        {"id": "shipping.address.postal_code", "label": "Shipping Postal Code"},
                        {"id": "shipping.address.country", "label": "Shipping Country Code"},
                        
                        # Tax Information
                        {"id": "tax", "label": "Tax Information"},
                        {"id": "tax_ip_address", "label": "Tax IP Address"},
                        {"id": "tax_validate_location", "label": "Tax Location Validation"},
                        {"id": "tax_exempt", "label": "Tax Exempt Status"},
                        {"id": "tax_id_data", "label": "Tax IDs"},
                        {"id": "tax_id_data.type", "label": "Tax ID Type"},
                        {"id": "tax_id_data.value", "label": "Tax ID Value"},
                        
                        # Additional Information
                        {"id": "preferred_locales", "label": "Preferred Languages"},
                        {"id": "test_clock", "label": "Test Clock"}
                    ]
                }
            },
            {
                "update": {
                    "required_fields": [
                        {"id": "id", "label": "Customer ID"}
                    ],
                    "optional_fields": [
                        # Basic Information
                        {"id": "name", "label": "Full Name or Business Name"},
                        {"id": "email", "label": "Email Address"},
                        {"id": "phone", "label": "Phone Number"},
                        {"id": "description", "label": "Description"},
                        {"id": "metadata", "label": "Metadata"},
                        
                        # Address Information
                        {"id": "address", "label": "Address"},
                        {"id": "address.line1", "label": "Address Line 1"},
                        {"id": "address.line2", "label": "Address Line 2"},
                        {"id": "address.city", "label": "City"},
                        {"id": "address.state", "label": "State"},
                        {"id": "address.postal_code", "label": "Postal Code"},
                        {"id": "address.country", "label": "Country"},
                        
                        # Payment Information
                        {"id": "default_source", "label": "Default Payment Source"},
                        {"id": "source", "label": "Payment Source"},
                        
                        # Balance Information
                        {"id": "balance", "label": "Balance"},
                        {"id": "cash_balance", "label": "Cash Balance"},
                        
                        # Invoice Settings
                        {"id": "invoice_prefix", "label": "Invoice Prefix"},
                        {"id": "invoice_settings", "label": "Invoice Settings"},
                        {"id": "invoice_settings_custom_fields", "label": "Custom Fields"},
                        {"id": "invoice_settings_default_payment_method", "label": "Default Payment Method"},
                        {"id": "invoice_settings_footer", "label": "Invoice Footer"},
                        {"id": "invoice_settings_rendering_options", "label": "Rendering Options"},
                        {"id": "next_invoice_sequence", "label": "Next Invoice Sequence"},
                        
                        # Shipping Information
                        {"id": "shipping", "label": "Shipping Information"},
                        {"id": "shipping.name", "label": "Shipping Recipient Name"},
                        {"id": "shipping.phone", "label": "Shipping Phone Number"},
                        {"id": "shipping.address", "label": "Shipping Address"},
                        {"id": "shipping.address.line1", "label": "Shipping Address Line 1"},
                        {"id": "shipping.address.line2", "label": "Shipping Address Line 2"},
                        {"id": "shipping.address.city", "label": "Shipping City"},
                        {"id": "shipping.address.state", "label": "Shipping State or Province"},
                        {"id": "shipping.address.postal_code", "label": "Shipping Postal Code"},
                        {"id": "shipping.address.country", "label": "Shipping Country Code"},
                        
                        # Tax Information
                        {"id": "tax", "label": "Tax Information"},
                        {"id": "tax_exempt", "label": "Tax Exempt Status"},
                        
                        # Additional Information
                        {"id": "preferred_locales", "label": "Preferred Languages"}
                    ]
                }
            },
            {
                "get": {
                    "required_fields": [
                        {"id": "customer", "label": "Customer ID"}
                    ],
                    "optional_fields": []
                }
            },
            {
                "list": {
                    "required_fields": [
                        {"id": "limit", "label": "Limit"}
                    ],
                    "optional_fields": [
                        # Pagination
                        {"id": "starting_after", "label": "Starting After"},
                        {"id": "ending_before", "label": "Ending Before"},
                        
                        # Date Filters
                        {"id": "created_gt", "label": "Created After"},
                        {"id": "created_gte", "label": "Created On or After"},
                        {"id": "created_lt", "label": "Created Before"},
                        {"id": "created_lte", "label": "Created On or Before"},
                        
                        # Other Filters
                        {"id": "email", "label": "Email Filter"},
                        {"id": "test_clock", "label": "Test Clock"}
                    ]
                }
            },
            {
                "delete": {
                    "required_fields": [
                        {"id": "id", "label": "Customer ID"}
                    ],
                    "optional_fields": []
                }
            },
            {
                "search": {
                    "required_fields": [
                        {"id": "query", "label": "Search Query"},
                        {"id": "limit", "label": "Result Limit"}
                    ],
                    "optional_fields": [
                        {"id": "page", "label": "Page Number"}
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
                        {"id": "amount", "label": "Amount"},
                        {"id": "currency", "label": "Currency"}
                    ],
                    "optional_fields": [
                        # Basic Information
                        {"id": "customer", "label": "Customer ID"},

                        # Payment Source
                        {"id": "source", "label": "Payment Source"},

                        # Basic Information 2 
                        {"id": "description", "label": "Description"},
                        {"id": "metadata", "label": "Metadata"},
                        {"id": "receipt_email", "label": "Receipt Email"},
                        
                        
                        
                        # Statement Information
                        {"id": "statement_descriptor", "label": "Statement Descriptor"},
                        {"id": "statement_descriptor_suffix", "label": "Statement Descriptor Suffix"},
                        
                        # Shipping Information
                        {"id": "shipping", "label": "Shipping Information"},
                        {"id": "shipping.name", "label": "Shipping Recipient Name"},
                        {"id": "shipping.phone", "label": "Shipping Phone Number"},
                        {"id": "shipping_carrier", "label": "Shipping Carrier"},
                        {"id": "shipping_tracking_number", "label": "Tracking Number"},
                        {"id": "shipping.address", "label": "Shipping Address"},
                        {"id": "shipping.address.line1", "label": "Shipping Address Line 1"},
                        {"id": "shipping.address.line2", "label": "Shipping Address Line 2"},
                        {"id": "shipping.address.city", "label": "Shipping City"},
                        {"id": "shipping.address.state", "label": "Shipping State or Province"},
                        {"id": "shipping.address.postal_code", "label": "Shipping Postal Code"},
                        {"id": "shipping.address.country", "label": "Shipping Country Code"},
                        
                        # Payment Settings
                        {"id": "capture", "label": "Capture"},
                        {"id": "application_fee_amount", "label": "Application Fee Amount"},
                        {"id": "on_behalf_of", "label": "On Behalf Of"},
                        
                        # Connect Specific
                        {"id": "transfer_data", "label": "Transfer Data"},
                        {"id": "transfer_group", "label": "Transfer Group"},
                        
                        # Radar Options
                        {"id": "radar_options", "label": "Radar Options"}
                    ]
                }
            },
            {
                "update": {
                    "required_fields": [
                        {"id": "id", "label": "Charge ID"}
                    ],
                    "optional_fields": [
                        # Basic Information
                        {"id": "customer", "label": "Customer ID"},
                        {"id": "description", "label": "Description"},
                        {"id": "metadata", "label": "Metadata"},
                        {"id": "receipt_email", "label": "Receipt Email"},
                        
                        # Shipping Information
                        {"id": "shipping", "label": "Shipping Information"},
                        {"id": "shipping.name", "label": "Shipping Recipient Name"},
                        {"id": "shipping.phone", "label": "Shipping Phone Number"},
                        {"id": "shipping_carrier", "label": "Shipping Carrier"},
                        {"id": "shipping_tracking_number", "label": "Tracking Number"},
                        {"id": "shipping.address", "label": "Shipping Address"},
                        {"id": "shipping.address.line1", "label": "Shipping Address Line 1"},
                        {"id": "shipping.address.line2", "label": "Shipping Address Line 2"},
                        {"id": "shipping.address.city", "label": "Shipping City"},
                        {"id": "shipping.address.state", "label": "Shipping State or Province"},
                        {"id": "shipping.address.postal_code", "label": "Shipping Postal Code"},
                        {"id": "shipping.address.country", "label": "Shipping Country Code"},
                        
                        # Fraud Details
                        {"id": "fraud_details", "label": "Fraud Details"},
                        
                        # Connect Specific
                        {"id": "transfer_group", "label": "Transfer Group"}
                    ]
                }
            },
            {
                "get": {
                    "required_fields": [
                        {"id": "charge", "label": "Charge ID"}
                    ],
                    "optional_fields": []
                }
            },
            {
                "list": {
                    "required_fields": [
                        {"id": "limit", "label": "Limit"}
                    ],
                    "optional_fields": [
                        # Pagination
                        {"id": "starting_after", "label": "Starting After"},
                        {"id": "ending_before", "label": "Ending Before"},
                        
                        # Date Filters
                        {"id": "created_gt", "label": "Created After"},
                        {"id": "created_gte", "label": "Created On or After"},
                        {"id": "created_lt", "label": "Created Before"},
                        {"id": "created_lte", "label": "Created On or Before"},
                        
                        # Other Filters
                        {"id": "email", "label": "Email Filter"},
                        {"id": "test_clock", "label": "Test Clock"}
                    ]
                }
            },
            {
                "delete": {
                    "required_fields": [
                        {"id": "id", "label": "Charge ID"}
                    ],
                    "optional_fields": []
                }
            },
            {
                "search": {
                    "required_fields": [
                        {"id": "query", "label": "Search Query"},
                        {"id": "limit", "label": "Result Limit"}
                    ],
                    "optional_fields": [
                        {"id": "page", "label": "Page Number"}
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
                        {"id": "amount", "label": "Amount in cents"},
                        {"id": "currency", "label": "Three-letter ISO currency code"}
                    ],
                    "optional_fields": [
                        # Basic Information
                        {"id": "description", "label": "Description of the payment"},
                        {"id": "metadata", "label": "Additional metadata"},
                        {"id": "receipt_email", "label": "Email for receipt"},
                        {"id": "statement_descriptor", "label": "Statement descriptor (max 22 chars)"},
                        {"id": "statement_descriptor_suffix", "label": "Statement descriptor suffix"},
                        
                        # Payment Method Configuration
                        {"id": "payment_method_types", "label": "List of payment method types to accept"},
                        {"id": "payment_method", "label": "Specific payment method to use"},
                        {"id": "payment_method_data", "label": "Payment method data for new payment methods"},
                        {"id": "payment_method_options", "label": "Payment method specific options"},
                        {"id": "payment_method_options_card", "label": "Card payment method options"},
                        {"id": "payment_method_options_card_installments", "label": "Card installments configuration"},
                        {"id": "payment_method_options_card_mandate_options", "label": "Card mandate options"},
                        {"id": "payment_method_options_card_network", "label": "Specific card network"},
                        {"id": "payment_method_options_card_request_three_d_secure", "label": "3D Secure request type"},
                        {"id": "payment_method_options_card_setup_future_usage", "label": "Setup future usage for card"},
                        {"id": "payment_method_options_card_capture_method", "label": "Capture method for card"},
                        {"id": "payment_method_options_card_verification_method", "label": "Verification method for card"},
                        
                        # Automatic Payment Methods
                        {"id": "automatic_payment_methods", "label": "Automatic payment methods configuration"},
                        {"id": "automatic_payment_methods_enabled", "label": "Enable automatic payment methods"},
                        {"id": "automatic_payment_methods_allow_redirects", "label": "Allow redirect-based payment methods"},
                        
                        # Customer and Future Usage
                        {"id": "customer", "label": "Customer ID"},
                        {"id": "setup_future_usage", "label": "Setup future usage type"},
                        {"id": "off_session", "label": "Off-session payment configuration"},
                        
                        # Confirmation Settings
                        {"id": "confirm", "label": "Whether to confirm the payment immediately"},
                        {"id": "confirmation_method", "label": "Confirmation method type"},
                        {"id": "capture_method", "label": "Capture method type"},
                        {"id": "confirmation_token", "label": "Confirmation token"},
                        {"id": "error_on_requires_action", "label": "Error on requires action"},
                        {"id": "mandate", "label": "Mandate ID for recurring payments"},
                        {"id": "mandate_data", "label": "Mandate data for new mandates"},
                        
                        # Shipping Information
                        {"id": "shipping", "label": "Shipping Information"},
                        {"id": "shipping.name", "label": "Shipping Recipient Name"},
                        {"id": "shipping.phone", "label": "Shipping Phone Number"},
                        {"id": "shipping.address", "label": "Shipping Address Object"},
                        {"id": "shipping.address.line1", "label": "Shipping Address Line 1"},
                        {"id": "shipping.address.line2", "label": "Shipping Address Line 2"},
                        {"id": "shipping.address.city", "label": "Shipping City"},
                        {"id": "shipping.address.state", "label": "Shipping State or Province"},
                        {"id": "shipping.address.postal_code", "label": "Shipping Postal Code"},
                        {"id": "shipping.address.country", "label": "Shipping Country Code"},
                        
                        # Connect Specific
                        {"id": "application_fee_amount", "label": "Application fee amount"},
                        {"id": "on_behalf_of", "label": "Connected account ID"},
                        {"id": "transfer_data", "label": "Transfer data configuration"},
                        {"id": "transfer_data_destination", "label": "Transfer destination account"},
                        {"id": "transfer_data_amount", "label": "Transfer amount"},
                        {"id": "transfer_group", "label": "Transfer group identifier"},
                        
                        # Amount Details
                        {"id": "amount_details", "label": "Amount details object"},
                        {"id": "amount_details_tip", "label": "Tip amount details"},
                        {"id": "amount_details_tip_amount", "label": "Tip amount value"},
                        {"id": "amount_details_tip_amount_off_session", "label": "Off-session tip amount"},
                        {"id": "amount_details_tip_amount_on_session", "label": "On-session tip amount"},
                        
                        # Additional Settings
                        {"id": "radar_options", "label": "Radar options configuration"},
                        {"id": "radar_options_session", "label": "Radar session ID"},
                        {"id": "return_url", "label": "Return URL after payment"},
                        {"id": "use_stripe_sdk", "label": "Use Stripe SDK flag"},
                        {"id": "processing", "label": "Processing configuration"},
                        {"id": "processing_type", "label": "Processing type"},
                        {"id": "processing_card_present", "label": "Card present processing options"},
                        {"id": "processing_card_present_request_extended_authorization", "label": "Request extended authorization"},
                        {"id": "processing_card_present_request_incremental_authorization_support", "label": "Request incremental authorization support"},
                        {"id": "processing_card_present_request_incremental_authorization", "label": "Request incremental authorization"},
                        {"id": "processing_card_present_request_incremental_authorization_amount", "label": "Incremental authorization amount"},
                        {"id": "processing_card_present_request_incremental_authorization_currency", "label": "Incremental authorization currency"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_off_session", "label": "Off-session incremental authorization amount"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_on_session", "label": "On-session incremental authorization amount"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_automatic", "label": "Automatic incremental authorization amount"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_suggested", "label": "Suggested incremental authorization amount"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_manual", "label": "Manual incremental authorization amount"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_manual_amount", "label": "Manual incremental authorization amount value"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_manual_currency", "label": "Manual incremental authorization amount currency"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_manual_amount_off_session", "label": "Manual off-session incremental authorization amount"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_manual_amount_on_session", "label": "Manual on-session incremental authorization amount"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_manual_amount_automatic", "label": "Manual automatic incremental authorization amount"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_manual_amount_suggested", "label": "Manual suggested incremental authorization amount"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_manual_amount_manual", "label": "Manual manual incremental authorization amount"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_manual_amount_manual_amount", "label": "Manual manual incremental authorization amount value"},
                        {"id": "processing_card_present_request_incremental_authorization_amount_manual_amount_manual_currency", "label": "Manual manual incremental authorization amount currency"}
                    ]
                }
            },
            {
                "get": {
                    "required_fields": [
                        {"id": "payment_intent", "label": "Payment Intent ID"}
                    ],
                    "optional_fields": [
                        {"id": "client_secret", "label": "Client secret for client-side retrieval"},
                        {"id": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "list": {
                    "required_fields": [
                        {"id": "limit", "label": "Maximum number of objects to return"}
                    ],
                    "optional_fields": [
                        # Pagination
                        {"id": "starting_after", "label": "Cursor for pagination (start after)"},
                        {"id": "ending_before", "label": "Cursor for pagination (end before)"},
                        
                        # Date Filters
                        {"id": "created", "label": "Filter by creation date"},
                        {"id": "created_gt", "label": "Created after timestamp"},
                        {"id": "created_gte", "label": "Created on or after timestamp"},
                        {"id": "created_lt", "label": "Created before timestamp"},
                        {"id": "created_lte", "label": "Created on or before timestamp"},
                        
                        # Other Filters
                        {"id": "customer", "label": "Filter by customer ID"},
                        {"id": "payment_method", "label": "Filter by payment method ID"},
                        {"id": "transfer_data_destination", "label": "Filter by transfer destination"},
                        {"id": "transfer_group", "label": "Filter by transfer group"},
                        {"id": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "cancel": {
                    "required_fields": [
                        {"id": "id", "label": "Payment Intent ID"}
                    ],
                    "optional_fields": [
                        {"id": "cancellation_reason", "label": "Reason for cancellation"},
                        {"id": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "capture": {
                    "required_fields": [
                        {"id": "id", "label": "Payment Intent ID"}
                    ],
                    "optional_fields": [
                        {"id": "amount_to_capture", "label": "Amount to capture"},
                        {"id": "application_fee_amount", "label": "Application fee amount"},
                        {"id": "statement_descriptor", "label": "Statement descriptor"},
                        {"id": "statement_descriptor_suffix", "label": "Statement descriptor suffix"},
                        {"id": "transfer_data", "label": "Transfer data configuration"},
                        {"id": "transfer_data_destination", "label": "Transfer destination account"},
                        {"id": "transfer_data_amount", "label": "Transfer amount"},
                        {"id": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "confirm": {
                    "required_fields": [
                        {"id": "id", "label": "Payment Intent ID"}
                    ],
                    "optional_fields": [
                        {"id": "payment_method", "label": "Payment method ID"},
                        {"id": "payment_method_data", "label": "Payment method data"},
                        {"id": "payment_method_options", "label": "Payment method options"},
                        {"id": "receipt_email", "label": "Receipt email"},
                        {"id": "return_url", "label": "Return URL"},
                        {"id": "setup_future_usage", "label": "Setup future usage"},
                        {"id": "shipping", "label": "Shipping Information"},
                        {"id": "use_stripe_sdk", "label": "Use Stripe SDK"},
                        {"id": "mandate", "label": "Mandate ID"},
                        {"id": "mandate_data", "label": "Mandate data"},
                        {"id": "off_session", "label": "Off-session configuration"},
                        {"id": "error_on_requires_action", "label": "Error on requires action"},
                        {"id": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "increment_authorization": {
                    "required_fields": [
                        {"id": "id", "label": "Payment Intent ID"},
                        {"id": "amount", "label": "Amount to increment authorization by"}
                    ],
                    "optional_fields": [
                        {"id": "description", "label": "Description of the increment"},
                        {"id": "statement_descriptor", "label": "Statement descriptor"},
                        {"id": "statement_descriptor_suffix", "label": "Statement descriptor suffix"},
                        {"id": "metadata", "label": "Additional metadata"},
                        {"id": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "verify_microdeposits": {
                    "required_fields": [
                        {"id": "id", "label": "Payment Intent ID"}
                    ],
                    "optional_fields": [
                        {"id": "amounts", "label": "Microdeposit amounts"},
                        {"id": "descriptor_code", "label": "Descriptor code"},
                        {"id": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "search": {
                    "required_fields": [
                        {"id": "query", "label": "Search query"},
                        {"id": "limit", "label": "Maximum number of objects to return"}
                    ],
                    "optional_fields": [
                        {"id": "page", "label": "Page number for pagination"},
                        {"id": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            }
        ]
    },
    {
        "object_type": "balance",
        "action": [
            {
                "get": {
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
                "get": {
                    "required_fields": [
                        {"id":"balance_transaction", "label":"Balance transaction ID"}
                    ],
                    "optional_fields": []
                }
            },
            {
                "list": {
                    "required_fields": [
                        {"id": "limit", "label": "Maximum number of objects to return"}
                    ],
                    "optional_fields": [
                        # Pagination
                        {"id": "starting_after", "label": "Cursor for pagination (start after)"},
                        {"id": "ending_before", "label": "Cursor for pagination (end before)"},
                        
                        # Filters
                        {"id": "payout", "label": "Filter by payout ID"},
                        {"id": "type", "label": "Filter by transaction type"},
                        {"id": "currency", "label": "Filter by currency"},
                        {"id": "source", "label": "Filter by source object"},
                        
                        # Date Filters
                        {"id": "created", "label": "Filter by creation date"},
                        {"id": "created_gt", "label": "Created after timestamp"},
                        {"id": "created_gte", "label": "Created on or after timestamp"},
                        {"id": "created_lt", "label": "Created before timestamp"},
                        {"id": "created_lte", "label": "Created on or before timestamp"}
                    ]
                }
            }
        ]
    }
]


CREATE_OBJECT_TYPE = []
UPDATE_OBJECT_TYPE = []
GET_OBJECT_TYPE = []
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
            elif key == "get":
                GET_OBJECT_TYPE.append(object_type)
            elif key == "list":
                LIST_OBJECT_TYPE.append(object_type)
            else:
                CUSTOME_OBJECT_TYPE.append(object_type)

print("CREATE_OBJECT_TYPE",CREATE_OBJECT_TYPE)
print("UPDATE_OBJECT_TYPE",UPDATE_OBJECT_TYPE)
print("GET_OBJECT_TYPE ",GET_OBJECT_TYPE)
print("LIST_OBJECT_TYPE",LIST_OBJECT_TYPE)
print("CUSTOME_OBJECT_TYPE",CUSTOME_OBJECT_TYPE)


__all__ = ["OBJECT_TYPE", "CREATE_OBJECT_TYPE", "UPDATE_OBJECT_TYPE", "GET_OBJECT_TYPE", "LIST_OBJECT_TYPE", "CUSTOME_OBJECT_TYPE"]












