import json
import os
import logging
from typing import Dict, Any, List

from flask import request as flask_request
from workflows_cdk import Response, Request, ManagedError
from main import router
from src.utils.dictionary.company_enrichment_fields import company_enrich_return_fields_formatted
from src.utils.dictionary.person_enrichment_fields import person_enrich_return_fields_formatted
from .client import EnrichmentClient
from src.utils.content_handler import handle_content_request


@router.route("/content", methods=["POST"])
def content():
    """
    Provide dynamic content for the module UI.
    Fetches available identifier types based on the selected object type.
    """
    # Parse the request
    request = Request(flask_request)


    # Parse the request
    request = Request(flask_request)
    data = request.data

    if not data:
        return Response(data={"message": "Missing request data"}, status_code=400)
        
    form_data = data.get("form_data", {})

    content_object_names = data.get("content_object_names", [])
    
    # Extract content object names from objects if needed
    if isinstance(content_object_names, list) and content_object_names and isinstance(content_object_names[0], dict):
        content_object_names = [obj.get("id") for obj in content_object_names if "id" in obj]
  
    object_type = form_data.get("object_type")
    content_objects = []
    for content_name in content_object_names:
        # Object types (Contact, Lead, etc.)
        if content_name == "identifier_types":
            content_object = [
                    {"value": "person", "label": "Person"},
                    {"value": "company", "label": "Company"}
                ]
            result = {
                    "content_object_name": "identifier_types",
                    "data": content_object
                }
            content_objects.append(result)
            if object_type == "company":
                content_object = [
                    {"value": "company_domain", "label": "Company Domain"},
                    {"value": "company_name", "label": "Company Name"},
                    {"value": "company_linkedin_url", "label": "Company LinkedIn URL"},
                    {"value": "company_id", "label": "Company ID"}
                ]
                result = {
                    "content_object_name": "identifier_types",
                    "data": content_object
                }
                content_objects.append(result)
            elif object_type == "person":
                
                content_object = [
                    {"value": "linkedin_profile_url", "label": "LinkedIn Profile URL"},
                    {"value": "business_email", "label": "Business Email"}
                ]
                result = {
                    "content_object_name": "identifier_types",
                    "data": content_object
                }
                content_objects.append(result)

        elif content_name == "return_fields":
            if object_type == "company":
                content_object = company_enrich_return_fields_formatted
            elif object_type == "person":
                content_object = person_enrich_return_fields_formatted
            result = {
                "content_object_name": "return_fields",
                "data": content_object
            }
            content_objects.append(result)

    return Response(data={"content_objects": content_objects})

