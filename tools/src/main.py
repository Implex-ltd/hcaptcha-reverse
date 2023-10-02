import os, base64

__n__ = "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"

class CustomWASM:
    def __init__(self, stub_path: str) -> None:
        self.path = stub_path

    def compile_wasm(self):
        os.system('cd assets && wat2wasm custom.wat -o build.wasm')
        print('[+] Wasm compiled')

    def build_custom(self) -> None:
        with open(self.path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    def replace_wasm(self, b64: str) -> None:
        with open("./assets/stub.js", "r+") as f:
            with open("./out/hsw_bind.js", "w+") as hsw:
                hsw.write(f.read().replace("|replace_wasm|", b64))
        
        print('[+] hsw wasm replaced')

    def run(self):
        self.compile_wasm()

        b64 = self.build_custom()
        self.replace_wasm(b64)


class N:
    @staticmethod
    def parse_n(n: str) -> int:
        buff = base64.b64decode(n)

        byte_arr = [b for b in buff]
        bytes_length = len(buff)
        cipher_text = "".join([chr(b) for b in buff])

        print(
            f"""
        \r[cyper-text] {cipher_text}
        \r[n-bytes] {byte_arr[:50]}
        \r[n-len] {len(n)}
        \r[b64-bytes] {bytes_length}
        """
        )


if __name__ == "__main__":
    N.parse_n(__n__)
    
    #CustomWASM("../src/assets/build.wasm").run()