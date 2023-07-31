from .nodes import IntLiteral, FloatLiteral, StringLiteral, CheckpointListLiteral
from .operations import Operation
from .startup_utils import symlink_web_dir

NODE_CLASS_MAPPINGS = {
    "Int": IntLiteral,
    "Float": FloatLiteral,
    "String": StringLiteral,
    "Operation": Operation,
    "Checkpoint": CheckpointListLiteral,
}

EXTENSION_NAME = "ComfyLiterals"

symlink_web_dir("js", EXTENSION_NAME)