@router.route("/execute", methods=["POST"])
def execute():
    """
    Execute an enrichment request for Companies or People.
    """
    try:
        # Parse the request
        request = Request(flask_request)
        data = request.data
    
        # Validate required parameters
        if not data:
            raise ManagedError("Missing request parameters")
        
        # Get the parameters
        object_type = data.get("object_type", "company").lower()
        identifier_type = data.get("identifier_type", "company_domain")
        fields_data = data.get("fields", [])
        identifier_values = data.get("identifier_values", [])
        enrich_realtime = data.get("enrich_realtime", False)
        
        # Validate fields - ensure it's a list of strings
        if not isinstance(fields_data, list):
            raise ManagedError("Fields must be a list")
        if not all(isinstance(f, str) for f in fields_data):
            raise ManagedError("All items in fields must be strings")
        field_list = fields_data
        
        # Validate identifiers - ensure it's a list of strings
        if not isinstance(identifier_values, list):
            raise ManagedError("Identifier values must be a list")
        if not all(isinstance(val, str) for val in identifier_values):
             raise ManagedError("All identifier values must be strings")

        identifiers = [val.strip() for val in identifier_values if val.strip()]

        # Limit to 25 identifiers
        if len(identifiers) > 25:
            identifiers = identifiers[:25]
        
        if not identifiers:
            raise ManagedError("No valid identifiers provided")
            
        # Get API key from environment or request
        api_key = os.environ.get("CRUSTDATA_API_KEY")
        
        # Initialize client
        client = EnrichmentClient(api_key) if api_key else None
        
        if not client:
            raise ManagedError("API key not provided")
            

        # Create kwargs for API call based on object type and identifier type
        kwargs = {
            "fields": field_list,
            "realtime": enrich_realtime
        }
        
        if object_type == "company":
            # Map identifiers to the correct parameter for companies
            if identifier_type == "company_name":
                kwargs["company_names"] = identifiers
            elif identifier_type == "company_domain":
                kwargs["company_domains"] = identifiers
            elif identifier_type == "company_linkedin_url":
                kwargs["company_linkedin_urls"] = identifiers
            elif identifier_type == "company_id":
                kwargs["company_ids"] = identifiers
            else:
                raise ManagedError(f"Invalid identifier type for company: {identifier_type}")
            
            # Make the API call
            response = client.enrich_companies(**kwargs)
            
            # Format company response for better display
            return Response(
                data=response,
                metadata={
                    "source": "api",
                    "object_type": object_type,
                    "identifier_type": identifier_type
                }
            )
        elif object_type == "person":
            # Map identifiers to the correct parameter for persons
            if identifier_type == "linkedin_profile_url":
                kwargs["linkedin_profile_urls"] = identifiers
            elif identifier_type == "business_email":
                kwargs["business_emails"] = identifiers
            else:
                raise ManagedError(f"Invalid identifier type for person: {identifier_type}")
            
            # Make the API call
            response = client.enrich_persons(**kwargs)
            
            # Return person response directly
            return Response(
                data=response,
                metadata={
                    "source": "api",
                    "object_type": object_type,
                    "identifier_type": identifier_type
                }
            )
        else:
            raise ManagedError(f"Unsupported object type: {object_type}")
            
    except ManagedError as e:
        return Response.error(str(e))
    except Exception as e:
        return Response.error(f"Unexpected error: {str(e)}")

def format_company_response(response, kwargs, identifier_type, object_type):
    """Helper function to format company response data for better display"""
    import json # Ensure json is imported
    # Extract company name from LinkedIn URL if possible
    company_name = None
    if kwargs.get("company_linkedin_urls"):
        url = kwargs["company_linkedin_urls"][0]
        if "/company/" in url:
            company_slug = url.split("/company/")[1].split("/")[0]
            company_name = company_slug.replace("-", " ").title()
    
    # Format the response for better display
    formatted_response = {}
    
    # If response is a list, use the first item
    if isinstance(response, list) and response:
        response = response[0]
    
    # Check if we have companies in the response
    companies = response.get("companies", [])
    if companies and len(companies) > 0:
        # Use the first company
        formatted_response = companies[0]
    else:
        # Check for news articles
        news_articles = response.get("news_articles", [])
        if news_articles and len(news_articles) > 0:
            # Get company ID from first article if available
            company_id = news_articles[0].get("company_id") if news_articles else None
            
            # Create a simplified company record with news
            formatted_response = {
                "company_id": company_id,
                "company_name": company_name or "Unknown Company",
                "linkedin_url": kwargs.get("company_linkedin_urls", [""])[0],
                "news_count": len(news_articles),
                "recent_news": news_articles[:5] if news_articles else []
            }
        else:
            # See if there's any data we can extract from the response
            if isinstance(response, dict):
                formatted_response = {
                    "company_name": company_name or "Unknown Company",
                    "linkedin_url": kwargs.get("company_linkedin_urls", [""])[0]
                }
                
                # Add a few key fields from the response if they exist
                for key in ["company_id", "description", "headquarters", "year_founded", "company_website"]:
                    if key in response:
                        formatted_response[key] = response[key]
    
    return Response(
        data=formatted_response,
        metadata={
            "source": "api",
            "object_type": object_type,
            "identifier_type": identifier_type
        }
    ) 



