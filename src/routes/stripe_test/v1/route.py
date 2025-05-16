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


@router.route("/schema", methods=["POST"])
def schema(): 
    return Response(data={"schema": base_schema})
    