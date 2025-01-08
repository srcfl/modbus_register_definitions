import os
import importlib.util
from pathlib import Path

def load_module_from_file(file_path, module_name):
    """Load a Python module from file path."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def get_registers_from_module(module):
    """Extract register profile from module."""
    # Look for *_profile variable in the module
    profile_var = next((var for var in dir(module) if var.endswith('_profile')), None)
    if profile_var:
        return getattr(module, profile_var)
    return None

def format_registers(registers_dict):
    """Format registers into markdown text."""
    from src.modbus.register_definition_keys import ProfileKey, RegistersKey
    
    output = []
    if ProfileKey.REGISTERS in registers_dict:
        for reg in registers_dict[ProfileKey.REGISTERS]:
            name = reg.get(RegistersKey.NAME, "Unknown")
            unit = reg.get(RegistersKey.UNIT, "N/A")
            desc = reg.get(RegistersKey.DESCRIPTION, "No description")
            output.append(f"- **{name}** ({unit}) - {desc}")
    return "\n".join(output)

def main():
    # Get the project root directory
    project_root = Path(__file__).parent
    inverters_dir = project_root / "src" / "inverters"
    
    # Process each inverter directory
    for manufacturer_dir in inverters_dir.iterdir():
        if not manufacturer_dir.is_dir() or manufacturer_dir.name == '__pycache__':
            continue
            
        # Look for the main inverter file (same name as directory)
        inverter_file = manufacturer_dir / f"{manufacturer_dir.name}.py"
        if not inverter_file.exists():
            continue
            
        try:
            # Load the module
            module = load_module_from_file(inverter_file, manufacturer_dir.name)
            registers = get_registers_from_module(module)
            
            if registers:
                print(f"\n# {manufacturer_dir.name.title()} Registers")
                print(format_registers(registers))
                
        except Exception as e:
            print(f"Error processing {manufacturer_dir.name}: {str(e)}")

if __name__ == "__main__":
    main()
