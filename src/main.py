import os, base64

__version__ = "1.40.31"

class CustomWASM:
    def __init__(self, stub_path: str) -> None:
        self.path = stub_path

    def compile_wasm(self):
        os.system(f'cd assets && wat2wasm custom_{__version__.replace(".", "_")}.wat -o build.wasm')
        print(f'[+] [{__version__}] Wasm compiled ')

    def build_custom(self) -> None:
        with open(self.path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    def replace_wasm(self, b64: str) -> None:
        with open("./assets/stub.js", "r+") as f:
            with open("./out/hsw_bind.js", "w+") as hsw:
                hsw.write(f.read().replace("|replace_wasm|", b64))
        
        print(f'[+] [{__version__}] Hsw wasm replaced')

    def run(self):
        self.compile_wasm()

        b64 = self.build_custom()
        self.replace_wasm(b64)


if __name__ == "__main__":
    CustomWASM("../src/assets/build.wasm").run()