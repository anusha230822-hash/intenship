class Laptop:
    def __init__(self, brand, model, cpu, ram_gb, storage_gb):
        self.brand = brand
        self.model = model
        self.cpu = cpu
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb

    def specs(self):
        print(f"{self.brand} {self.model}: CPU={self.cpu}, RAM={self.ram_gb}GB, Storage={self.storage_gb}GB")

if __name__ == '__main__':
    l = Laptop('Dell', 'XPS 13', 'Intel i7', 16, 512)
    l.specs()
