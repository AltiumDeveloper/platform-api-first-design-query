def print_delimiter_1():
    print("########################################\n")

def print_delimiter_2():
    print("----------------------------------------\n")

def print_nested(data, indent=0):
    spacing = "  " * indent

    if not isinstance(data, dict):
        print(f"{spacing}{data}")
        return

    # Calculate max width of keys at this level for vertical colon alignment
    max_key_len = max(len(str(k)) for k in data.keys())

    for key in data.keys():
        value = data[key]

        # Go into the next level of nesting
        if isinstance(value, dict):
            print(f"\n{spacing}{key}:")
            print_nested(value, indent + 2)

        elif isinstance(value, list):
            # Align the key and colon
            print(f"{spacing}{str(key):<{max_key_len}} :")
            for item in value:
                # Align bullet points under where the value would start
                print(f"{spacing}{' ' * (max_key_len + 3)} - {item}")

        else:
            # Key aligned to max width, followed by a colon and double tabs
            print(f"{spacing}{str(key):<{max_key_len}} :\t\t{value}")
