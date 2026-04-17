import requests

if __name__ == '__main__':
    # *** Paste your Personal Access Token and Workspace URL here. No token? Visit https://developer.altium.com ***
    PAT = '...'
    WORKSPACE_URL = '...'
    query = '''
        query Projects {
            desProjects {
              nodes {
                name
                description
                id
                updatedAt
                variantCount
                url
              }
            }
          }'''

    s = requests.session()
    s.keep_alive = False
    workspaceUrl = WORKSPACE_URL.rstrip('/')
    apiUrl = f'{workspaceUrl}/svc/napi/gateway/graphql'

    print('Altium 365 API - Hello Workspace! - First project...\n======================================================================\n')

    try:
        r = s.post(
            apiUrl,
            json={'query': query},
            headers={'Authorization': f'Bearer {PAT}'}
        )
        response = r.json()
    except Exception as e:
        print(e)
        raise Exception('Error while getting API response. Make sure you paste a valid Personal Access Token into \'pat\'')

    if 'errors' in response:
        for error in response['errors']: print(error["message"])
        raise SystemExit

    if response['data']['desProjects']['nodes']:
        first_project = response['data']['desProjects']['nodes'][0]
        print(f'        name: {first_project["name"]}\n'
              f' description: {first_project["description"]}\n'
              f'          id: {first_project["id"]}\n'
              f'last updated: {first_project["updatedAt"]}\n'
              f'  # variants: {first_project["variantCount"]}\n'
              f' project URL: {first_project["url"]}\n======================================================================')
    else:
        print(f'No projects found in your workspace: {workspaceUrl}')