class American():
    pass


class NewYoker(American):
    tshirt = "WHITE"

    def heart_tshirt(self):

        return f"I ❤️ NEW YORK" \
               f" AND I LOVE {self.tshirt} T-SHIRT"


people = NewYoker
print(people.heart_tshirt(NewYoker))
