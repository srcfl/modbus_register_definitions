def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    output_lines = []
    in_register = False
    register_lines = []

    for line in lines:
        if '{' in line and 'RegistersKey' in line:
            in_register = True
            register_lines = [line]
        elif in_register:
            register_lines.append(line)
            if '}' in line:
                in_register = False
                # Process the register
                register_text = ''.join(register_lines)

                # Change first key to RegistersKey.NAME
                if 'RegistersKey.' in register_lines[0]:
                    first_line = register_lines[0].split(':', 1)
                    register_lines[0] = f'            RegistersKey.NAME:{first_line[1]}'

                # Adjust number of registers based on data type
                for i, line in enumerate(register_lines):
                    if 'DataTypeKey.' in line:
                        data_type = line.strip().split(
                            'DataTypeKey.')[1].split(',')[0]
                        num_registers = 1  # default for 16-bit
                        if '32' in data_type:
                            num_registers = 2
                        elif '64' in data_type:
                            num_registers = 4

                        # Find and replace NUM_OF_REGISTERS line
                        for j, reg_line in enumerate(register_lines):
                            if 'NUM_OF_REGISTERS' in reg_line:
                                register_lines[
                                    j] = f'            RegistersKey.NUM_OF_REGISTERS: {num_registers},  # {data_type} = {num_registers} registers\n'

                output_lines.extend(register_lines)
            continue

        if not in_register:
            output_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(output_lines)


if __name__ == "__main__":
    input_file = "src/inverters/sofar/sofar.py"
    output_file = "src/inverters/sofar/sofar_modified.py"
    process_file(input_file, output_file)
