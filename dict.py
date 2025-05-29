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
                        {"id": "address[line1]", "label": "Address Line 1"},
                        {"id": "address[line2]", "label": "Address Line 2"},
                        {"id": "address[city]", "label": "City"},
                        {"id": "address[state]", "label": "State"},
                        {"id": "address[postal_code]", "label": "Postal Code"},
                        {"id": "address[country]", "label": "Country"},
                        
                        # Payment Information
                        {"id": "payment_method", "label": "Payment Method"},
                        {"id": "source", "label": "Source"},
                        
                        # Balance Information
                        {"id": "balance", "label": "Balance"},
                        {"id": "cash_balance", "label": "Cash Balance"},
                        
                        # Invoice Settings
                        {"id": "invoice_prefix", "label": "Invoice Prefix"},
                        {"id": "invoice_settings[custom_fields]", "label": "Custom Fields"},
                        {"id": "invoice_settings[default_payment_method]", "label": "Default Payment Method"},
                        {"id": "invoice_settings[footer]", "label": "Invoice Footer"},
                        {"id": "invoice_settings[rendering_options]", "label": "Rendering Options"},
                        {"id": "next_invoice_sequence", "label": "Next Invoice Sequence"},
                        
                        # Shipping Information
                        {"id": "shipping[name]", "label": "Shipping Recipient Name"},
                        {"id": "shipping[phone]", "label": "Shipping Phone Number"},
                        {"id": "shipping[address][line1]", "label": "Shipping Address Line 1"},
                        {"id": "shipping[address][line2]", "label": "Shipping Address Line 2"},
                        {"id": "shipping[address][city]", "label": "Shipping City"},
                        {"id": "shipping[address][state]", "label": "Shipping State or Province"},
                        {"id": "shipping[address][postal_code]", "label": "Shipping Postal Code"},
                        {"id": "shipping[address][country]", "label": "Shipping Country Code"},
                        
                        # Tax Information
                        {"id": "tax[ip_address]", "label": "Tax IP Address"},
                        {"id": "tax[validate_location]", "label": "Tax Location Validation"},
                        {"id": "tax_exempt", "label": "Tax Exempt Status"},
                        {"id": "tax_id_data[type]", "label": "Tax ID Type"},
                        {"id": "tax_id_data[value]", "label": "Tax ID Value"},
                        
                        # Additional Information
                        {"id": "preferred_locales", "label": "Preferred Languages"},
                        {"id": "test_clock", "label": "Test Clock", "description": "A special clock for testing time-dependent features. First, you need to create a test clock using the 'Create Test Clock' action. Then, you can use its ID here to filter results for that specific test time. This lets you simulate different dates and times in your test environment. For example, if you want to test what happens when a subscription renews in the future, create a test clock, advance it to that date, and use its ID here. This only works in test mode, not in live mode. Example: clock_123456789"}
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
                        {"id": "address[line1]", "label": "Address Line 1"},
                        {"id": "address[line2]", "label": "Address Line 2"},
                        {"id": "address[city]", "label": "City"},
                        {"id": "address[state]", "label": "State"},
                        {"id": "address[postal_code]", "label": "Postal Code"},
                        {"id": "address[country]", "label": "Country"},
                        
                        # Payment Information
                        {"id": "default_source", "label": "Default Payment Source"},
                        {"id": "source", "label": "Payment Source"},
                        
                        # Balance Information
                        {"id": "balance", "label": "Balance"},
                        {"id": "cash_balance", "label": "Cash Balance"},
                        
                        # Invoice Settings
                        {"id": "invoice_prefix", "label": "Invoice Prefix"},
                        {"id": "invoice_settings[custom_fields]", "label": "Custom Fields"},
                        {"id": "invoice_settings[default_payment_method]", "label": "Default Payment Method"},
                        {"id": "invoice_settings[footer]", "label": "Invoice Footer"},
                        {"id": "invoice_settings[rendering_options]", "label": "Rendering Options"},
                        {"id": "next_invoice_sequence", "label": "Next Invoice Sequence"},
                        
                        # Shipping Information
                        {"id": "shipping[name]", "label": "Shipping Recipient Name"},
                        {"id": "shipping[phone]", "label": "Shipping Phone Number"},
                        {"id": "shipping[address][line1]", "label": "Shipping Address Line 1"},
                        {"id": "shipping[address][line2]", "label": "Shipping Address Line 2"},
                        {"id": "shipping[address][city]", "label": "Shipping City"},
                        {"id": "shipping[address][state]", "label": "Shipping State or Province"},
                        {"id": "shipping[address][postal_code]", "label": "Shipping Postal Code"},
                        {"id": "shipping[address][country]", "label": "Shipping Country Code"},
                        
                        # Tax Information
                        {"id": "tax[ip_address]", "label": "Tax IP Address"},
                        {"id": "tax[validate_location]", "label": "Tax Location Validation"},
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
                        {"id": "limit", "label": "Limit", "description": "How many customers to return (e.g., 10 for 10 customers)"}
                    ],
                    "optional_fields": [
                        # Email Filter
                        {"id": "email", "label": "Email", "description": "Find customers by email (e.g., customer@example.com)"},
                        
                        # Date Filters
                        {"id": "created[gt]", "label": "Created After", "description": "Find records created after this date. Example: To find records created after March 1, 2024, select that date in the calendar."},
                        {"id": "created[gte]", "label": "Created On or After", "description": "Find records created on or after this date. Example: To find records created on or after March 1, 2024, select that date in the calendar."},
                        {"id": "created[lt]", "label": "Created Before", "description": "Find records created before this date. Example: To find records created before March 1, 2024, select that date in the calendar."},
                        {"id": "created[lte]", "label": "Created On or Before", "description": "Find records created on or before this date. Example: To find records created on or before March 1, 2024, select that date in the calendar."},
                        
                        # Pagination
                        {"id": "starting_after", "label": "Start After", "description": "Get customers after this ID (e.g., cus_123456789)"},
                        {"id": "ending_before", "label": "End Before", "description": "Get customers before this ID (e.g., cus_123456789)"},
                        
                        # Test Clock
                        {"id": "test_clock", "label": "Test Clock", "description": "A special clock for testing time-dependent features. First, you need to create a test clock using the 'Create Test Clock' action. Then, you can use its ID here to filter results for that specific test time. This lets you simulate different dates and times in your test environment. For example, if you want to test what happens when a subscription renews in the future, create a test clock, advance it to that date, and use its ID here. This only works in test mode, not in live mode. Example: clock_123456789"}
                    ],
                    "ui_options": {
                        "ui_order": ["limit", "email", "created[gt]", "created[gte]", "created[lt]", "created[lte]", "starting_after", "ending_before", "test_clock"]
                    } 
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
                        {"id": "shipping[name]", "label": "Shipping Recipient Name"},
                        {"id": "shipping[phone]", "label": "Shipping Phone Number"},
                        {"id": "shipping[carrier]", "label": "Shipping Carrier"},
                        {"id": "shipping[tracking_number]", "label": "Tracking Number"},
                        {"id": "shipping[address][line1]", "label": "Shipping Address Line 1"},
                        {"id": "shipping[address][line2]", "label": "Shipping Address Line 2"},
                        {"id": "shipping[address][city]", "label": "Shipping City"},
                        {"id": "shipping[address][state]", "label": "Shipping State or Province"},
                        {"id": "shipping[address][postal_code]", "label": "Shipping Postal Code"},
                        {"id": "shipping[address][country]", "label": "Shipping Country Code"},
                        
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
                        {"id": "shipping[name]", "label": "Shipping Recipient Name"},
                        {"id": "shipping[phone]", "label": "Shipping Phone Number"},
                        {"id": "shipping[carrier]", "label": "Shipping Carrier"},
                        {"id": "shipping[tracking_number]", "label": "Tracking Number"},
                        {"id": "shipping[address][line1]", "label": "Shipping Address Line 1"},
                        {"id": "shipping[address][line2]", "label": "Shipping Address Line 2"},
                        {"id": "shipping[address][city]", "label": "Shipping City"},
                        {"id": "shipping[address][state]", "label": "Shipping State or Province"},
                        {"id": "shipping[address][postal_code]", "label": "Shipping Postal Code"},
                        {"id": "shipping[address][country]", "label": "Shipping Country Code"},
                        
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
                        {"id": "limit", "label": "Limit", "description": "How many charges to return (e.g., 10 for 10 charges)"}
                    ],
                    "optional_fields": [
                        # Customer Filter
                        {"id": "customer", "label": "Customer ID", "description": "Find charges for a specific customer (e.g., cus_123456789)"},
                        
                        # Date Filters
                        {"id": "created[gt]", "label": "Created After", "description": "Find charges created after this date. Example: To find charges created after March 1, 2024, select that date in the calendar."},
                        {"id": "created[gte]", "label": "Created On or After", "description": "Find charges created on or after this date. Example: To find charges created on or after March 1, 2024, select that date in the calendar."},
                        {"id": "created[lt]", "label": "Created Before", "description": "Find charges created before this date. Example: To find charges created before March 1, 2024, select that date in the calendar."},
                        {"id": "created[lte]", "label": "Created On or Before", "description": "Find charges created on or before this date. Example: To find charges created on or before March 1, 2024, select that date in the calendar."},
                        
                        # Payment Intent Filter
                        {"id": "payment_intent", "label": "Payment Intent ID", "description": "Find charges for a specific payment intent (e.g., pi_123456789)"},
                        
                        # Pagination
                        {"id": "starting_after", "label": "Start After", "description": "Get charges after this ID (e.g., ch_123456789)"},
                        {"id": "ending_before", "label": "End Before", "description": "Get charges before this ID (e.g., ch_123456789)"},
                        
                        # Transfer Group Filter
                        {"id": "transfer_group", "label": "Transfer Group", "description": "Find charges in a transfer group (e.g., tg_123456789)"},
                        
                        # Test Clock
                        {"id": "test_clock", "label": "Test Clock", "description": "A special clock for testing time-dependent features. First, you need to create a test clock using the 'Create Test Clock' action. Then, you can use its ID here to filter results for that specific test time. This lets you simulate different dates and times in your test environment. For example, if you want to test what happens when a subscription renews in the future, create a test clock, advance it to that date, and use its ID here. This only works in test mode, not in live mode. Example: clock_123456789"}
                    ],
                    "ui_options": {
                        "ui_order": ["limit", "customer", "created[gt]", "created[gte]", "created[lt]", "created[lte]", "payment_intent", "starting_after", "ending_before", "transfer_group", "test_clock"]
                    }
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
                        {"id": "amount", "label": "Amount in cents (minimum 50 cents)"},
                        {"id": "currency", "label": "Three-letter ISO currency code (e.g., 'usd')"}
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
                        {"id": "payment_method_data[type]", "label": "Type of payment method"},
                        {"id": "payment_method_data[billing_details][name]", "label": "Name on the payment method"},
                        {"id": "payment_method_data[billing_details][email]", "label": "Email for billing"},
                        {"id": "payment_method_data[billing_details][phone]", "label": "Phone for billing"},
                        {"id": "payment_method_data[billing_details][address][line1]", "label": "Billing address line 1"},
                        {"id": "payment_method_data[billing_details][address][line2]", "label": "Billing address line 2"},
                        {"id": "payment_method_data[billing_details][address][city]", "label": "Billing city"},
                        {"id": "payment_method_data[billing_details][address][state]", "label": "Billing state"},
                        {"id": "payment_method_data[billing_details][address][postal_code]", "label": "Billing postal code"},
                        {"id": "payment_method_data[billing_details][address][country]", "label": "Billing country"},
                        
                        # Payment Method Options
                        {"id": "payment_method_options", "label": "Payment method specific options"},
                        {"id": "payment_method_options[card]", "label": "Card payment method options"},
                        {"id": "payment_method_options[card][installments]", "label": "Card installments configuration"},
                        {"id": "payment_method_options[card][installments][enabled]", "label": "Enable card installments"},
                        {"id": "payment_method_options[card][installments][plan]", "label": "Installment plan type"},
                        {"id": "payment_method_options[card][mandate_options]", "label": "Card mandate options"},
                        {"id": "payment_method_options[card][mandate_options][amount]", "label": "Mandate amount"},
                        {"id": "payment_method_options[card][mandate_options][amount_type]", "label": "Mandate amount type"},
                        {"id": "payment_method_options[card][mandate_options][currency]", "label": "Mandate currency"},
                        {"id": "payment_method_options[card][mandate_options][interval]", "label": "Mandate interval"},
                        {"id": "payment_method_options[card][mandate_options][interval_count]", "label": "Mandate interval count"},
                        {"id": "payment_method_options[card][mandate_options][reference]", "label": "Mandate reference"},
                        {"id": "payment_method_options[card][mandate_options][start_date]", "label": "Mandate start date"},
                        {"id": "payment_method_options[card][mandate_options][supported_types]", "label": "Supported mandate types"},
                        {"id": "payment_method_options[card][network]", "label": "Specific card network"},
                        {"id": "payment_method_options[card][request_three_d_secure]", "label": "3D Secure request type"},
                        {"id": "payment_method_options[card][setup_future_usage]", "label": "Setup future usage for card"},
                        {"id": "payment_method_options[card][capture_method]", "label": "Capture method for card"},
                        {"id": "payment_method_options[card][verification_method]", "label": "Verification method for card"},
                        
                        # Automatic Payment Methods
                        {"id": "automatic_payment_methods", "label": "Automatic payment methods configuration"},
                        {"id": "automatic_payment_methods[enabled]", "label": "Enable automatic payment methods"},
                        {"id": "automatic_payment_methods[allow_redirects]", "label": "Allow redirect-based payment methods"},
                        
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
                        {"id": "mandate_data[customer_acceptance]", "label": "Customer acceptance data"},
                        {"id": "mandate_data[customer_acceptance][type]", "label": "Customer acceptance type"},
                        {"id": "mandate_data[customer_acceptance][online]", "label": "Online acceptance data"},
                        {"id": "mandate_data[customer_acceptance][online][ip]", "label": "IP address of acceptance"},
                        {"id": "mandate_data[customer_acceptance][online][user_agent]", "label": "User agent of acceptance"},
                        {"id": "mandate_data[customer_acceptance][offline]", "label": "Offline acceptance data"},
                        
                        # Shipping Information
                        {"id": "shipping[name]", "label": "Shipping Recipient Name"},
                        {"id": "shipping[phone]", "label": "Shipping Phone Number"},
                        {"id": "shipping[address][line1]", "label": "Shipping Address Line 1"},
                        {"id": "shipping[address][line2]", "label": "Shipping Address Line 2"},
                        {"id": "shipping[address][city]", "label": "Shipping City"},
                        {"id": "shipping[address][state]", "label": "Shipping State or Province"},
                        {"id": "shipping[address][postal_code]", "label": "Shipping Postal Code"},
                        {"id": "shipping[address][country]", "label": "Shipping Country Code"},
                        
                        # Connect Specific
                        {"id": "application_fee_amount", "label": "Application fee amount"},
                        {"id": "on_behalf_of", "label": "Connected account ID"},
                        {"id": "transfer_data", "label": "Transfer data configuration"},
                        {"id": "transfer_data[destination]", "label": "Transfer destination account"},
                        {"id": "transfer_data[amount]", "label": "Transfer amount"},
                        {"id": "transfer_group", "label": "Transfer group identifier"},
                        
                        # Amount Details
                        {"id": "amount_details", "label": "Amount details object"},
                        {"id": "amount_details[tip]", "label": "Tip amount details"},
                        {"id": "amount_details[tip][amount]", "label": "Tip amount value"},
                        
                        # Additional Settings
                        {"id": "radar_options", "label": "Radar options configuration"},
                        {"id": "radar_options[session]", "label": "Radar session ID"},
                        {"id": "return_url", "label": "Return URL after payment"},
                        {"id": "use_stripe_sdk", "label": "Use Stripe SDK flag"},
                        
                        # Processing Configuration
                        {"id": "processing", "label": "Processing configuration"},
                        {"id": "processing[type]", "label": "Processing type"},
                        {"id": "processing[card_present]", "label": "Card present processing options"},
                        {"id": "processing[card_present][request_extended_authorization]", "label": "Request extended authorization"},
                        {"id": "processing[card_present][request_incremental_authorization_support]", "label": "Request incremental authorization support"},
                        {"id": "processing[card_present][request_incremental_authorization]", "label": "Request incremental authorization"},
                        {"id": "processing[card_present][request_incremental_authorization][amount]", "label": "Incremental authorization amount"},
                        {"id": "processing[card_present][request_incremental_authorization][currency]", "label": "Incremental authorization currency"},
                        
                        # Expand Fields
                        {"id": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            },
            {
                "update": {
                    "required_fields": [
                        {"id": "id", "label": "Payment Intent ID"}
                    ],
                    "optional_fields": [
                        # Basic Information
                        {"id": "amount", "label": "Amount in cents (minimum 50 cents)"},
                        {"id": "currency", "label": "Three-letter ISO currency code (e.g., 'usd')"},
                        {"id": "description", "label": "Description of the payment"},
                        {"id": "metadata", "label": "Additional metadata"},
                        {"id": "receipt_email", "label": "Email for receipt"},
                        {"id": "statement_descriptor", "label": "Statement descriptor (max 22 chars)"},
                        {"id": "statement_descriptor_suffix", "label": "Statement descriptor suffix"},
                        
                        # Payment Method Configuration
                        {"id": "payment_method", "label": "Specific payment method to use"},
                        {"id": "payment_method_types", "label": "List of payment method types to accept"},
                        {"id": "payment_method_data[type]", "label": "Type of payment method"},
                        {"id": "payment_method_data[billing_details][name]", "label": "Name on the payment method"},
                        {"id": "payment_method_data[billing_details][email]", "label": "Email for billing"},
                        {"id": "payment_method_data[billing_details][phone]", "label": "Phone for billing"},
                        {"id": "payment_method_data[billing_details][address][line1]", "label": "Billing address line 1"},
                        {"id": "payment_method_data[billing_details][address][line2]", "label": "Billing address line 2"},
                        {"id": "payment_method_data[billing_details][address][city]", "label": "Billing city"},
                        {"id": "payment_method_data[billing_details][address][state]", "label": "Billing state"},
                        {"id": "payment_method_data[billing_details][address][postal_code]", "label": "Billing postal code"},
                        {"id": "payment_method_data[billing_details][address][country]", "label": "Billing country"},
                        
                        # Payment Method Options
                        {"id": "payment_method_options[card][installments][enabled]", "label": "Enable card installments"},
                        {"id": "payment_method_options[card][installments][plan]", "label": "Installment plan type"},
                        {"id": "payment_method_options[card][mandate_options][amount]", "label": "Mandate amount"},
                        {"id": "payment_method_options[card][mandate_options][amount_type]", "label": "Mandate amount type"},
                        {"id": "payment_method_options[card][mandate_options][currency]", "label": "Mandate currency"},
                        {"id": "payment_method_options[card][mandate_options][interval]", "label": "Mandate interval"},
                        {"id": "payment_method_options[card][mandate_options][interval_count]", "label": "Mandate interval count"},
                        {"id": "payment_method_options[card][mandate_options][reference]", "label": "Mandate reference"},
                        {"id": "payment_method_options[card][mandate_options][start_date]", "label": "Mandate start date"},
                        {"id": "payment_method_options[card][mandate_options][supported_types]", "label": "Supported mandate types"},
                        {"id": "payment_method_options[card][network]", "label": "Specific card network"},
                        {"id": "payment_method_options[card][request_three_d_secure]", "label": "3D Secure request type"},
                        {"id": "payment_method_options[card][setup_future_usage]", "label": "Setup future usage for card"},
                        {"id": "payment_method_options[card][capture_method]", "label": "Capture method for card"},
                        {"id": "payment_method_options[card][verification_method]", "label": "Verification method for card"},
                        
                        # Automatic Payment Methods
                        {"id": "automatic_payment_methods[enabled]", "label": "Enable automatic payment methods"},
                        {"id": "automatic_payment_methods[allow_redirects]", "label": "Allow redirect-based payment methods"},
                        
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
                        {"id": "mandate_data[customer_acceptance][type]", "label": "Customer acceptance type"},
                        {"id": "mandate_data[customer_acceptance][online][ip]", "label": "IP address of acceptance"},
                        {"id": "mandate_data[customer_acceptance][online][user_agent]", "label": "User agent of acceptance"},
                        {"id": "mandate_data[customer_acceptance][offline]", "label": "Offline acceptance data"},
                        
                        # Shipping Information
                        {"id": "shipping[name]", "label": "Shipping Recipient Name"},
                        {"id": "shipping[phone]", "label": "Shipping Phone Number"},
                        {"id": "shipping[carrier]", "label": "Shipping Carrier"},
                        {"id": "shipping[tracking_number]", "label": "Tracking Number"},
                        {"id": "shipping[address][line1]", "label": "Shipping Address Line 1"},
                        {"id": "shipping[address][line2]", "label": "Shipping Address Line 2"},
                        {"id": "shipping[address][city]", "label": "Shipping City"},
                        {"id": "shipping[address][state]", "label": "Shipping State or Province"},
                        {"id": "shipping[address][postal_code]", "label": "Shipping Postal Code"},
                        {"id": "shipping[address][country]", "label": "Shipping Country Code"},
                        
                        # Connect Specific
                        {"id": "application_fee_amount", "label": "Application fee amount"},
                        {"id": "on_behalf_of", "label": "Connected account ID"},
                        {"id": "transfer_data[destination]", "label": "Transfer destination account"},
                        {"id": "transfer_data[amount]", "label": "Transfer amount"},
                        {"id": "transfer_group", "label": "Transfer group identifier"},
                        
                        # Amount Details
                        {"id": "amount_details[tip][amount]", "label": "Tip amount value"},
                        
                        # Additional Settings
                        {"id": "radar_options[session]", "label": "Radar session ID"},
                        {"id": "return_url", "label": "Return URL after payment"},
                        {"id": "use_stripe_sdk", "label": "Use Stripe SDK flag"},
                        
                        # Processing Configuration
                        {"id": "processing[type]", "label": "Processing type"},
                        {"id": "processing[card_present][request_extended_authorization]", "label": "Request extended authorization"},
                        {"id": "processing[card_present][request_incremental_authorization_support]", "label": "Request incremental authorization support"},
                        {"id": "processing[card_present][request_incremental_authorization][amount]", "label": "Incremental authorization amount"},
                        {"id": "processing[card_present][request_incremental_authorization][currency]", "label": "Incremental authorization currency"},
                        
                        # Expand Fields
                        {"id": "expand", "label": "Fields to expand in the response"}
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
                        {"id": "limit", "label": "Limit", "description": "How many payment intents to return (e.g., 10 for 10 payment intents)"}
                    ],
                    "optional_fields": [
                        # Customer Filter
                        {"id": "customer", "label": "Customer ID", "description": "Find payment intents for a specific customer (e.g., cus_123456789)"},
                        
                        # Date Filters
                        {"id": "created[gt]", "label": "Created After", "description": "Find payment intents created after this date. Example: To find payment intents created after March 1, 2024, select that date in the calendar."},
                        {"id": "created[gte]", "label": "Created On or After", "description": "Find payment intents created on or after this date. Example: To find payment intents created on or after March 1, 2024, select that date in the calendar."},
                        {"id": "created[lt]", "label": "Created Before", "description": "Find payment intents created before this date. Example: To find payment intents created before March 1, 2024, select that date in the calendar."},
                        {"id": "created[lte]", "label": "Created On or Before", "description": "Find payment intents created on or before this date. Example: To find payment intents created on or before March 1, 2024, select that date in the calendar."},
                        
                        # Pagination
                        {"id": "starting_after", "label": "Start After", "description": "Get payment intents after this ID (e.g., pi_123456789)"},
                        {"id": "ending_before", "label": "End Before", "description": "Get payment intents before this ID (e.g., pi_123456789)"},
                        {"id": "test_clock", "label": "Test Clock", "description": "A special clock for testing time-dependent features. First, you need to create a test clock using the 'Create Test Clock' action. Then, you can use its ID here to filter results for that specific test time. This lets you simulate different dates and times in your test environment. For example, if you want to test what happens when a subscription renews in the future, create a test clock, advance it to that date, and use its ID here. This only works in test mode, not in live mode. Example: clock_123456789"}
                    ],
                    "ui_options": {
                        "ui_order": ["limit", "customer", "created[gt]", "created[gte]", "created[lt]", "created[lte]", "starting_after", "ending_before", "test_clock"]
                    }
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
                        {"id": "balance_transaction", "label": "Balance Transaction ID"}
                    ],
                    "optional_fields": []
                }
            },
            {
                "list": {
                    "required_fields": [
                        {"id": "limit", "label": "Limit", "description": "How many transactions to return (e.g., 10 for 10 transactions)"}
                    ],
                    "optional_fields": [
                        # Payout Filter
                        {"id": "payout", "label": "Payout ID", "description": "Find transactions for a specific payout (e.g., po_123456789)"},
                        
                        # Transaction Type Filter
                        {"id": "type", "label": "Transaction Type", "description": "Find transactions of a specific type (e.g., charge, refund, transfer)"},
                        
                        # Date Filters
                        {"id": "created[gt]", "label": "Created After", "description": "Find transactions created after this date. Example: To find transactions created after March 1, 2024, select that date in the calendar."},
                        {"id": "created[gte]", "label": "Created On or After", "description": "Find transactions created on or after this date. Example: To find transactions created on or after March 1, 2024, select that date in the calendar."},
                        {"id": "created[lt]", "label": "Created Before", "description": "Find transactions created before this date. Example: To find transactions created before March 1, 2024, select that date in the calendar."},
                        {"id": "created[lte]", "label": "Created On or Before", "description": "Find transactions created on or before this date. Example: To find transactions created on or before March 1, 2024, select that date in the calendar."},
                        
                        # Currency Filter
                        {"id": "currency", "label": "Currency", "description": "Find transactions in a specific currency in Three-letter ISO currency code, in lowercase (e.g., usd, eur)"},
                        
                        # Source Filter
                        {"id": "source", "label": "Source ID", "description": "Find transactions for a specific source (e.g., ch_123456789)"},
                        
                        # Pagination
                        {"id": "starting_after", "label": "Start After", "description": "Get transactions after this ID (e.g., txn_123456789)"},
                        {"id": "ending_before", "label": "End Before", "description": "Get transactions before this ID (e.g., txn_123456789)"}
                    ],
                    "ui_options": {
                        "ui_order": ["limit", "payout", "type", "created[gt]", "created[gte]", "created[lt]", "created[lte]", "currency", "source", "starting_after", "ending_before"]
                    }
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
        "object_type": "event",
        "action": [
            {
                "list": {
                    "required_fields": [
                        {"id": "limit", "label": "Limit", "description": "How many events to return (e.g., 10 for 10 events)"}
                    ],
                    "optional_fields": [
                        # Types Filter
                        {"id": "type", "label": "Event Type", "description": "Find specific types of events (e.g., charge.succeeded, payment_intent.created)"},
                        
                        # Date Filters
                        {"id": "created[gt]", "label": "Created After", "description": "Find events created after this date. Example: To find events created after March 1, 2024, select that date in the calendar."},
                        {"id": "created[gte]", "label": "Created On or After", "description": "Find events created on or after this date. Example: To find events created on or after March 1, 2024, select that date in the calendar."},
                        {"id": "created[lt]", "label": "Created Before", "description": "Find events created before this date. Example: To find events created before March 1, 2024, select that date in the calendar."},
                        {"id": "created[lte]", "label": "Created On or Before", "description": "Find events created on or before this date. Example: To find events created on or before March 1, 2024, select that date in the calendar."},
                        
                        # Delivery Status Filter
                        {"id": "delivery_success", "label": "Delivery Success", "description": "Find events by delivery status (true for successful, false for failed)"},
                        
                        # Pagination
                        {"id": "starting_after", "label": "Start After", "description": "Get events after this ID (e.g., evt_123456789)"},
                        {"id": "ending_before", "label": "End Before", "description": "Get events before this ID (e.g., evt_123456789)"}
                    ],
                    "ui_options": {
                        "ui_order": [ "type", "created[gt]", "created[gte]", "created[lt]", "created[lte]", "delivery_success", "starting_after", "ending_before", "limit"]
                    }
                }
            },
            {
                "get": {
                    "required_fields": [
                        {"id": "event", "label": "Event ID"}
                    ],
                    "optional_fields": [
                        {"id": "expand", "label": "Fields to expand in the response"}
                    ]
                }
            }
        ]
    },
    {
        "object_type": "product",
        "action": [
            {
                "list": {
                    "required_fields": [
                        {"id": "limit", "label": "Limit", "description": "How many products to return (e.g., 10 for 10 products)"}
                    ],
                    "optional_fields": [
                        # Active Status Filter
                        {"id": "active", "label": "Active Status", "description": "Find active or inactive products (true for active, false for inactive)"},
                        
                        # Date Filters
                        {"id": "created[gt]", "label": "Created After", "description": "Find products created after this date. Example: To find products created after March 1, 2024, select that date in the calendar."},
                        {"id": "created[gte]", "label": "Created On or After", "description": "Find products created on or after this date. Example: To find products created on or after March 1, 2024, select that date in the calendar."},
                        {"id": "created[lt]", "label": "Created Before", "description": "Find products created before this date. Example: To find products created before March 1, 2024, select that date in the calendar."},
                        {"id": "created[lte]", "label": "Created On or Before", "description": "Find products created on or before this date. Example: To find products created on or before March 1, 2024, select that date in the calendar."},
                        
                        # IDs Filter
                        {"id": "ids", "label": "Product IDs", "description": "Find specific products by their IDs (e.g., prod_123456789, prod_987654321)"},
                        
                        # Shippable Filter
                        {"id": "shippable", "label": "Shippable Status", "description": "Find shippable or non-shippable products (true for shippable, false for non-shippable)"},
                        
                        # URL Filter
                        {"id": "url", "label": "Product URL", "description": "Find products with a specific URL (e.g., https://example.com/product)"},
                        
                        # Pagination
                        {"id": "starting_after", "label": "Start After", "description": "Get products after this ID (e.g., prod_123456789)"},
                        {"id": "ending_before", "label": "End Before", "description": "Get products before this ID (e.g., prod_123456789)"}
                    ],
                    "ui_options": {
                        "ui_order": ["limit", "active", "created[gt]", "created[gte]", "created[lt]", "created[lte]", "ids", "shippable", "url", "starting_after", "ending_before"]
                    }
                }
            }
        ]
    },
    {
        "object_type": "invoice",
        "action": [
            {
                "list": {
                    "required_fields": [
                        {"id": "limit", "label": "Limit", "description": "How many invoices to return (e.g., 10 for 10 invoices)"}
                    ],
                    "optional_fields": [
                        # Customer Filter
                        {"id": "customer", "label": "Customer ID", "description": "Find invoices for a specific customer (e.g., cus_123456789)"},
                        
                        # Status Filter
                        {"id": "status", "label": "Invoice Status", "description": "Find invoices by status (draft, open, paid, uncollectible, void)"},
                        
                        # Subscription Filter
                        {"id": "subscription", "label": "Subscription ID", "description": "Find invoices for a specific subscription (e.g., sub_123456789)"},
                        
                        # Collection Method Filter
                        {"id": "collection_method", "label": "Collection Method", "description": "Find invoices by collection method (charge_automatically, send_invoice)"},
                        
                        # Date Filters
                        {"id": "created[gt]", "label": "Created After", "description": "Find invoices created after this date. Example: To find invoices created after March 1, 2024, select that date in the calendar."},
                        {"id": "created[gte]", "label": "Created On or After", "description": "Find invoices created on or after this date. Example: To find invoices created on or after March 1, 2024, select that date in the calendar."},
                        {"id": "created[lt]", "label": "Created Before", "description": "Find invoices created before this date. Example: To find invoices created before March 1, 2024, select that date in the calendar."},
                        {"id": "created[lte]", "label": "Created On or Before", "description": "Find invoices created on or before this date. Example: To find invoices created on or before March 1, 2024, select that date in the calendar."},
                        
                        # Pagination
                        {"id": "starting_after", "label": "Start After", "description": "Get invoices after this ID (e.g., in_123456789)"},
                        {"id": "ending_before", "label": "End Before", "description": "Get invoices before this ID (e.g., in_123456789)"},
                        {"id": "test_clock", "label": "Test Clock", "description": "A special clock for testing time-dependent features. First, you need to create a test clock using the 'Create Test Clock' action. Then, you can use its ID here to filter results for that specific test time. This lets you simulate different dates and times in your test environment. For example, if you want to test what happens when a subscription renews in the future, create a test clock, advance it to that date, and use its ID here. This only works in test mode, not in live mode. Example: clock_123456789"}
                    ],
                    "ui_options": {
                        "ui_order": ["limit", "customer", "status", "subscription", "collection_method", "created[gt]", "created[gte]", "created[lt]", "created[lte]", "starting_after", "ending_before", "test_clock"]
                    }
                }
            }
        ]
    }
]

