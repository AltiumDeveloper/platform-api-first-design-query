import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(SCRIPT_DIR, '..', '..', 'AltiumClient'))
from api_client import AltiumClient

sys.path.append(os.path.join(SCRIPT_DIR, '..'))
from workspace import query_workspace_DesWorkspaceInfos

from library import query_library_desLibraryComponents

sys.path.append(os.path.join(SCRIPT_DIR, '..', '..', 'Helpers'))
from utils import print_delimiter_1
from utils import print_delimiter_2

# ANSI colours for highlighting non-compliant components in the console.
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# Parameter names (matched case-insensitively, substring) that carry compliance data.
COMPLIANCE_KEYWORDS = ("rohs", "reach", "compliance", "compliant")

# Values that indicate a component is NOT RoHS compliant.
NON_COMPLIANT_VALUES = ("non-compliant", "noncompliant", "not compliant", "no", "false")


def extract_compliance_parameters(component):
    # Return the subset of a component's parameters that relate to compliance.
    details = component.get("details") or {}
    parameters = details.get("parameters") or []
    return [
        p for p in parameters
        if any(keyword in (p.get("name") or "").lower() for keyword in COMPLIANCE_KEYWORDS)
    ]


def rohs_status(compliance_parameters):
    # Return True (compliant), False (not compliant), or None (unknown) for RoHS.
    for p in compliance_parameters:
        if "rohs" not in (p.get("name") or "").lower():
            continue
        value = (p.get("value") or "").strip().lower()
        if not value:
            return None
        if any(bad in value for bad in NON_COMPLIANT_VALUES):
            return False
        return True
    return None


if __name__ == '__main__':

    print("Altium 365 platform-api-first-query")
    print_delimiter_1()

    # *** Paste your credentials here. Use a PAT, or a Client ID / Client Secret / Refresh Token. No token? Visit https://developer.altium.com ***
    PAT = ''
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    REFRESH_TOKEN = ''

    pat = PAT or None
    clientId = CLIENT_ID or None
    clientSecret = CLIENT_SECRET or None
    refreshToken = REFRESH_TOKEN or None

    if pat is None and any(v is None for v in (clientId, clientSecret, refreshToken)):
        sys.exit("Set your credentials at the top of this file: either PAT, or CLIENT_ID / CLIENT_SECRET / REFRESH_TOKEN.")

    client = AltiumClient(clientId, clientSecret, refreshToken, pat, ["design.domain", "user.access", "offline_access"])

    workspaces = client.get_query(query_workspace_DesWorkspaceInfos)["desWorkspaceInfos"]
    grid_prefix = "grid:global::platform:workspace/"
    for workspace in workspaces:
        if not client.token_workspace_scope_match(workspace["workspaceId"].removeprefix(grid_prefix)):
            continue

        variables = {
            'url': workspace["url"]
        }
        client.api_url = workspace["location"]["apiServiceUrl"]
        print(f'library components for workspace: {workspace["name"]} ({client.api_url})')
        print_delimiter_1()

        total = 0
        non_compliant = []
        for page in client.NodeIter(query_library_desLibraryComponents, variables,
                                    lambda x: x["desLibrary"]["components"]):
            for component in page:
                total += 1
                compliance_parameters = extract_compliance_parameters(component)
                status = rohs_status(compliance_parameters)

                if status is True:
                    label = f'{GREEN}RoHS compliant{RESET}'
                elif status is False:
                    label = f'{RED}NOT RoHS compliant{RESET}'
                    non_compliant.append(component)
                else:
                    label = 'RoHS status unknown'

                print(f'Component Id: {component["id"]}')
                print(f'Name        : {component["name"]}')
                print(f'Compliance  : {label}')
                if compliance_parameters:
                    print('Parameters  :')
                    for p in compliance_parameters:
                        print(f'                - {p["name"]} = {p["value"]} ({p["type"]})')
                print()
                print_delimiter_2()

        print_delimiter_1()
        print(f'Scanned {total} component(s) in "{workspace["name"]}".')
        if non_compliant:
            print(f'{RED}{len(non_compliant)} component(s) are NOT RoHS compliant:{RESET}')
            for component in non_compliant:
                print(f'  {RED}- {component["name"]} ({component["id"]}){RESET}')
        else:
            print(f'{GREEN}No non-compliant components found.{RESET}')
        print()
