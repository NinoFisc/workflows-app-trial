import json
from typing import Dict, Any, List

from flask import request as flask_request
from workflows_cdk import Response, Request, ManagedError
from main import router


@router.route("/content", methods=["POST"])
def content():
    """
    Provide dynamic content for the module UI.
    With the new schema, this supplies content for the "single_input" field.
    """
    try:
        # Parse the request
        req = Request(flask_request)
        data = req.data

        if not data:
            return Response(data={"message": "Missing request data"}, status_code=400)
        
        # Get list of content objects requested
        content_object_names = data.get("content_object_names", [])
        content_objects = []
        
    
        
        return Response(data={"content_objects": content_objects})
        
    except Exception as e:
        return Response.error(str(e))


@router.route("/execute", methods=["POST"])
def execute():
    """
    Execute the operation using a single input field defined by the schema.
    """
    try:
        # Parse the request
        req = Request(flask_request)
        data = req.data

        if not data:
            raise ManagedError("Missing request parameters")
        
        # Validate that the single input is provided
        single_input = data.get("single_input")
        if not single_input:
            raise ManagedError("The 'single_input' field is required.")
        
        # Process the single input - this example echoes back the input
        result = {
            "single_input": single_input,
            "processed": True
        }
        
        return Response(
            data=result,
            metadata={"message": "Successfully processed the input"}
        )
        
    except ManagedError as e:
        return Response.error(str(e))
    except Exception as e:
        return Response.error(str(e))