EVENT_TYPES = {
    "account": {
        "application": {
            "authorized": "Occurs whenever a user authorizes an application",
            "deauthorized": "Occurs whenever a user deauthorizes an application"
        },
        "external_account": {
            "created": "Occurs whenever an external account is created",
            "deleted": "Occurs whenever an external account is deleted",
            "updated": "Occurs whenever an external account is updated"
        },
        "updated": "Occurs whenever an account status or property has changed"
    },
    "application_fee": {
        "created": "Occurs whenever an application fee is created on a charge",
        "refund": {
            "updated": "Occurs whenever an application fee refund is updated"
        },
        "refunded": "Occurs whenever an application fee is refunded"
    },
    "balance": {
        "available": "Occurs whenever your Stripe balance has been updated"
    },
    "billing_portal": {
        "configuration": {
            "created": "Occurs whenever a portal configuration is created",
            "updated": "Occurs whenever a portal configuration is updated"
        },
        "session": {
            "created": "Occurs whenever a portal session is created"
        }
    },
    "billing": {
        "alert": {
            "triggered": "Occurs whenever your custom alert threshold is met"
        },
        "credit_balance_transaction": {
            "created": "Occurs when a credit balance transaction is created"
        },
        "credit_grant": {
            "created": "Occurs when a credit grant is created",
            "updated": "Occurs when a credit grant is updated"
        },
        "meter": {
            "created": "Occurs when a meter is created",
            "deactivated": "Occurs when a meter is deactivated",
            "reactivated": "Occurs when a meter is reactivated",
            "updated": "Occurs when a meter is updated"
        }
    },
    "capability": {
        "updated": "Occurs whenever a capability has new requirements or a new status"
    },
    "cash_balance": {
        "funds_available": "Occurs whenever there is a positive remaining cash balance"
    },
    "charge": {
        "captured": "Occurs whenever a previously uncaptured charge is captured",
        "dispute": {
            "closed": "Occurs when a dispute is closed",
            "created": "Occurs whenever a customer disputes a charge with their bank",
            "funds_reinstated": "Occurs when funds are reinstated to your account after a dispute",
            "funds_withdrawn": "Occurs when funds are removed from your account due to a dispute",
            "updated": "Occurs when the dispute is updated"
        },
        "expired": "Occurs whenever an uncaptured charge expires",
        "failed": "Occurs whenever a failed charge attempt occurs",
        "pending": "Occurs whenever a pending charge is created",
        "refund": {
            "updated": "Occurs whenever a refund is updated on selected payment methods"
        },
        "refunded": "Occurs whenever a charge is refunded",
        "succeeded": "Occurs whenever a charge is successful",
        "updated": "Occurs whenever a charge description or metadata is updated"
    },
    "checkout": {
        "session": {
            "async_payment_failed": "Occurs when a payment intent using a delayed payment method fails",
            "async_payment_succeeded": "Occurs when a payment intent using a delayed payment method succeeds",
            "completed": "Occurs when a Checkout Session has been successfully completed",
            "expired": "Occurs when a Checkout Session is expired"
        }
    },
    "climate": {
        "order": {
            "canceled": "Occurs when a Climate order is canceled",
            "created": "Occurs when a Climate order is created",
            "delayed": "Occurs when a Climate order is delayed",
            "delivered": "Occurs when a Climate order is delivered",
            "product_substituted": "Occurs when a Climate order's product is substituted"
        },
        "product": {
            "created": "Occurs when a Climate product is created",
            "pricing_updated": "Occurs when a Climate product's pricing is updated"
        }
    },
    "customer": {
        "created": "Occurs whenever a new customer is created",
        "deleted": "Occurs whenever a customer is deleted",
        "updated": "Occurs whenever a customer is updated",
        "discount": {
            "created": "Occurs whenever a discount is created for a customer",
            "deleted": "Occurs whenever a discount is removed from a customer",
            "updated": "Occurs whenever a customer's discount is updated"
        },
        "subscription": {
            "created": "Occurs whenever a customer subscribes to a plan",
            "deleted": "Occurs whenever a customer's subscription is canceled",
            "paused": "Occurs whenever a customer's subscription is paused",
            "resumed": "Occurs whenever a customer's subscription is resumed",
            "trial_will_end": "Occurs three days before a subscription's trial period is scheduled to end",
            "updated": "Occurs whenever a subscription is updated"
        },
        "tax_id": {
            "created": "Occurs whenever a tax ID is created for a customer",
            "deleted": "Occurs whenever a tax ID is deleted from a customer",
            "updated": "Occurs whenever a customer's tax ID is updated"
        }
    },
    "invoice": {
        "created": "Occurs whenever a new invoice is created",
        "deleted": "Occurs whenever an invoice is deleted",
        "finalized": "Occurs whenever an invoice is finalized",
        "marked_uncollectible": "Occurs whenever an invoice is marked uncollectible",
        "paid": "Occurs whenever an invoice is paid",
        "payment_action_required": "Occurs whenever an invoice requires payment action",
        "payment_failed": "Occurs whenever an invoice payment attempt fails",
        "payment_succeeded": "Occurs whenever an invoice payment attempt succeeds",
        "sent": "Occurs whenever an invoice is sent",
        "upcoming": "Occurs whenever an upcoming invoice is created",
        "updated": "Occurs whenever an invoice is updated",
        "voided": "Occurs whenever an invoice is voided"
    },
    "payment_intent": {
        "amount_capturable_updated": "Occurs whenever a payment intent's amount_capturable changes",
        "canceled": "Occurs whenever a payment intent is canceled",
        "created": "Occurs whenever a new payment intent is created",
        "partially_funded": "Occurs whenever a payment intent is partially funded",
        "payment_failed": "Occurs whenever a payment intent's payment fails",
        "processing": "Occurs whenever a payment intent is processing",
        "requires_action": "Occurs whenever a payment intent requires action",
        "succeeded": "Occurs whenever a payment intent succeeds"
    },
    "payout": {
        "canceled": "Occurs whenever a payout is canceled",
        "created": "Occurs whenever a new payout is created",
        "failed": "Occurs whenever a payout fails",
        "paid": "Occurs whenever a payout is paid",
        "updated": "Occurs whenever a payout is updated"
    },
    "price": {
        "created": "Occurs whenever a new price is created",
        "deleted": "Occurs whenever a price is deleted",
        "updated": "Occurs whenever a price is updated"
    },
    "product": {
        "created": "Occurs whenever a new product is created",
        "deleted": "Occurs whenever a product is deleted",
        "updated": "Occurs whenever a product is updated"
    },
    "refund": {
        "created": "Occurs whenever a new refund is created",
        "updated": "Occurs whenever a refund is updated"
    },
    "subscription": {
        "created": "Occurs whenever a new subscription is created",
        "deleted": "Occurs whenever a subscription is canceled",
        "paused": "Occurs whenever a subscription is paused",
        "resumed": "Occurs whenever a subscription is resumed",
        "trial_will_end": "Occurs three days before a subscription's trial period is scheduled to end",
        "updated": "Occurs whenever a subscription is updated"
    },
    "tax": {
        "calculation": {
            "created": "Occurs whenever a tax calculation is created",
            "updated": "Occurs whenever a tax calculation is updated"
        },
        "registration": {
            "created": "Occurs whenever a tax registration is created",
            "updated": "Occurs whenever a tax registration is updated"
        },
        "transaction": {
            "created": "Occurs whenever a tax transaction is created",
            "updated": "Occurs whenever a tax transaction is updated"
        }
    },
    "transfer": {
        "created": "Occurs whenever a new transfer is created",
        "failed": "Occurs whenever a transfer fails",
        "paid": "Occurs whenever a transfer is paid",
        "reversed": "Occurs whenever a transfer is reversed",
        "updated": "Occurs whenever a transfer is updated"
    }
}

