#
#                  IsThicc API Python Wrapper __init__.py | 2020-2021 (c) IsThicc
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import aiohttp
from ..__init__ import __version__
from ..config   import url
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
async def behind() -> str:
    """
    :return:
    """

    session = aiohttp.ClientSession()
    request = await session.get(f"{url}updates/wrapper/{__version__}")
    json    = await request.json()

    await session.close()

    return json  # TODO: Select the version from the json

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
