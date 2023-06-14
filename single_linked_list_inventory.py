class Product:
    def __init__(self, name, code, stock):
        self.name = name
        self.code = code
        self.stock = stock
        self.next = None


class InventoryManagement:
    def __init__(self):
        self.head = None

    def add_product(self, name, code, stock):
        new_product = Product(name, code, stock)

        if self.head is None:
            self.head = new_product
        else:
            current_product = self.head
            while current_product.next is not None:
                current_product = current_product.next
            current_product.next = new_product

        print(
            "Produk '{}' dengan kode '{}' dan jumlah stok {} telah ditambahkan.".format(
                name, code, stock
            )
        )

    def remove_product(self, code):
        if self.head is None:
            print("Inventaris kosong.")
            return

        if self.head.code == code:
            self.head = self.head.next
            print("Produk dengan kode '{}' telah dihapus dari inventaris.".format(code))
            return

        current_product = self.head
        while current_product.next is not None and current_product.next.code != code:
            current_product = current_product.next

        if current_product.next is None:
            print(
                "Produk dengan kode '{}' tidak ditemukan dalam inventaris.".format(code)
            )
        else:
            current_product.next = current_product.next.next
            print("Produk dengan kode '{}' telah dihapus dari inventaris.".format(code))

    def print_inventory(self):
        if self.head is None:
            print("Inventaris kosong.")
        else:
            current_product = self.head
            print("Daftar Produk dalam Inventaris:")
            print("-------------------------------")
            while current_product is not None:
                print(
                    "Nama Produk: {}, Kode: {}, Jumlah Stok: {}".format(
                        current_product.name,
                        current_product.code,
                        current_product.stock,
                    )
                )
                current_product = current_product.next
            print("-------------------------------")


inventory = InventoryManagement()

inventory.add_product("Mouse", "M001", 50)
inventory.add_product("Keyboard", "K001", 30)
inventory.add_product("Monitor", "M002", 20)

inventory.print_inventory()

inventory.remove_product("K001")

inventory.print_inventory()
