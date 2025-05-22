from flask import request as flask_request
from workflows_cdk import Response, Request
from main import router
import stripe
from dict import *

module = "create"

@router.route("/content", methods=["POST"])
def content():
    request = Request(flask_request)
    data = request.data
    
    form_data = data.get("form_data")
    
    object_type = form_data.get("object_type")
    

    print("---------------------")

    print(str(object_type))
    print("---------------------")

    options = []
    
    index = 0
    
    for obj in OBJECT_TYPE:
        if obj.get("object_type")==object_type:
            index = OBJECT_TYPE.index(obj)

    object_type_actions = OBJECT_TYPE[index].get("action")

    for action in object_type_actions:
        for action_key, action_value in action.items():
            if action_key == module:
                required_fields = action_value.get("required_fields")
                optional_fields = action_value.get("optional_fields")

    options = required_fields + optional_fields

        
            

    # Return the options
    return Response(data={
        "content_objects": [{
            "content_object_name": "fields",
            "data": options
        }]
    })

@router.route("/execute", methods=["POST", "GET"])
def execute():
    request = Request(flask_request)
    data = request.data
    
    object_type = data.get("object_type")
    print("---------")
    print(object_type)
    print("---------")

    fields = data.get("fields")

    print("---------------")
    print(fields)
    print("---------------")


    api_key = data.get("api_key")

    print("---------------")
    print(api_key)
    print("---------------")

    stripe.api_key = api_key
    
    

    field_value = {}

    for field in fields:
        name = field.get("field_name")
        value = field.get("field_value")
        field_value[name]= value

    if object_type == "customer":
    
        customer = stripe.Customer.create(**field_value)
        return Response(data=customer)


    if object_type == "charge":
        charge = stripe.Charge.create(**field_value)
        return Response(data=charge)

    return Response(data="") 




base_schema = {
  "metadata": {
    "workflows_module_schema_version": "1.0.0"
  },
  "fields": [
    {
      "type": "string",
      "id": "api_key",
      "label": "API Key"
    },
    {
      "type": "string",
      "id": "object_type",
      "label": "Select Object Type",
      "ui_options": {
        "ui_widget": "SelectWidget"
      },
      "on_action":{
          "load_schema":True
      },
      "choices": {
        "values": [
          {
            "value": obj_type,
            "label": obj_type.title()  # This will capitalize the first letter
          } for obj_type in CREATE_OBJECT_TYPE
        ]
      },
      "validation": {
        "required": True
      }
    }
  ]
}


base_schema = {
  "metadata": {
    "workflows_module_schema_version": "1.0.0"
  },
  "fields": [
    {
      "type": "string",
      "id": "api_key",
      "label": "API Key",
      "validation": {
        "required": True
      }
    },
    {
      "type": "string",
      "id": "object_type",
      "label": "Select Object Type",
      "ui_options": {
        "ui_widget": "SelectWidget"
      },
      "on_action":{
          "load_schema":True
      },
      "choices": {
        "values": [
          {
            "value": obj_type,
            "label": obj_type.title()  # This will capitalize the first letter
          } for obj_type in CREATE_OBJECT_TYPE
        ]
      },
      "validation": {
        "required": True
      }
    }
  ]
}

object_type_schema = {
    "metadata": {
        "workflows_module_schema_version": "1.0.0"
    },
    "fields": [
        {
            "type": "string",
            "id": "api_key",
            "label": "API Key",
            "validation": {
                "required": True
            }
        },
        {
            "type": "string",
            "id": "object_type",
            "label": "Select Object Type",
            "ui_options": {
                "ui_widget": "SelectWidget"
            },
            "on_action": {
                "load_schema": True
            },
            "choices": {
                "values": [
                    {
                        "value": obj_type,
                        "label": obj_type.title()
                    } for obj_type in CREATE_OBJECT_TYPE
                ]
            },
            "validation": {
                "required": True
            }
        },
        {
            "type": "array",
            "id": "field_inputs",
            "label": "Field Values",
            "items": {
                "type": "object",
                "fields": [
                    {
                        "type": "string",
                        "id": "field_name",
                        "label": "Field Name",
                        "ui_options": {
                            "ui_widget": "SelectWidget"
                        },
                        "content": {
                            "type": ["managed"],
                            "content_objects": [{
                                "id": "fields"
                            }]
                        },
                        "validation": {
                            "required": True
                        }
                    },
                    {
                        "type": "string",
                        "id": "field_value",
                        "label": "Field Value",
                        "validation": {
                            "required": True
                        }
                    }
                ], 
                "ui_options": {
                "ui_layout": {
                    "type": "horizontal",
                    "elements": ["field_name", "field_value"]
                }
            },
            },
            
            "validation": {
                "min_items": 1,
                "message": "At least one field is required"
            }
        }
    ],
    "ui_options": {
        "ui_order": [
            "api_key",
            "object_type",
            "field_inputs"
        ]
    }
}

@router.route("/schema", methods=["POST"])
def schema():
    request = Request(flask_request)
    data = request.data
    print("Data:", data, "\n -------------")

    form_data = data.get("form_data")
    print("Form data:", form_data, "\n------------")

    object_type = form_data.get("object_type")
    if not object_type:
        return Response(data={"schema": base_schema})

    print("object_type:", object_type)
    
    # Return object_type_schema for all object types
    return Response(data={"schema": object_type_schema})

    




    