EVENT_TYPES_OBJ = []

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
for obj in EVENT_TYPES:
    EVENT_TYPES_OBJ.append(obj)

# print("CREATE_OBJECT_TYPE",CREATE_OBJECT_TYPE)
# print("UPDATE_OBJECT_TYPE",UPDATE_OBJECT_TYPE)
# print("GET_OBJECT_TYPE ",GET_OBJECT_TYPE)
# print("LIST_OBJECT_TYPE",LIST_OBJECT_TYPE)
# print("CUSTOME_OBJECT_TYPE",CUSTOME_OBJECT_TYPE)


__all__ = ["OBJECT_TYPE", "CREATE_OBJECT_TYPE", "UPDATE_OBJECT_TYPE", "GET_OBJECT_TYPE", "LIST_OBJECT_TYPE", "CUSTOME_OBJECT_TYPE"]



# print(EVENT_TYPES_OBJ)

# Simple list of all possible event types
EVENT_TYPES_LIST = [
    # Account Events
    "Default",
    "account.application.authorized",
    "account.application.deauthorized",
    "account.external_account.created",
    "account.external_account.deleted",
    "account.external_account.updated",
    "account.updated",
    
    # Application Fee Events
    "application_fee.created",
    "application_fee.refund.updated",
    "application_fee.refunded",
    
    # Balance Events
    "balance.available",
    
    # Billing Portal Events
    "billing_portal.configuration.created",
    "billing_portal.configuration.updated",
    "billing_portal.session.created",
    
    # Billing Events
    "billing.alert.triggered",
    "billing.credit_balance_transaction.created",
    "billing.credit_grant.created",
    "billing.credit_grant.updated",
    "billing.meter.created",
    "billing.meter.deactivated",
    "billing.meter.reactivated",
    "billing.meter.updated",
    
    # Capability Events
    "capability.updated",
    
    # Cash Balance Events
    "cash_balance.funds_available",
    
    # Charge Events
    "charge.captured",
    "charge.dispute.closed",
    "charge.dispute.created",
    "charge.dispute.funds_reinstated",
    "charge.dispute.funds_withdrawn",
    "charge.dispute.updated",
    "charge.expired",
    "charge.failed",
    "charge.pending",
    "charge.refund.updated",
    "charge.refunded",
    "charge.succeeded",
    "charge.updated",
    
    # Checkout Events
    "checkout.session.async_payment_failed",
    "checkout.session.async_payment_succeeded",
    "checkout.session.completed",
    "checkout.session.expired",
    
    # Climate Events
    "climate.order.canceled",
    "climate.order.created",
    "climate.order.delayed",
    "climate.order.delivered",
    "climate.order.product_substituted",
    "climate.product.created",
    "climate.product.pricing_updated",
    
    # Customer Events
    "customer.created",
    "customer.deleted",
    "customer.updated",
    "customer.discount.created",
    "customer.discount.deleted",
    "customer.discount.updated",
    "customer.subscription.created",
    "customer.subscription.deleted",
    "customer.subscription.paused",
    "customer.subscription.resumed",
    "customer.subscription.trial_will_end",
    "customer.subscription.updated",
    "customer.tax_id.created",
    "customer.tax_id.deleted",
    "customer.tax_id.updated",
    
    # Invoice Events
    "invoice.created",
    "invoice.deleted",
    "invoice.finalized",
    "invoice.marked_uncollectible",
    "invoice.paid",
    "invoice.payment_action_required",
    "invoice.payment_failed",
    "invoice.payment_succeeded",
    "invoice.sent",
    "invoice.upcoming",
    "invoice.updated",
    "invoice.voided",
    
    # Payment Intent Events
    "payment_intent.amount_capturable_updated",
    "payment_intent.canceled",
    "payment_intent.created",
    "payment_intent.partially_funded",
    "payment_intent.payment_failed",
    "payment_intent.processing",
    "payment_intent.requires_action",
    "payment_intent.succeeded",
    
    # Payout Events
    "payout.canceled",
    "payout.created",
    "payout.failed",
    "payout.paid",
    "payout.updated",
    
    # Price Events
    "price.created",
    "price.deleted",
    "price.updated",
    
    # Product Events
    "product.created",
    "product.deleted",
    "product.updated",
    
    # Refund Events
    "refund.created",
    "refund.updated",
    
    # Subscription Events
    "subscription.created",
    "subscription.deleted",
    "subscription.paused",
    "subscription.resumed",
    "subscription.trial_will_end",
    "subscription.updated",
    
    # Tax Events
    "tax.calculation.created",
    "tax.calculation.updated",
    "tax.registration.created",
    "tax.registration.updated",
    "tax.transaction.created",
    "tax.transaction.updated",
    
    # Transfer Events
    "transfer.created",
    "transfer.failed",
    "transfer.paid",
    "transfer.reversed",
    "transfer.updated"
]

# Update EVENT_TYPES_OBJ to use the flat list
EVENT_TYPES_OBJ = EVENT_TYPES_LIST