base_schema = {
  "metadata": {
    "workflows_module_schema_version": "1.0.0",
    "version": "1.0.0"
  },
  "fields": [
    {
      "type": "string",
      "id": "object_type",
      "label": "Object Type",
      "description": "Type of record to enrich",
      "ui_options": {
        "ui_widget": "SelectWidget"
      },
          "content": {
        "type": ["managed"],
        "content_objects": [{ "id": "identifier_types" }]
      },
      "on_action":{
        "load_schema":True
      },
      "choices": {
        "values": [
          { "value": "company", "label": "Company" },
          { "value": "person", "label": "Person" }
        ]
      }
    }
   
  ],
  "ui_options": {
    "ui_order": [
      "object_type",
      "identifier_type",
      "identifiers_text",
      "fields",
      "enrich_realtime"
    ]
  }

}


company_schema = {
  "metadata": {
    "workflows_module_schema_version": "1.0.0",
    "version": "1.0.0"
  },
  "fields": [
    {
      "type": "string",
      "id": "object_type",
      "label": "Object Type",
      "description": "Type of record to enrich",
      "ui_options": {
        "ui_widget": "SelectWidget"
      },
      "content": {
        "type": ["managed"],
        "content_objects": [{ "id": "identifier_types" }]
      },
      "on_action":{
        "load_schema":True
      },
      "choices": {
        "values": [
          { "value": "company", "label": "Company" },
          { "value": "person", "label": "Person" }
        ]
      }
    },
    {
        "type": "string",
        "id":"company_name",
        "label": "Company Name",
        "description": "Name of the company to enrich"
    },
    {
        "type": "string",
        "id":"company_domain",
        "label": "Company Domain",
        "description": "Domain of the company to enrich"
    }
   
  ],
  "ui_options": {
    "ui_order": [
      "object_type",
      "company_name",
      "company_domain",
      "fields",
      "enrich_realtime"
    ]
  }

}


person_schema = {
  "metadata": {
    "workflows_module_schema_version": "1.0.0",
    "version": "1.0.0"
  },
  "fields": [
    {
      "type": "string",
      "id": "object_type",
      "label": "Object Type",
      "description": "Type of record to enrich",
      "ui_options": {
        "ui_widget": "SelectWidget"
      },
          "content": {
        "type": ["managed"],
        "content_objects": [{ "id": "identifier_types" }]
      },
      "on_action":{
        "load_schema":True
      },
      "choices": {
        "values": [
          { "value": "company", "label": "Company" },
          { "value": "person", "label": "Person" }
        ]
      }
    },
    {
        "type": "string",
        "id":"person_name",
        "label": "Person Name",
        "description": "Name of the person to enrich"
    },
    {
        "type": "string",
        "id":"person_email",
        "label": "Person Email",
        "description": "Email of the person to enrich"
    }
   
  ],
  "ui_options": {
    "ui_order": [
      "object_type",
      "company_name",
      "company_domain",
      "fields",
      "enrich_realtime"
    ]
  }

}

@router.route("/schema", methods=["POST"])
def schema():
    """
    Provide the schema for the module.
    """
    print("schema")
    request = Request(flask_request)
    data = request.data
    print(request.json)
    form_data = data.get("form_data", {})
    if not data:
        raise ManagedError("Missing request data")
    
    object_type = form_data.get("object_type")
    print(object_type)
    if not object_type:
        return Response(data={"schema": base_schema})
    
    if object_type == "company":
        return Response(data={"schema": company_schema})

    if object_type == "person":
        return Response(data={"schema": person_schema})

    
    return Response(data={"schema": base_schema})


{
    "choices": {
        "values": [
            {
                "value": field["value"] if isinstance(field, dict) else field,
                "label": field["label"] if isinstance(field, dict) else field.title()
                                    } for field in (create_action.get("required_fields", []) + 
                                                  create_action.get("optional_fields", []))
                                ]
                            }}