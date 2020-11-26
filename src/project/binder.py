from flask_injector import request
from injector import Binder


def configure(binder: Binder):
    bind_interfaces(binder, {
    })


def bind_interfaces(binder: Binder, interfaces: dict):
    for interface, implementation in interfaces.items():
        binder.bind(
            interface,
            to=implementation,
            scope=request
        )
