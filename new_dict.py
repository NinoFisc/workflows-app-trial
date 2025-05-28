OBJECTS = {
    "customer": {
        "object_type": "customer",
        "fields": {
            # Basic Information
            "name": {
                "label": "Full Name or Business Name",
                "type": "string",
                "validation": {
                    "required": False
                }
            },
            "email": {
                "label": "Email Address",
                "type": "string",
                "validation": {
                    "required": False,
                    "max_length": 512
                }
            },
            "phone": {
                "label": "Phone Number",
                "type": "string",
                "validation": {
                    "required": False
                }
            },
            "description": {
                "label": "Description",
                "type": "string",
                "validation": {
                    "required": False
                }
            },
            "metadata": {
                "label": "Additional Metadata",
                "type": "string",
                "ui_options": {
                    "ui_widget": "CodeblockWidget",
                    "ui_options": {
                        "language": "json"
                    }
                },
                "validation": {
                    "required": False
                }
            },

            # Address Information
            "address": {
                "label": "Customer Address",
                "type": "object",
                "fields": {
                    "line1": {
                        "label": "Address Line 1",
                        "type": "string"
                    },
                    "line2": {
                        "label": "Address Line 2",
                        "type": "string"
                    },
                    "city": {
                        "label": "City",
                        "type": "string"
                    },
                    "state": {
                        "label": "State/Province",
                        "type": "string"
                    },
                    "postal_code": {
                        "label": "Postal Code",
                        "type": "string"
                    },
                    "country": {
                        "label": "Country",
                        "type": "string",
                        "ui_options": {
                            "ui_widget": "SelectWidget"
                        },
                        "choices": {
                            "values": [
                                {"value": code} for code in ["US", "CA", "GB", "FR", "DE", "IT", "ES", "JP", "AU"]
                            ]
                        }
                    }
                }
            },

            # Shipping Information
            "shipping": {
                "label": "Shipping Information",
                "type": "object",
                "fields": {
                    "name": {
                        "label": "Recipient Name",
                        "type": "string"
                    },
                    "phone": {
                        "label": "Phone Number",
                        "type": "string"
                    },
                    "address": {
                        "label": "Shipping Address",
                        "type": "object",
                        "fields": {
                            "line1": {
                                "label": "Address Line 1",
                                "type": "string"
                            },
                            "line2": {
                                "label": "Address Line 2",
                                "type": "string"
                            },
                            "city": {
                                "label": "City",
                                "type": "string"
                            },
                            "state": {
                                "label": "State/Province",
                                "type": "string"
                            },
                            "postal_code": {
                                "label": "Postal Code",
                                "type": "string"
                            },
                            "country": {
                                "label": "Country",
                                "type": "string",
                                "ui_options": {
                                    "ui_widget": "SelectWidget"
                                },
                                "choices": {
                                    "values": [
                                        {"value": code} for code in ["US", "CA", "GB", "FR", "DE", "IT", "ES", "JP", "AU"]
                                    ]
                                }
                            }
                        }
                    }
                }
            },

            # Tax Information
            "tax": {
                "label": "Tax Information",
                "type": "object",
                "fields": {
                    "ip_address": {
                        "label": "IP Address for Tax Calculation",
                        "type": "string"
                    },
                    "validate_location": {
                        "label": "Validate Location",
                        "type": "boolean"
                    }
                }
            },
            "tax_exempt": {
                "label": "Tax Exempt Status",
                "type": "string",
                "ui_options": {
                    "ui_widget": "SelectWidget"
                },
                "choices": {
                    "values": [
                        {"value": "none"},
                        {"value": "exempt"},
                        {"value": "reverse"}
                    ]
                }
            },

            # Payment Information
            "payment_method": {
                "label": "Payment Method ID",
                "type": "string"
            },
            "source": {
                "label": "Source ID (Card or Bank Account)",
                "type": "string"
            },

            # Balance Information
            "balance": {
                "label": "Balance (in cents)",
                "type": "number"
            },
            "cash_balance": {
                "label": "Cash Balance",
                "type": "object",
                "fields": {
                    "amount": {
                        "label": "Amount",
                        "type": "number"
                    },
                    "currency": {
                        "label": "Currency",
                        "type": "string",
                        "ui_options": {
                            "ui_widget": "SelectWidget"
                        },
                        "choices": {
                            "values": [
                                {"value": "usd"},
                                {"value": "eur"},
                                {"value": "gbp"}
                            ]
                        }
                    }
                }
            },

            # Invoice Settings
            "invoice_prefix": {
                "label": "Invoice Prefix",
                "type": "string"
            },
            "invoice_settings": {
                "label": "Invoice Settings",
                "type": "object",
                "fields": {
                    "custom_fields": {
                        "label": "Custom Fields",
                        "type": "array",
                        "items": {
                            "type": "object",
                            "fields": {
                                "name": {
                                    "label": "Field Name",
                                    "type": "string"
                                },
                                "value": {
                                    "label": "Field Value",
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "default_payment_method": {
                        "label": "Default Payment Method ID",
                        "type": "string"
                    },
                    "footer": {
                        "label": "Invoice Footer",
                        "type": "string"
                    }
                }
            },

            # Additional Settings
            "preferred_locales": {
                "label": "Preferred Languages",
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "test_clock": {
                "label": "Test Clock ID",
                "type": "string"
            }
        },
        "action": [
            {
                "create": {
                    "required_fields": [],  # No required fields for basic customer creation
                    "optional_fields": ["name", "email", "phone", "description", "metadata", "address", 
                                      "shipping", "tax", "tax_exempt", "payment_method", "source", 
                                      "balance", "cash_balance", "invoice_prefix", "invoice_settings", 
                                      "preferred_locales", "test_clock"]
                }
            }
        ]
    }
}