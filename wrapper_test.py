from src.commandblock_py.wrapper import *
from src.commandblock_py.commands import basic_commands as commands
from src.commandblock_py.utils.autofill import *
from src.commandblock_py.utils.selectors import selector

mypack = Datapack_wrap(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tickkk")

@mypack.make_auto_run
@mypack.new_function('load')
def test(ctx):
    ctx.register('say hi')
    #print("hello")

@mypack.make_auto_run
@mypack.new_function('tickkk')
def test2(ctx):
    ctx.register(commands.say('pp'))

@mypack.make_auto_run
@mypack.new_function('p')
def test3(ctx):
    ctx.register(commands.function(test2))

@mypack.make_auto_run
@mypack.new_function('h')
def test4(ctx):
    ctx.register(commands.function('h:h'))

@mypack.make_auto_run
@mypack.new_function('bb')
def test5(ctx):
    ctx.register(commands.function(test))

@mypack.make_auto_run
@mypack.new_function('u')
def hhhhh(ctx):
    ctx.register(commands.kill(selector(type=entities_list.ZOMBIE)))

@mypack.make_auto_run
@mypack.new_function('z', 'z')
def z(ctx):
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))
    ctx.register(commands.say('pp'))

if __name__ == "__main__":
    mypack.gen(zip=False)

""" class test:
    mypack = Datapack_wrap(datapack_name="cool_dasadtapack", namespace_id="asadsdsdbc", pack_version=7, datapack_description="My brand new datapack", loadjson="load", tickjson="tick")

    @mypack.make_auto_run
    @mypack.new_function('load')
    def load(ctx):
        ctx.register('say hi')

    @mypack.make_auto_run
    @mypack.new_function('tick')
    def tick(ctx):
        ctx.register('say hi')

    mypack.gen()

test() """