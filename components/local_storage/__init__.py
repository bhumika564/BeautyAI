import streamlit.components.v1 as components
import os

_component_func = components.declare_component(
    "local_storage",
    path=os.path.dirname(os.path.abspath(__file__))
)

def local_storage(action="read", data=None, key=None):
    """
    Access the browser's localStorage.
    action: "read", "write", or "clear"
    data: dictionary to save when action="write"
    """
    return _component_func(action=action, data=data, key=key)
