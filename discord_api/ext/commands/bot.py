from ...client import Client
from ...command import CommandOption, Command
from inspect import signature

class Bot(Client):
    def add_command(self, name, coro):
        options = []
        values = signature(coro).parameters.values()
        for p in values:
            option_name = p.name
            option = p.annotation
            if not isinstance(option, CommandOption):
                options.append(CommandOption(name = option_name))
            else:
                options.append(option)
        super().add_command(Command(name = name, description = coro.kwargs.pop("description", "..."), options = options))
    
    def application_command(self, name, **kwargs):
        def deco(coro):
            coro.kwargs = kwargs
            self.add_command(name, coro)
            return coro
        return deco

    def run(self, token):
        super().run(token)
