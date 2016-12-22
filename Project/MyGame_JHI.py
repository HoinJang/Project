import os
import platform
if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import Start_State_JHI
import Framework_JHI

Framework_JHI.run(Start_State_JHI)
