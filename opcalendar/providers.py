from esi.openapi_clients import ESIClientProvider

from . import __version__

esi = ESIClientProvider(
    compatibility_date="2026-05-19",
    ua_appname="AaOpcalendar",
    ua_version=__version__,
    ua_url="https://github.com/Thrainkrilleve/opcalendartemp",
    tags=["Calendar"],
)
