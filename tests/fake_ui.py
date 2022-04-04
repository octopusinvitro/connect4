class FakeUI:
    def get_column(self, columns):
        return 0

    def set_fake_option(self, option):
        self._option = option

    def get_option(self, options):
        return self._option
