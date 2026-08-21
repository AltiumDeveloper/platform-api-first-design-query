query_library_desLibraryComponents = '''
query LibraryComponents($url: String!, $end: String) {
    desLibrary(workspaceUrl: $url) {
      components(first: 100, after: $end) {
        nodes {
          id
          name
          details {
            parameters {
              type
              name
              value
            }
          }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
  }'''
