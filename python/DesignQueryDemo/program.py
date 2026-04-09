'''Example query for workspace info.'''
import os, sys
#from ..AltiumClient.apiClient import AltiumClient
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(SCRIPT_DIR, '..', 'AltiumClient'))
from apiClient import AltiumClient

gqlQuery = '''
query Workspaces {
    desWorkspaceInfos {
      workspaceId  
      url
      name
      description
      location {
        apiServiceUrl
      }
    }
  }'''

gqlQuery2 = '''
query Projects($url: String!, $end: String) {
    desProjects(workspaceUrl: $url, first: 10, after: $end) {
      nodes {
        id
        name
        description
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }'''

if __name__ == '__main__':

    print("Altium 365 platform-api-first-design-query")
    
    clientId = None
    clientSecret = None
    refreshToken = None

    pat = os.environ.get('A365_PAT')
    
    if pat is None:
        clientId = os.environ.get('A365_CLIENT_ID')
        clientSecret = os.environ.get('A365_CLIENT_SECRET')
        refreshToken = os.environ.get('A365_REFRESH_TOKEN')
        if any(v is None for v in (clientId, clientSecret, refreshToken)):
            sys.exit("Missing environment variable(s). Please set A365_PAT or the triplet A365_CLIENT_ID / A365_CLIENT_SECRET / A365_REFRESH_TOKEN then retry.")
    
    client = AltiumClient(clientId, clientSecret, refreshToken, pat, ['design.domain', 'user.access', 'offline_access'])

    workspaces = client.get_query(gqlQuery)['desWorkspaceInfos']
    grid_prefix = "grid:global::platform:workspace/"
    for workspace in workspaces:
        if not client.token_workspace_scope_match(workspace['workspaceId'].removeprefix(grid_prefix)):
            continue
            
        variables = {
            'url': workspace['url']
        }
        client.api_url = workspace['location']['apiServiceUrl']
        print(f'projects for workspace: {workspace["name"]} ({client.api_url})')

        for page in client.NodeIter(gqlQuery2, variables, lambda x: x['desProjects']):
            for project in page:
                print(f'Project Id: {project["id"]}')
                print(f'Name: {project["name"]}')
                print(f'Description: {project["description"]}')
                print()
