class Item:
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance
        self.next = None


class Inventory:
    def __init__(self):
        self.head = None

    def add_item(self, name, importance):
        new_item = Item(name, importance)

        if self.head is None:
            self.head = new_item
        else:
            current_item = self.head
            if current_item.importance < importance:
                new_item.next = current_item
                self.head = new_item
            else:
                while (
                    current_item.next is not None
                    and current_item.next.importance >= importance
                ):
                    current_item = current_item.next
                new_item.next = current_item.next
                current_item.next = new_item

        print(
            "Item '{}' dengan tingkat kepentingan {} telah ditambahkan ke dalam tas.".format(
                name, importance
            )
        )

    def remove_item(self, name):
        if self.head is None:
            print("Tas kosong.")
            return

        if self.head.name == name:
            self.head = self.head.next
            print("Item '{}' telah dihapus dari tas.".format(name))
            return

        current_item = self.head
        while current_item.next is not None and current_item.next.name != name:
            current_item = current_item.next

        if current_item.next is None:
            print("Item '{}' tidak ditemukan dalam tas.".format(name))
        else:
            current_item.next = current_item.next.next
            print("Item '{}' telah dihapus dari tas.".format(name))

    def print_inventory(self):
        if self.head is None:
            print("Tas kosong.")
        else:
            current_item = self.head
            print("Daftar Item dalam Tas:")
            print("----------------------")
            while current_item is not None:
                print(
                    "Nama Item: {}, Tingkat Kepentingan: {}".format(
                        current_item.name, current_item.importance
                    )
                )
                current_item = current_item.next
            print("----------------------")


inventory = Inventory()

inventory.add_item("Immortal", 5)
inventory.add_item("Winter Tracsion", 3)
inventory.add_item("Wind Of Natur", 7)

inventory.print_inventory()

inventory.remove_item("Potion")

inventory.print_inventory()
