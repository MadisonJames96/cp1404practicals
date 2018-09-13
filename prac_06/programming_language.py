
class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in 1991".format(self.name, self.typing, self.reflection, self.year)

