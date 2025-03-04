import os
import sys
from pathlib import Path

import folder_paths

comfy_path = os.environ.get('COMFYUI_PATH')

if comfy_path is None:
    # legacy env var
    comfy_path = os.environ.get('COMFYUI_PATH')

if comfy_path is None:
    comfy_path = os.path.abspath(os.path.dirname(sys.modules['__main__'].__file__))


def symlink_web_dir(local_path, extension_name):
    comfy_web_ext_root = Path(os.path.join(comfy_path, "web", "extensions"))
    
    target_dir = Path(os.path.join(comfy_web_ext_root, extension_name))
    extension_path = Path(__file__).parent.resolve()

    if target_dir.exists():
        print(f"Web extensions folder found at {target_dir}")
    elif comfy_web_ext_root.exists():
        try:
            os.symlink((os.path.join(extension_path, local_path)), target_dir)
        except OSError as e:  # OSError
            print(
                f"Error:\n{e}\n"
                f"Failed to create symlink to {target_dir}. Please copy the folder manually.\n"
                f"Source: {os.path.join(extension_path, local_path)}\n"
                f"Target: {target_dir}"
            )
        except Exception as e:
            print(f"Unexpected error:\n{e}")
    else:
        print(
            f"Failed to find comfy root automatically, please copy the folder {os.path.join(extension_path, 'web')} manually in the web/extensions folder of ComfyUI"
        )
