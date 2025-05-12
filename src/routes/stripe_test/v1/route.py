from flask import request as flask_request
from workflows_cdk import Response, Request
from main import router



@router.route("/content", methods=["POST"])
def content():
    
    

    request = Request(flask_request)
    data = request.data
    
    
    
    # Get the current category selection
    category = data.get("form_data", {}).get("category", "fruits")
    
    
    
    # Define options based on category
    if category == "fruits":
        options = [
            {"value": "apple", "label": "Apple"},
            {"value": "banana", "label": "Banana"}
        ]
    else:
        options = [
            {"value": "carrot", "label": "Carrot"},
            {"value": "broccoli", "label": "Broccoli"}
        ]
    

    
    # Return the options
    return Response(data={
        "content_objects": [{
            "content_object_name": "subcategories",
            "data": options
        }]
    })

