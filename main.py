from src.utils import decode_jwt_to_json, create_register_values_from_jwt
from tabulate import tabulate

with open("jwts/huawei.jwt", "r") as file:
    jwt_token = file.read().strip()

    header, payload = decode_jwt_to_json(jwt_token)
    model_name = header.get('model', '').capitalize()

    # Create RegisterValue objects
    register_values = create_register_values_from_jwt(header, payload)

    # Prepare table data
    table_data = []
    for register_value, value in register_values:
        unit = register_value.unit if register_value.unit != "N/A" else ""
        table_data.append([
            register_value.address,
            register_value.name,
            f"{value} {unit}".strip(),
            register_value.description[0:20]
        ])

    # Sort by register address
    table_data.sort(key=lambda x: x[0])
    
    # Print the table
    print(f"\n{model_name} Inverter Register Values:")
    print(tabulate(
        table_data,
        headers=["Register", "Name", "Value", "Description"],
        tablefmt="presto",  # Using presto format which has better column separation
        numalign="right",
        stralign="left",
        disable_numparse=True  # Prevent number parsing which can affect alignment
    ))
