import importlib


readerclass = {
    'tglyph': 'TglyphReader',
}


def Reader(target):
    modname = target
    clsname = readerclass[target]
    modpath = 'thothglyph.reader.{}'.format(modname)
    module = importlib.import_module(modpath)
    return getattr(module, clsname)()
