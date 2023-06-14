class Participant:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
        self.next = None


class Tournament:
    def __init__(self):
        self.head = None

    def register_participant(self, name, ranking):
        new_participant = Participant(name, ranking)

        if self.head is None:
            self.head = new_participant
        else:
            current_participant = self.head
            if current_participant.ranking > ranking:
                new_participant.next = current_participant
                self.head = new_participant
            else:
                while (
                    current_participant.next is not None
                    and current_participant.next.ranking <= ranking
                ):
                    current_participant = current_participant.next
                new_participant.next = current_participant.next
                current_participant.next = new_participant

        print(
            "Peserta '{}' dengan peringkat {} telah terdaftar dalam turnamen.".format(
                name, ranking
            )
        )

    def eliminate_participant(self, name):
        if self.head is None:
            print("Daftar peserta kosong.")
            return

        if self.head.name == name:
            self.head = self.head.next
            print("Peserta '{}' telah dikeluarkan dari turnamen.".format(name))
            return

        current_participant = self.head
        while (
            current_participant.next is not None
            and current_participant.next.name != name
        ):
            current_participant = current_participant.next

        if current_participant.next is None:
            print("Peserta '{}' tidak ditemukan dalam turnamen.".format(name))
        else:
            current_participant.next = current_participant.next.next
            print("Peserta '{}' telah dikeluarkan dari turnamen.".format(name))

    def print_participants(self):
        if self.head is None:
            print("Daftar peserta kosong.")
        else:
            current_participant = self.head
            print("Daftar Peserta Turnamen:")
            print("-------------------------")
            while current_participant is not None:
                print(
                    "Nama Peserta: {}, Peringkat: {}".format(
                        current_participant.name, current_participant.ranking
                    )
                )
                current_participant = current_participant.next
            print("-------------------------")


tournament = Tournament()

tournament.register_participant("Jamal", 1200)
tournament.register_participant("Budi", 1500)
tournament.register_participant("Saepul", 1000)

tournament.print_participants()

tournament.eliminate_participant("Siti")

tournament.print_participants()
