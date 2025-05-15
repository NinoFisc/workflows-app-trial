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
                        {"value": "name", "label": "Name"},
                        {"value": "email", "label": "Email"},
                        {"value": "phone", "label": "Phone"},
                        {"value": "description", "label": "Description"},
                        
                        # Address Information
                        {"value": "address", "label": "Address"},
                        {"value": "address.line1", "label": "Address Line 1"},
                        {"value": "address.line2", "label": "Address Line 2"},
                        {"value": "address.city", "label": "City"},
                        {"value": "address.state", "label": "State"},
                        {"value": "address.postal_code", "label": "Postal Code"},
                        {"value": "address.country", "label": "Country"},
                        
                        # Invoice Settings
                        {"value": "invoice_settings", "label": "Invoice Settings"},
                        {"value": "invoice_settings.custom_fields", "label": "Custom Fields"},
                        {"value": "invoice_settings.default_payment_method", "label": "Default Payment Method"},
                        {"value": "invoice_settings.footer", "label": "Invoice Footer"},
                        {"value": "invoice_settings.rendering_options", "label": "Rendering Options"},
                        
                        # Additional Information
                        {"value": "metadata", "label": "Metadata"},
                        {"value": "currency", "label": "Currency"},
                        {"value": "balance", "label": "Balance"},
                        
                        # Shipping Information
                        {"value": "shipping", "label": "Shipping"},
                        {"value": "shipping.name", "label": "Shipping Name"},
                        {"value": "shipping.phone", "label": "Shipping Phone"},
                        {"value": "shipping.address", "label": "Shipping Address"},
                        
                        # Tax Information
                        {"value": "tax_exempt", "label": "Tax Exempt"},
                        
                        # Localization
                        {"value": "preferred_locales", "label": "Preferred Locales"}
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
                        {"value": "name", "label": "Name"},
                        {"value": "email", "label": "Email"},
                        {"value": "phone", "label": "Phone"},
                        {"value": "description", "label": "Description"},
                        
                        # Address Information
                        {"value": "address", "label": "Address"},
                        {"value": "address.line1", "label": "Address Line 1"},
                        {"value": "address.line2", "label": "Address Line 2"},
                        {"value": "address.city", "label": "City"},
                        {"value": "address.state", "label": "State"},
                        {"value": "address.postal_code", "label": "Postal Code"},
                        {"value": "address.country", "label": "Country"},
                        
                        # Invoice Settings
                        {"value": "invoice_settings", "label": "Invoice Settings"},
                        {"value": "invoice_settings.custom_fields", "label": "Custom Fields"},
                        {"value": "invoice_settings.default_payment_method", "label": "Default Payment Method"},
                        {"value": "invoice_settings.footer", "label": "Invoice Footer"},
                        {"value": "invoice_settings.rendering_options", "label": "Rendering Options"},
                        {"value": "invoice_prefix", "label": "Invoice Prefix"},
                        
                        # Payment Information
                        {"value": "default_source", "label": "Default Payment Source"},
                        {"value": "source", "label": "Payment Source"},
                        
                        # Balance Information
                        {"value": "balance", "label": "Balance"},
                        {"value": "cash_balance", "label": "Cash Balance"},
                        
                        # Additional Information
                        {"value": "metadata", "label": "Metadata"},
                        {"value": "next_invoice_sequence", "label": "Next Invoice Sequence"},
                        
                        # Shipping Information
                        {"value": "shipping", "label": "Shipping"},
                        {"value": "shipping.name", "label": "Shipping Name"},
                        {"value": "shipping.phone", "label": "Shipping Phone"},
                        {"value": "shipping.address", "label": "Shipping Address"},
                        
                        # Tax Information
                        {"value": "tax", "label": "Tax Information"},
                        {"value": "tax_exempt", "label": "Tax Exempt Status"},
                        
                        # Localization
                        {"value": "preferred_locales", "label": "Preferred Locales"}
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
                        {"value": "currency", "label": "Currency"},
                        {"value": "customer", "label": "Customer ID"},
                        {"value": "source", "label": "Source"}
                    ],
                    "optional_fields": [
                        # Basic Information
                        {"value": "description", "label": "Description"},
                        {"value": "metadata", "label": "Metadata"},
                        {"value": "receipt_email", "label": "Receipt Email"},
                        {"value": "receipt_number", "label": "Receipt Number"},
                        {"value": "statement_descriptor", "label": "Statement Descriptor"},
                        {"value": "statement_descriptor_suffix", "label": "Statement Descriptor Suffix"},
                        
                        # Billing Details
                        {"value": "billing_details", "label": "Billing Details"},
                        {"value": "billing_details.address", "label": "Billing Address"},
                        {"value": "billing_details.address.city", "label": "Billing City"},
                        {"value": "billing_details.address.country", "label": "Billing Country"},
                        {"value": "billing_details.address.line1", "label": "Billing Address Line 1"},
                        {"value": "billing_details.address.line2", "label": "Billing Address Line 2"},
                        {"value": "billing_details.address.postal_code", "label": "Billing Postal Code"},
                        {"value": "billing_details.address.state", "label": "Billing State"},
                        {"value": "billing_details.email", "label": "Billing Email"},
                        {"value": "billing_details.name", "label": "Billing Name"},
                        {"value": "billing_details.phone", "label": "Billing Phone"},
                        
                        # Shipping Information
                        {"value": "shipping", "label": "Shipping"},
                        {"value": "shipping.address", "label": "Shipping Address"},
                        {"value": "shipping.name", "label": "Shipping Name"},
                        {"value": "shipping.phone", "label": "Shipping Phone"},
                        
                        # Payment Information
                        {"value": "capture", "label": "Capture"},
                        {"value": "application_fee_amount", "label": "Application Fee Amount"},
                        {"value": "on_behalf_of", "label": "On Behalf Of"},
                        {"value": "transfer_data", "label": "Transfer Data"},
                        {"value": "transfer_group", "label": "Transfer Group"},
                        
                        # Additional Settings
                        {"value": "fraud_details", "label": "Fraud Details"},
                        {"value": "receipt_url", "label": "Receipt URL"},
                        {"value": "review", "label": "Review"},
                        {"value": "source_transfer", "label": "Source Transfer"},
                        {"value": "transfer", "label": "Transfer"}
                    ]
                }
            }
        ]
    }
]

__all__ = ["OBJECT_TYPE"]













