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
                        {"id": "limit", "label": "Limit"}
                    ],
                    "optional_fields": [
                        # Pagination
                        {"id": "starting_after", "label": "Starting After"},
                        {"id": "ending_before", "label": "Ending Before"},
                        
                        # Date Filters
                        {"id": "created", "label": "Filter by creation date"},
                        {"id": "created[gt]", "label": "Created After"},
                        {"id": "created[gte]", "label": "Created On or After"},
                        {"id": "created[lt]", "label": "Created Before"},
                        {"id": "created[lte]", "label": "Created On or Before"},
                        
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
                        {"id": "limit", "label": "Limit"}
                    ],
                    "optional_fields": [
                        # Pagination
                        {"id": "starting_after", "label": "Starting After"},
                        {"id": "ending_before", "label": "Ending Before"},
                        
                        # Date Filters
                        {"id": "created", "label": "Filter by creation date"},
                        {"id": "created[gt]", "label": "Created After"},
                        {"id": "created[gte]", "label": "Created On or After"},
                        {"id": "created[lt]", "label": "Created Before"},
                        {"id": "created[lte]", "label": "Created On or Before"},
                        
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
                        {"id": "limit", "label": "Limit"}
                    ],
                    "optional_fields": [
                        # Pagination
                        {"id": "starting_after", "label": "Cursor for pagination (start after)"},
                        {"id": "ending_before", "label": "Cursor for pagination (end before)"},
                        
                        # Date Filters
                        {"id": "created", "label": "Filter by creation date"},
                        {"id": "created[gt]", "label": "Created after timestamp"},
                        {"id": "created[gte]", "label": "Created on or after timestamp"},
                        {"id": "created[lt]", "label": "Created before timestamp"},
                        {"id": "created[lte]", "label": "Created on or before timestamp"},
                        
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
                        {"id": "balance_transaction", "label": "Balance Transaction ID"}
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
                        {"id": "starting_after", "label": "Cursor for pagination (start after)"},
                        {"id": "ending_before", "label": "Cursor for pagination (end before)"},
                        
                        # Filters
                        {"id": "payout", "label": "Filter by payout ID"},
                        {"id": "type", "label": "Filter by transaction type (e.g., charge, refund, transfer)"},
                        {"id": "currency", "label": "Filter by currency code"},
                        {"id": "source", "label": "Filter by source object ID"},
                        
                        # Date Filters
                        {"id": "created", "label": "Filter by creation date"},
                        {"id": "created[gt]", "label": "Created after timestamp"},
                        {"id": "created[gte]", "label": "Created on or after timestamp"},
                        {"id": "created[lt]", "label": "Created before timestamp"},
                        {"id": "created[lte]", "label": "Created on or before timestamp"},
                        
                        # Additional Options
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












