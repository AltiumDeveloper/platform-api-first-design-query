import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(SCRIPT_DIR, '..', '..', 'AltiumClient'))
from api_client import AltiumClient

from workspace import query_workspace_DesWorkspaceInfos
from project import query_project_desProjects
from project import query_project_desProjectById

sys.path.append(os.path.join(SCRIPT_DIR, '..', '..', 'Helpers'))
from utils import print_delimiter_1
from utils import print_delimiter_2
from utils import print_nested

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
        print(f'projects for workspace: {workspace["name"]} ({client.api_url})')
        print_delimiter_1()

        first_project = None
        for page in client.NodeIter(query_project_desProjects, variables, lambda x: x["desProjects"]):
            for project in page:
                if first_project is None:
                    first_project = project
                    
                print(f'Project Id: {project["id"]}')
                print(f'Name: {project["name"]}')
                print(f'Description: {project["description"]}')
                print()
                print_delimiter_2()

        if first_project is not None:
            print(f'Fetching details of the first project: {first_project["name"]}\n')
            print_delimiter_1()
            
            variables = {
                'id': first_project["id"]
            }
            
            project_details = client.get_query(query_project_desProjectById, variables)["desProjectById"]
            if project_details is not None:
                print_nested(project_details)
        