import base64

# Replace 'your-wasm-file.wasm' with the path to your WASM file
wasm_file_path = 'clean.wasm'

try:
    # Open the WASM file in binary mode and read its contents
    with open(wasm_file_path, 'rb') as wasm_file:
        wasm_bytes = wasm_file.read()
        
        # Encode the binary data as base64
        base64_wasm = base64.b64encode(wasm_bytes).decode('utf-8')
        
        print(base64_wasm)
except FileNotFoundError:
    print(f"Error: File '{wasm_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
