#
#                IsThicc API Python Wrapper __init__.py | 2020-2021 (c) IsThicc
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
__version__ = "0.1.0"
__author__  = "IsThicc Software"
__name__    = "IsThicc"
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import updates
from config  import url
from asyncio import get_event_loop
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
async def info():
    """

    :return:
    """

    print(
        '\n'
        'IsThicc Python API Wrapper!'
        '\n \n'
        f'Your current API Version is {__version__}!'
        '\n'
        f'You are behind on {await updates.behind()} updates!'
    )

    if url != "https://api.isthicc.dev/v1/":

        print(
            '\n \n'
            'You are using an unofficial API URL. You cannot receive support!'
        )

    print(
        '\n'
        'Check more project from the IsThicc Developers at:'
        '\n'
        'https://isthicc.dev/'
    )

#
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
if __name__ == "__main__":
    loop = get_event_loop()
    loop.run_until_complete(info())
